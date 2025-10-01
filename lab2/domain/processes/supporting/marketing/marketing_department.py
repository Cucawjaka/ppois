from dataclasses import dataclass
from core.exceptions import CampaignNotFoundError
from domain.processes.supporting.finance.budget import Budget
from domain.processes.supporting.marketing.marketing_campaign import MarketingCampaign


@dataclass
class CampaignReport:
    name: str
    roi: float


class MarketingDepatment:
    def __init__(self, budget: Budget) -> None:
        self._campaigns: list[MarketingCampaign] = list()
        self._budget: Budget = budget


    def create_campaign(self, name: str, budget_amount: int) -> MarketingCampaign:
        campaign_budget: Budget = self._budget.allocate_subbudget(budget_amount)
        return MarketingCampaign(name, campaign_budget)


    def analyze_campaign(self, campaign_name: str, revenue: int) -> CampaignReport:
        for campaign in self._campaigns:
            if campaign.name == campaign_name:
                campaign_roi = campaign.calculate_roi(revenue)
                return CampaignReport(campaign_name, campaign_roi)
        raise CampaignNotFoundError(f"Кампания с именем {campaign_name} не существует")




    