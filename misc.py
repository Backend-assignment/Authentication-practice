import requests
from randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        base_url = self.base_url
        url = f"{base_url}/api/Misc/Cultures"
        headers = {"X-Api-Key":api_key}
        r = requests.get(url, headers=headers)
        return r.json()
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        base_url = self.base_url
        url = f"{base_url}/api/Misc/Random-Address"
        headers = {"X-Api-Key":api_key}
        params = {"number": number, "culture": "en"}
        r = requests.get(url, params=params, headers=headers)
        return r.status_code

key = "940a688e878544858234dee258149563"

f = Misc()

print(f.get_random_address(key,3))