import datetime
from typing import Literal
from core.enums.country import Country
from core.exceptions import (
    AdvertisementChannelExistedError,
    NotFoundError,
)
from core.utils.id_generator import IDGenerator
from domain.processes.supporting.finance.budget import Budget
from domain.processes.supporting.marketing.advertising_channel import AdvertisingChannel


class MarketingCampaign:
    def __init__(self, name: str, budget: Budget) -> None:
        self._id: str = IDGenerator.create_uuid()
        self._name: str = name
        self._budget: Budget = budget
        self._channels: list[AdvertisingChannel] = list()
        self._start_date: datetime.datetime
        self._end_date: datetime.datetime
        self._status: Literal["active", "completed", "planned"] = "planned"
        self._target_countries: list[Country] = list()

    def add_country(self, country: Country) -> None:
        if country in self._target_countries:
            return
        self._target_countries.append(country)

    def remove_country(self, country: Country) -> None:
        try:
            self._target_countries.remove(country)
        except ValueError:
            return

    def add_channel(self, channel: AdvertisingChannel, channel_budget: int) -> None:
        if channel in self._channels:
            raise AdvertisementChannelExistedError("Канал уже существует")

        self._budget.spend(channel_budget)
        channel.set_budget(channel_budget)
        self._channels.append(channel)

    def remove_channel(self, channel: AdvertisingChannel) -> None:
        if channel not in self._channels:
            raise NotFoundError("Такого канала не существует")
        self._channels.remove(channel)

    def start_campaign(self) -> None:
        self._start_date = datetime.datetime.now()
        self._status = "active"

    def finish_campaign(self) -> None:
        self._end_date = datetime.datetime.now()
        self._status = "completed"

    @property
    def name(self) -> str:
        return self._name

    def calculate_roi(self, revenue: int) -> float:
        return revenue / self._budget.amount_allocated * 100
