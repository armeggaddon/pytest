def test_module_resource(module_resource):
    assert module_resource.read_text() == 'module resource'


def test_yield_fixture(resource_with_teardown):
    assert resource_with_teardown['connected'] is True
