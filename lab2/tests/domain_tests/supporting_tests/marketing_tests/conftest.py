import pytest

from core.enums.advertisement import Advertisement
from domain.processes.supporting.finance.budget import Budget
from domain.processes.supporting.marketing.advertising_channel import AdvertisingChannel
from domain.processes.supporting.marketing.marketing_campaign import MarketingCampaign
from domain.processes.supporting.marketing.marketing_department import (
    MarketingDepatment,
)


@pytest.fixture
def marketing_department(budget: Budget) -> MarketingDepatment:
    return MarketingDepatment(budget)


@pytest.fixture
def marketing_campaign(budget: Budget) -> MarketingCampaign:
    return MarketingCampaign("test", budget)


@pytest.fixture
def channel() -> AdvertisingChannel:
    return AdvertisingChannel(Advertisement.TIKTOK, "tiktok")
