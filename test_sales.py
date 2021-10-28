import pickle

from sale_account_num import SaleAccountNumber as SaleModel


class TestSales:

    def test_01_response_code_a01(self):
        sm = SaleModel
        r_model = sm.request_model
        r_model.city = "Odessa"
        request = r_model.request_number()
        response_text = sm(request).response_text()
        resp_code = sm.response_model.parse_obj(response_text).responseCode
        assert resp_code == "A01"

    def test_02_csc_response_code_m(self):
        sm = SaleModel
        r_model = sm.request_model
        r_model.csc = "111"
        request = r_model.request_number()
        response_text = sm(request).response_text()
        resp_code = sm.response_model.parse_obj(response_text).cscResponseCode
        assert resp_code == "M"

    def test_03_response_code_d05(self):
        sm = SaleModel
        r_model = sm.request_model
        r_model.accountData = sm.accountData
        request = r_model.request_data()
        response = sm(request).response
        response_text = sm(request).response_text()
        print(f'method = {response.request.method}\n'
              f'url = {response.request.url}\n'
              f'body = {response.request.body}\n'
              f'headers = {response.request.headers}\n'
              f'status_code = {response.status_code}\n'
              f'response_content = {response.content}\n')
        resp_code = sm.response_model.parse_obj(response_text).cscResponseCode
        print(f'resp_code ={resp_code}')
        assert resp_code == "D05"

    def test_04_avc_response_code_46(self):
        sm = SaleModel
        r_model = sm.request_model
        r_model.street = ""
        r_model.zipCode = "30301"
        request = r_model.request_number()
        response_text = sm(request).response_text()
        resp_code = sm.response_model.parse_obj(response_text).avsResponseCode
        assert resp_code == "46"
