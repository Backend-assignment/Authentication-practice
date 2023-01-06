import requests
from randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        self.base_url = f'{self.get_url()}Finance/CryptoAddress/Types'
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(),headers=header)
        return response.json()

    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        self.base_url = f'{self.get_url()}Finance/CryptoAddress'
        payload = {
            'cryptoType':crypto_type
        }
        header = {
            'X-Api-Key':api_key
        }

        response = requests.get(self.get_url(),params=payload,headers=header)
        return response.json()

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        self.base_url = f'{self.get_url()}Finance/Countries'
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(), headers=header)
        return response.json()

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        self.base_url = f'{self.get_url()}Finance/Iban/{country_code}'
        payload = {
            'countryCode':country_code
        }
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(),params=payload,headers=header)
        return response