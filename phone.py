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
        url = f"{self.get_url()}Phone/Generate"
        headers = {
            "X-Api-Key": api_key
        }
        parametrs = {
            "CountryCode": CountryCode,
            "Quantity": Quantity
        }
        response = requests.get(url, params=parametrs, headers=headers)
        return response.json()
    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        url = f"{self.get_url()}Phone/IMEI"
        headers = {
            "X-Api-Key": api_key
        }
        parametrs = {
            "Quantity" : quantity
        }
        response = requests.get(url, params=parametrs, headers=headers)
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
        url = f'{self.get_url()}Phone/Validate'
        headers = {
            'X-Api-Key': api_key
        }
        parametrs = {
            'telephone': telephone,
            'CountryCode': CountryCode
        }

        response = requests.get(url, params=parametrs, headers=headers)
        return response.json()
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        url = f'{self.get_url()}Phone/Countries'
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, headers=headers)
        return response.json()

key = '9174cdd006f046029c4def5446299088'
c_code = 'uz'
quantity = 5
# print(Phone().generate(key, c_code, quantity))
# print(Phone().get_IMEI(key,quantity))
# print(Phone().is_valid(key, '+998 20 016 00 09', 'uz'))
print(Phone().get_countries(key))