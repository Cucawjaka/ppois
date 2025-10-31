import pytest

from application.services.boxes.SafeBoxService import SafeBoxService
from core.utils.IDGenerator import IDGenerator
from infrastructure.repositories.BoxRepository import BoxRepository


@pytest.fixture
def boxes_repo() -> BoxRepository:
    return BoxRepository()


@pytest.fixture
def generator() -> IDGenerator:
    return IDGenerator()


@pytest.fixture
def service(generator: IDGenerator, boxes_repo: BoxRepository) -> SafeBoxService:
    return SafeBoxService(generator=generator, repo=boxes_repo)
