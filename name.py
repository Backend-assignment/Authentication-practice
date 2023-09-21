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
        url = f"{self.get_url()}Name"

        headers = {
            "X-Api-Key": api_key
        }
        parametrs = {
            'nameType': nameType,
            'quantity': quantity
        }

        response = requests.get(url, params=parametrs, headers= headers)
        return response.json()
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        url = f"{self.get_url()}Name/Suggestions"

        headers = {
            "X-Api-Key": api_key
        }
        
        parametrs = {
            'startingWords' : startingWords
        }
    
        response = requests.get(url, params=parametrs, headers=headers)
        return response.json()

    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        url = f"{self.get_url()}Name/Cultures"
        header = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, headers=header)
        return response.json()
    
name = Name()
nametype = 'firstname'
quantity = 7
api_key = '9174cdd006f046029c4def5446299088'
# print(name.get_name(api_key, nametype, quantity))
# print(name.get_name_suggestions(api_key, startingWords="Krisha"))
print(name.get_name_cultures(api_key))