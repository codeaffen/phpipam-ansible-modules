import os

import ansible_runner
import pytest
import py.path  # type: ignore
import yaml


TEST_PLAYBOOKS_PATH = py.path.local(__file__).realpath() / '..' / 'test_playbooks'


def find_all_test_playbooks():
    for playbook in TEST_PLAYBOOKS_PATH.listdir(sort=True):
        playbook = playbook.basename
        if playbook.endswith('.yml') and not playbook.startswith('example_'):
            yield playbook.replace('.yml', '')


TEST_PLAYBOOKS = list(find_all_test_playbooks())


def pytest_addoption(parser):
    parser.addoption(
        "--testcase",
        action="store",
        default="",
        help="testcase to run",
    )


@pytest.fixture
def testcase(request):
    return request.config.getoption('testcase')


def get_phpipam_url():
    server_yml = py.path.local(__file__).realpath() / '..' / 'test_playbooks/vars/server.yml'
    with open(server_yml.strpath) as server_yml_file:
        server_yml_content = yaml.safe_load(server_yml_file)

    return server_yml_content['phpipam_server_url']


def run_playbook(module, extra_vars=None, limit=None, inventory=None, check_mode=False, extra_env=None):
    # Assemble parameters for playbook call
    os.environ['ANSIBLE_CONFIG'] = os.path.join(os.getcwd(), 'ansible.cfg')
    if extra_env is not None:
        os.environ.update(extra_env)
    kwargs = {}
    kwargs['playbook'] = os.path.join(os.getcwd(), 'tests', 'test_playbooks', '{}.yml'.format(module))
    if inventory is None:
        inventory = os.path.join(os.getcwd(), 'tests', 'inventory', 'hosts')
    kwargs['inventory'] = inventory
    kwargs['verbosity'] = 4
    if extra_vars:
        kwargs['extravars'] = extra_vars
    if limit:
        kwargs['limit'] = limit
    if check_mode:
        kwargs['cmdline'] = "--check"
    return ansible_runner.run(**kwargs)
