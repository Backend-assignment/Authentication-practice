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
        base_url = self.base_url
        url = f"{base_url}/api/Finance/CryptoAddress/Types"
        headers = {"X-Api-Key": api_key}
        r = requests.get(url, headers=headers)
        return r.json()

    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        base_url = self.base_url
        url = f"{base_url}/api/Finance/CryptoAddress"
        headers = {"X-Api-Key":api_key}
        params = {"cryptoType":crypto_type}
        r = requests.get(url, headers=headers,params=params)
        return r.json()

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        base_url = self.base_url
        url = f"{base_url}/api/Finance/Countries"
        headers = {"X-Api-Key":api_key}
        r = requests.get(url, headers=headers)
        return r.json()

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        base_url = self.base_url
        url = f"{base_url}/api/Finance/Iban/{countryCode}"
        headers = {"X-Api-Key":api_key}
        r = requests.get(url, headers=headers)
        return r.status_code

key = "940a688e878544858234dee258149563"
f = Finance()

print(f.get_iban_by_country_code("AL",key))