from core.utils.id_generator import IDGenerator


def test_create_id() -> None:
    id_generator: IDGenerator = IDGenerator()

    assert id_generator.create_int_id() == 1
    assert id_generator.create_int_id() == 2


def test_create_uuid() -> None:
    assert isinstance(IDGenerator.create_uuid(), str)
