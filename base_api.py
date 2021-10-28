from base import Base


class BaseApi(Base):
    def __init__(self, response_txt):
        self.response_txt = response_txt

    def converted_dict(self):
        return dict((x.strip(), y.strip())
                    for x, y in (element.split('=')
                                 for element in self.response_txt.split('&')))
