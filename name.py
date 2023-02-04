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
        base_url = self.base_url
        url = f"{base_url}/api/Name"
        headers = {"X-Api-Key":api_key}
        params = {"nameType": nameType, "quantity":quantity}
        r = requests.get(url, headers=headers)
        return r.json()
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        base_url = self.base_url
        url = f"{base_url}"
        headers = {"X-Api-Key":api_key}
        params = {"startingWords": startingWords}
        r = requests.get(url, params=params, headers=headers)
        return r.json()
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        headers = {"X-Api-Key":api_key}
        r = requests.get(f'{self.get_url()}Name/Cultures', headers=headers)
        return r.status_code


