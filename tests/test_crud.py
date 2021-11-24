import os
import sys

import pytest

from .conftest import TEST_PLAYBOOKS, run_playbook, run_playbook_vcr

IGNORED_WARNINGS = [
    "Activation Key 'Test Activation Key Copy' already exists.",
]

if sys.version_info[0] == 2:
    for envvar in os.environ.keys():
        try:
            os.environ[envvar] = os.environ[envvar].decode('utf-8').encode('ascii', 'ignore')
        except UnicodeError:
            os.environ.pop(envvar)


@pytest.mark.parametrize('module', TEST_PLAYBOOKS)
def test_crud(tmpdir, module, vcrmode):
    if vcrmode == "live":
        run = run_playbook(module)
    else:
        record = vcrmode == "record"
        run = run_playbook_vcr(tmpdir, module, record=record)
    assert run.rc == 0

    _assert_no_warnings(run)


@pytest.mark.parametrize('module', TEST_PLAYBOOKS)
def test_check_mode(tmpdir, module):
    run = run_playbook_vcr(tmpdir, module, check_mode=True)
    assert run.rc == 0

    _assert_no_warnings(run)


def _assert_no_warnings(run):
    for event in run.events:
        # check for play level warnings
        assert not event.get('event_data', {}).get('warning', False)

        # check for task level warnings
        event_warnings = [warning for warning in event.get('event_data', {}).get('res', {}).get('warnings', []) if warning not in IGNORED_WARNINGS]
        assert [] == event_warnings, str(event_warnings)
