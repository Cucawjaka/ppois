import pytest
from core.exceptions import NotFoundError
from domain.processes.supporting.marketing.campaign_report import CampaignReport
from domain.processes.supporting.marketing.marketing_campaign import MarketingCampaign
from domain.processes.supporting.marketing.marketing_department import (
    MarketingDepatment,
)


def test_create_campaign(marketing_department: MarketingDepatment) -> None:
    marketing_campaign: MarketingCampaign = marketing_department.create_campaign(
        "test", 800
    )

    assert marketing_campaign.name == "test"
    assert marketing_campaign._budget._amount_allocated == 800
    assert marketing_department._budget._amount_spend == 800
    assert len(marketing_department._campaigns) == 1


def test_analyze_campaign(marketing_department: MarketingDepatment) -> None:
    _: MarketingCampaign = marketing_department.create_campaign("test", 800)

    report: CampaignReport = marketing_department.analyze_campaign("test", 400)

    assert report.name == "test"
    assert report.roi == 50


def test_analyze_campaign_with_error(marketing_department: MarketingDepatment) -> None:
    with pytest.raises(NotFoundError):
        marketing_department.analyze_campaign("test_campaign", 800)
