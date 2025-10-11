from domain.processes.supporting.marketing.AdvertisingChannel import AdvertisingChannel


def test_calculate_ctr(channel: AdvertisingChannel) -> None:
    channel.record_clicks(100)
    channel.record_shows(200)

    assert channel.calculate_ctr() == 50


def test_calculate_cvr(channel: AdvertisingChannel) -> None:
    channel.record_conversions(25)
    channel.record_clicks(50)

    assert channel.calculate_cvr() == 50
