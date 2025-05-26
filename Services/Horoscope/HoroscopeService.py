from Clients.Horoscope.ClientInterface import ClientInterface
from Clients.Translate.LingvaClient import LingvaClient
from Services.Horoscope.HoroscopeInterface import HoroscopeInterface
from Services.Translate.TranslateService import TranslateService


class HoroscopeService(HoroscopeInterface):
    zodiac_api_mapping = {
        "♈ Овен": "aries",
        "♉ Телец": "taurus",
        "♊ Близнецы": "gemini",
        "♋ Рак": "cancer",
        "♌ Лев": "leo",
        "♍ Дева": "virgo",
        "♎ Весы": "libra",
        "♏ Скорпион": "scorpio",
        "♐ Стрелец": "sagittarius",
        "♑ Козерог": "capricorn",
        "♒ Водолей": "aquarius",
        "♓ Рыбы": "pisces"
    }

    def __init__(self, client: ClientInterface):
        self.client = client

    async def get_horoscope(self, zodiac: str) -> str:
        TranslateC = LingvaClient()
        TranslateS = TranslateService(TranslateC)

        response = await self.client.post(endpoint="/get-horoscope/daily", params={
            "sign": self.zodiac_api_mapping[zodiac],
            "day": "today"
        })

        response = await TranslateS.translate("en", "ru", response)

        return response