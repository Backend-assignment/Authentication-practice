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
        url = f"{self.get_url()}Finance/CryptoAddress/Types"
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        url = f'{self.get_url()}Finance/CryptoAddress'
        headers = {
            "X-Api-Key": api_key
        }
        parametrs = {
            "cryptoType": crypto_type
        }
        response = requests.get(url, params=parametrs, headers=headers)
        return response.json()

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        url = f"{self.get_url()}Finance/Countries"
        headers = {
            "X-Api-Key" :  api_key
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        countryCode = "TN"
        url = f"{self.get_url()}Finance/Iban/{countryCode}"
        header = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, headers=header)
        return response.json()
finance = Finance()
api_key = '9174cdd006f046029c4def5446299088'        
print(finance.get_crypto_address_types(api_key))
print(finance.get_crypto_address('Koto', api_key))
print(finance.get_countries(api_key))
countryCode = "TN"
print(finance.get_iban_by_country_code(countryCode, api_key))