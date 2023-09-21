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
        url = f"{self.get_url()}Misc/Cultures"
        header = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, headers=header)
        return response.json()
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        url = f"{self.get_url()}Misc/Random-Address"
        headers = {
            "X-Api-Key": api_key
        }
        parametrs = {
            "number": number,
            'culture': culture
        }
        response = requests.get(url, params=parametrs, headers=headers)
        return response.json()
    
api_key = '9174cdd006f046029c4def5446299088'
misc = Misc()
culture = 'ro'
print(misc.get_cultures(api_key))
print(misc.get_random_address(api_key, 5, culture))