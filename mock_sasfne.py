from soap_mock import SoapMock


class SasFneMock(SoapMock):

    def __init__(self):
        super().__init__('sasfne')
        self.set_auth('siaef', 'P@ssw0rd')

    def get_variable_value(self, msg):
        return ''
