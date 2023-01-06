import requests
from randommer import Randommer


class Card(Randommer):
    def get_card(self, api_key: str, type=None) -> dict:
        '''get card from randommer
        
        Args:
            api_key (str): api key
            type (str): card type

        Returns:
            dict: card data
        '''
        self.base_url = f'{self.get_url()}Card'
        payload = {
            'type':type,
        }
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(), params=payload,headers=header)
        return response.json()


    def get_card_types(self, api_key: str) -> list:
        '''get cars types from randommer

        Args:
            api_key (str): api key
            
        Returns:
            list: list of types
        '''
        self.base_url = f'{self.get_url()}Card/Types'
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(), headers=header)
        return response.json()