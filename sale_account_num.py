from datetime import datetime
from typing import Dict, List, Optional, Union, TypeVar, Generic

import requests
from pydantic import BaseModel, constr
from base import Base
from base_api import BaseApi


class SaleAccNumResponseModel(BaseModel):
    responseType: str = None
    transactionId: int = None
    accountId: str = None
    transactionDate: Optional[datetime] = None
    responseCode: constr(max_length=5) = None
    responseMessage: constr(max_length=255) = None
    transactionCode: constr(max_length=60) = None
    avsResponseCode: constr(max_length=2) = None
    approvalCode: Optional[str] = None
    cycleCode: Optional[str] = None
    accountType: str = None
    extendedAccountType: str = None
    providerResponseCode: Optional[constr(max_length=20)] = None
    providerResponseMessage: Optional[constr(max_length=260)] = None
    cscResponseCode: Optional[str] = None


class SaleAccNumRequestModel(BaseModel):
    requestType: str = None
    amount: int = None
    accountType: str = None
    transactionIndustryType: str = None
    holderType: Optional[str] = None
    holderName: str = None
    accountNumber: str = None
    accountAccessory: str = None
    accountData: str = None
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipCode: Optional[str] = None
    customerAccountCode: Optional[str] = None
    transactionCode: Optional[str] = None
    csc: Optional[constr(max_length=4)] = None

    def payload_number(self, requestType="sale", amount=5000, accountType="R",
                       transactionIndustryType="RE", holderName="John Smith",
                       accountNumber="4111111111111111", accountAccessory="0422"):
        self.requestType = requestType
        self.amount = amount
        self.accountType = accountType
        self.transactionIndustryType = transactionIndustryType
        self.holderName = holderName
        self.accountNumber = accountNumber
        self.accountAccessory = accountAccessory
        return self

    def payload_data(self, requestType="sale", amount=5000, accountType="R",
                     transactionIndustryType="RE"):
        self.requestType = requestType
        self.amount = amount
        self.accountType = accountType
        self.transactionIndustryType = transactionIndustryType
        return self

    def request_number(self):
        return self.payload_number().dict(exclude_none=True, by_alias=True)

    def request_data(self):
        return self.payload_data().dict(exclude_none=True, by_alias=True)


class SaleAccountNumber(Base):
    response_model = SaleAccNumResponseModel()
    request_model = SaleAccNumRequestModel()

    def __init__(self, request):
        self.response = self.post_response(request)

    def response_text(self):
        return BaseApi(self.response.text).converted_dict()
