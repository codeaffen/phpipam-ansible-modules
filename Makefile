NAMESPACE := $(shell python -c 'import yaml; print(yaml.safe_load(open("galaxy.yml"))["namespace"])')
NAME := $(shell python -c 'import yaml; print(yaml.safe_load(open("galaxy.yml"))["name"])')
VERSION := $(shell python -c 'import yaml; print(yaml.safe_load(open("galaxy.yml"))["version"])')
MANIFEST := build/collections/ansible_collections/$(NAMESPACE)/$(NAME)/MANIFEST.json

Roles := $(wildcard roles/*)
PLUGIN_TYPES := $(filter-out __%,$(notdir $(wildcard plugins/*)))
METADATA := galaxy.yml LICENSE README.md requirements.txt
$(foreach PLUGIN_TYPE,$(PLUGIN_TYPES),$(eval _$(PLUGIN_TYPE) := $(filter-out %__init__.py,$(wildcard plugins/$(PLUGIN_TYPE)/*.py))))
DEPENDENCIES := $(METADATA) $(foreach PLUGIN_TYPE,$(PLUGIN_TYPES),$(_$(PLUGIN_TYPE))) $(foreach ROLE,$(ROLES),$(wildcard $(ROLE)/*/*))

PYTHON_VERSION = $(shell python -c 'import sys; print("{}.{}".format(sys.version_info.major, sys.version_info.minor))')
COLLECTION_COMMAND ?= ansible-galaxy
SANITY_OPTS = --venv
TEST =
PYTEST = pytest -n 4 --boxed -v

default: help

help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  help - to show this message"
	@echo "  info - to show infomation about the collection"
	@echo "  lint - to run code linting"
	@echo "  dist - to build the collection archive"

info:
	@echo "Building collection $(NAMESPACE)-$(NAME)-$(VERSION)"
	@echo "  roles:\n $(foreach ROLE,$(notdir $(ROLES)),    - $(ROLE)\n)"
	@echo " $(foreach PLUGIN_TYPE,$(PLUGIN_TYPES), $(PLUGIN_TYPE):\n $(foreach PLUGIN,$(basename $(notdir $(_$(PLUGIN_TYPE)))),   - $(PLUGIN)\n)\n)"

lint: $(MANIFEST)
	flake8 plugins/ tests/

$(MANIFEST): $(NAMESPACE)-$(NAME)-$(VERSION).tar.gz
	ansible-galaxy collection install -p build/collections $< --force

build/src/%: %
	install -m 644 -DT $< $@

$(NAMESPACE)-$(NAME)-$(VERSION).tar.gz: $(addprefix build/src/,$(DEPENDENCIES))
	ansible-galaxy collection build build/src --force

dist: $(NAMESPACE)-$(NAME)-$(VERSION).tar.gz

release-%:
	bumpversion $*
	antsibull-changelog release
	make doc

publish: $(NAMESPACE)-$(NAME)-$(VERSION).tar.gz
	ansible-galaxy collection publish --api-key $(GALAXY_API_KEY) $<

clean:
	rm -rf build
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.tar.gz' -delete

doc-setup:
	pip install -r docs/requirements.txt

doc: $(MANIFEST)
	install -d -m 750 ./docs/plugins
	antsibull-docs collection --use-current --squash-hierarchy --dest-dir ./docs/plugins codeaffen.phpipam
	make -C docs html

FORCE:

.PHONY: help dist lint doc-setup doc publish FORCE
