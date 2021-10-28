import requests
import urllib.parse
from config import config


class Base:
    base_url = "https://qa-unibroker44.unitedthinkers.com/gates/xurl"
    accountData = urllib.parse.quote_plus("(~2001)021301000F3D0000%"
                                          "*4111********1111^SMITH/JOHN^*****************************?*"
                                          "8D40AD26E14C98F73B0210CD5F18A62ACF2B655EABC19BC10DAEEB870B42D6EADC20CE84E3677286B56D6F1C"
                                          "B7C4276C6BF10A91DB9E5947CA68AFD5884C2737312165237673628FB321C9B5F5094594C71F123CE8980E3482F"
                                          "3CB89629949003A0002E000E759D903")

    def post_response(self, request):
        request = {**config(), **request}
        response = requests.post(self.base_url, data=request)
        return response
