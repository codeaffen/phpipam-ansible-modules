# How to contribute to phpipam-ansible-modules

## Did you found a bug?

* Do not open a Github issue if the bug concerns [{php}IPAM](https://github.com/phpipam/phpipam) and not the ansible modules.

* Make sure the bug is not already opened by another user.

* If you can't find an open issue which reflects your observed problem, go ahead and [open a new bug](https://github.com/codeaffen/phpipam-ansible-modules/issues/new?assignees=&labels=bug&template=bug_report.md&title=).

* Provide as much information as mentioned in the bug report template.

## Did you write a patch for an open bug?

* Open new pull request containing the patch.

* Provide a clear description which describes the problem and the solution. Link the existing bug to the PR.

## Do you want to add a new feature?

* Make sure there isn't already a feature request.

* If you can't find an open feature request which describes your feature idea or parts of it, feel free to [open a new feature request](https://github.com/codeaffen/phpipam-ansible-modules/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=).

* Suggest your feature idea within the created feature request.

* Provide as much description as possible to enable others to have a good understanding of what you are doing.

* Point out that you want to start to work on the new feature

* If you want to start to work on a new module we suggest to read [How to write new phpipam modules@codeaffen.org](https://codeaffen.org/2021-01-07-writing-phpipam-ansible-modules/).

### Create your feature in a branch of your fork

Fork our repository and create a new branch for your feature. Then start to work on your feature.

### Add tests for your new feature

To make sure that your feature is working as expected and to make sure that it is not breaking any existing functionality, you should add tests for your new feature. To do so, you

1. need to have a working phpipam installation.
2. export the following environment variables:
   * PHPIPAM_URL - the URL of your phpipam installation (e.g. `https://localhost`)
   * PHPIPAM_USERNAME - the username to login to phpipam
   * PHPIPAM_PASSWORD - the password to login to phpipam
   * PHPIPAM_APPID - the appid to login to phpipam
3. add a new task definition for your new feature in tests/test_playbooks/tasks/
4. add a vars definition for your new feature in tests/test_playbooks/vars/
5. add a crud playbook for your new feature in tests/test_playbooks/
   The playbook should contain the following steps:
   * import vars files `vars/server.yml` and `vars/<yourtest>.yml`
   * tasks for
     * create a new entity
     * create a new entity again to make sure that it will not changed
     * update the entity
     * delete the entity
6. run your test with `ansible-playbook --inventory=tests/inventory/hosts tests/test_playbooks/<yourtest>.yml -vvv` to make sure that your feature is working as expected
7. run your test again with `make test-<yourtest>`
8. run all tests with `make test-all` to make sure that your feature does not break any existing functionality

### Create pull request for your new feature

When you are done, push your changes to your fork and create a pull request. Please make sure that you have squashed your changes before you create the pull request. Provide a clear description of your feature and the changes you made.

## Do you want to contribute to documentation?

* Fork me.

* Create a documentation branch.

* Write your documentation changes.

* Open a PR with your changes.

* Discuss with the team about your changes.

## Thank you for any contribution

We will thank you for heeding the contribution guidelines and we encourage you to contribute and join the team.
