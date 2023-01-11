import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        self.base_url = f'{self.get_url()}SocialNumber'
        header = {
            'X-Api-Key':api_key
        }
        response = requests.get(self.get_url(),headers=header)
        return response.json()