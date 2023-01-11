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
        self.base_url = f'{self.get_url()}Misc/Cultures'
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(),headers=header)
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
        self.base_url = f'{self.get_url()}Misc/Random-Address'
        payload = {
            'number':number,
            'culture':culture
        }
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(),params=payload,headers=header)
        return response.json()
