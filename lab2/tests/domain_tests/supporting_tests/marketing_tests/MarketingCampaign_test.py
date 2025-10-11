import pytest
from core.enums.Advertisement import Advertisement
from core.enums.Country import Country
from core.exceptions import (
    AdvertisementChannelExistedError,
    BudgetLimitExceededError,
    NotFoundError,
)
from domain.processes.supporting.marketing.AdvertisingChannel import AdvertisingChannel
from domain.processes.supporting.marketing.MarketingCampaign import MarketingCampaign


def test_add_country(marketing_campaign: MarketingCampaign) -> None:
    marketing_campaign.add_country(Country.BELARUS)

    assert marketing_campaign._target_countries[0] == Country.BELARUS


def test_remove_country(marketing_campaign: MarketingCampaign) -> None:
    marketing_campaign.add_country(Country.BELARUS)

    marketing_campaign.remove_country(Country.BELARUS)

    assert len(marketing_campaign._target_countries) == 0


def test_add_channel(
    marketing_campaign: MarketingCampaign, channel: AdvertisingChannel
) -> None:
    marketing_campaign.add_channel(channel, 100)

    assert marketing_campaign._budget._amount_spend == 100
    assert marketing_campaign._channels[0] == channel
    assert channel._budget == 100


def test_add_channel_with_budget_error(
    marketing_campaign: MarketingCampaign, channel: AdvertisingChannel
) -> None:
    with pytest.raises(BudgetLimitExceededError):
        marketing_campaign.add_channel(channel, 1100)


def test_add_channel_with_channel_error(
    marketing_campaign: MarketingCampaign, channel: AdvertisingChannel
) -> None:
    marketing_campaign.add_channel(channel, 100)

    with pytest.raises(AdvertisementChannelExistedError):
        marketing_campaign.add_channel(channel, 100)


def test_remove_channel(
    marketing_campaign: MarketingCampaign, channel: AdvertisingChannel
) -> None:
    marketing_campaign.add_channel(channel, 100)

    marketing_campaign.remove_channel(channel)

    assert len(marketing_campaign._channels) == 0


def test_remove_chanel_with_error(marketing_campaign: MarketingCampaign) -> None:
    channel: AdvertisingChannel = AdvertisingChannel(Advertisement.TIKTOK, "a")
    with pytest.raises(NotFoundError):
        marketing_campaign.remove_channel(channel)


def test_start_campaign(marketing_campaign: MarketingCampaign) -> None:
    marketing_campaign.start_campaign()

    assert marketing_campaign._status == "active"


def test_finish_campaign(marketing_campaign: MarketingCampaign) -> None:
    marketing_campaign.finish_campaign()

    assert marketing_campaign._status == "completed"
