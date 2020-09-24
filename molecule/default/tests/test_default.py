import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_image_deploy(host):
    assert host.user("image.deploy").exists
    assert host.user("image.deploy").uid == 9576
    assert host.user("image.deploy").gid == 9576
    assert host.user("image.deploy").group == "image.deploy"
    assert host.user("image.deploy").shell == "/bin/bash"
