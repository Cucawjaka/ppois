from dataclasses import dataclass
from domain.processes.main_procceses.warehouse_logistics.logistic_center import (
    LogisticsCenter,
)


@dataclass
class Route:
    origin: LogisticsCenter
    destination: LogisticsCenter
    checkpoints: list[LogisticsCenter] | None = None

    def get_next_checkpoint(self) -> LogisticsCenter:
        if self.checkpoints:
            return self.checkpoints.pop(0)
        return self.destination
