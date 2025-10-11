from core.enums.Country import Country
from domain.processes.main_procceses.transport_logistics.Route import Route
from domain.processes.main_procceses.warehouse_logistics.LogisticCenter import (
    LogisticsCenter,
)


def test_get_next_checkpoint() -> None:
    center_origin: LogisticsCenter = LogisticsCenter(Country.BELARUS)
    destination_center: LogisticsCenter = LogisticsCenter(Country.BELARUS)
    checkpoint_center: LogisticsCenter = LogisticsCenter(Country.BELARUS)
    route: Route = Route(center_origin, destination_center, [checkpoint_center])

    assert route.get_next_checkpoint() == checkpoint_center
