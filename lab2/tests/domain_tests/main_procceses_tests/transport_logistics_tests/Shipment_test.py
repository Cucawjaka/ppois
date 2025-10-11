from domain.processes.main_procceses.transport_logistics.Shipment import Shipment


def test_start(shipment: Shipment) -> None:
    shipment.start()

    assert shipment.status == "in_transit"


def test_complete(shipment: Shipment) -> None:
    shipment.complete()

    assert shipment.status == "delivered"
