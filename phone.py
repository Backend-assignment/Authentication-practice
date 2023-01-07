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
        self.base_url = f'{self.get_url()}Phone/Generate'
        payload = {
            'CountrCode':CountryCode,
            'Quantity':Quantity
        }
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(),params=payload,headers=header)
        return response.json()

    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        self.base_url = f'{self.get_url()}Phone/IMEI'
        payload = {
            'Quantity':Quantity
        }
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(),params=payload,headers=header)
        return response.json()
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        self.base_url = f'{self.get_url()}Phone/Generate'
        payload = {
            'telephone':telephone,
            'CountrCode':CountryCode
        }
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(),params=payload,headers=header)
        return response.json()
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        self.base_url = f'{self.get_url()}Phone/Countries'
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(),headers=header)
        return response.json()
