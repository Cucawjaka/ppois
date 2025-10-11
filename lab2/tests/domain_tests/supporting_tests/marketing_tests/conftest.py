import pytest

from core.enums.Advertisement import Advertisement
from domain.processes.supporting.finance.Budget import Budget
from domain.processes.supporting.marketing.AdvertisingChannel import AdvertisingChannel
from domain.processes.supporting.marketing.MarketingCampaign import MarketingCampaign
from domain.processes.supporting.marketing.MarketingDepartment import (
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
