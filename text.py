import requests
from randommer import Randommer


class Text(Randommer):
    def generate_LoremIpsum(self, api_key: str, loremType: str, type: str, number: int) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            loremType (str): loremType (normal or bussines)
            type (str): type (words or paragraphs)
            number (int): number

        Returns:
            str: Lorem text
        '''
        base_url = self.base_url
        url = f"{base_url}/api/Text/LoremIpsum"
        headers = {"X-Api-Key": api_key}
        params = {"loremType":loremType, "type":type, "number":number}
        r = requests.get(url, headers=headers, params=params)
        return r.json()
    
    def generate_password(self, api_key: str, length: int, hasDigits: bool, hasUppercase: bool, hasSpecial: bool) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            length (int): lenth of password
            hasDigits (bool): hasDigits
            hasUppercase (bool): hasUppercase
            hasSpecial (bool): hasSpecial

        Returns:
            str: pasword
        '''
        base_url = self.base_url
        url = f"{base_url}/api/Text/Password"
        headers = {"X-Api-Key": api_key}
        params = {
            "length": length,
            "hasDigits": hasDigits,
            "hasUppercase": hasUppercase,
            "hasSpecial": hasSpecial
        }
        r = requests.get(url, headers=headers, params=params)
        return r.json()


key = "940a688e878544858234dee258149563"  

f = Text()

print(f.generate_password(key, 6, True, True, True))