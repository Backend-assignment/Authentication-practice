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
        url = f"{self.get_url()}Card"

        headers = {
            'X-Api-Key': api_key
        }

        response = requests.get(url, headers=headers)
        return response.json()

    def get_card_types(self, api_key: str) -> list:
        '''get cars types from randommer

        Args:
            api_key (str): api key
            
        Returns:
            list: list of types
        '''
        url = f'{self.get_url()}Card/Types'
        header = {
            'X-Api-Key': api_key
        }

        response = requests.get(url, headers=header)

        return response.json()

api_key = "9174cdd006f046029c4def5446299088"
print(Card().get_card(api_key))

print(Card().get_card_types(api_key))