import requests
from randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        base_url = self.base_url
        url = f"{base_url}/api/Phone/Generate"
        headers = {"X-Api-Key":api_key}
        params = {"CountryCode": CountryCode, "Quantity":Quantity}
        r = requests.get(url, params=params, headers=headers)
        return r.json()
    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        base_url = self.base_url
        url = f"{base_url}/api/Phone/IMEI"
        headers = {"X-Api-Key":api_key}
        params = {"Quantity": Quantity}
        r = requests.get(url, params=params, headers=headers)
        return r.json()
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        base_url = self.base_url
        url = f"{base_url}/api/Phone/Validate"
        headers = {"X-Api-Key": api_key}
        payload = {"telephone": telephone, "CountryCode": CountryCode}
        r = requests.get(url, params=payload, headers=headers)
        return r.json()
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        base_url = self.base_url
        url = f"{base_url}/api/Phone/Countries"
        headers = {"X-Api-Key": api_key}
        r = requests.get(url, headers=headers)
        return r.json()

key = "940a688e878544858234dee258149563"    

f = Phone()

print(f.get_countries(key))
