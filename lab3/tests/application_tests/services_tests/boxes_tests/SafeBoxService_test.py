import pytest
from application.services.boxes.SafeBoxService import SafeBoxService
from domain.boxes.SafeBox import SafeBox
from exceptions.infrastructure_errors import RepositoryError
from infrastructure.repositories.BoxRepository import BoxRepository


def test_create_box(service: SafeBoxService, boxes_repo: BoxRepository):
    box: SafeBox = service.create_box(price_per_month=500)
    assert isinstance(box, SafeBox)
    assert box._price_per_month == 500
    assert not box._is_occupied

    saved: SafeBox = boxes_repo.read(box.id)
    assert saved.id == box.id
    assert saved._owner_id is None


def test_rent_box(service: SafeBoxService, boxes_repo: BoxRepository):
    box: SafeBox = service.create_box(price_per_month=1000)
    service.rent_box(box.id, owner_id="test", code="1234", months=3)

    rented: SafeBox = boxes_repo.read(box.id)
    assert rented._is_occupied
    assert rented._owner_id == "test"
    assert rented.verify_access("1234")
    assert not rented.verify_access("9999")
    assert rented._occuplied_until is not None


def test_free_box(service: SafeBoxService, boxes_repo: BoxRepository):
    box: SafeBox = service.create_box(price_per_month=700)
    service.rent_box(box.id, "test", "5555", 1)
    service.free_box(box.id)

    freed: SafeBox = boxes_repo.read(box.id)
    assert not freed._is_occupied
    assert freed._access_code is None


def test_get_box_not_found(service: SafeBoxService):
    with pytest.raises(RepositoryError):
        service._get_box(9999)
