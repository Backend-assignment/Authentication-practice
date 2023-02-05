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
        base_url = self.base_url
        url = f"{base_url}/api/SocialNumber"
        headers = {"X-Api-Key": api_key}
        r = requests.get(url, headers=headers)
        return r.json()
ilhomjan_154_ = SocialNumber()
key = "940a688e878544858234dee258149563"
print(ilhomjan_154_.get_SocialNumber(key))