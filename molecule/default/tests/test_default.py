import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_net_tools(host):
    net_tools = host.package("net-tools")
    assert net_tools.is_installed


def test_wget(host):
    wget = host.package("wget")
    assert wget.is_installed


def test_vim(host):
    wget = host.package("vim")
    assert wget.is_installed
