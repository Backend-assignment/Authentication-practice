import requests
from randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        self.base_url = f'{self.get_url()}Name'
        paylod = {
            'nameType':nameType,
            'quantity':quantity
        }
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(),params=paylod,headers=header)
        return response.json()

    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        self.base_url = f'{self.get_url()}Name/Suggestions'
        payload = {
            'startingWords':startingWords
        }
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(),params=payload,headers=header)
        return response.json()
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        self.base_url = f'{self.get_url()}Name/Cultures'
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(),headers=header)
        return response.json()