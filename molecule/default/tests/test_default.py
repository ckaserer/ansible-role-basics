import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_basic_packages(host):
    assert host.package("net-tools").is_installed
    assert host.package("vim-enhanced").is_installed
    assert host.package("wget").is_installed
