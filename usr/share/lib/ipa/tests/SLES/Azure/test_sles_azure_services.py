import pytest


@pytest.mark.parametrize('name', [
    ('waagent.service'),
])
def test_sles_azure_services(check_service, name):
    assert check_service(name)
