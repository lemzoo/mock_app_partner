from xmltodict import parse

from soap_mock import SoapMock

from flask import logging

logger = logging.getLogger(__name__)

class FneMock(SoapMock):

    def __init__(self):
        super().__init__('fne')

    def get_variable_value(self, msg):
        namespaces = {
            'http://schemas.xmlsoap.org/soap/envelope/': None,
            'http://interieur.gouv.fr/asile/': None
        }
        data = parse(msg, process_namespaces=True, namespaces=namespaces)
        type_flux = data['Envelope']['Body']['consultationFNERequest']['typeFlux']
        numero_etranger = data['Envelope']['Body']['consultationFNERequest']['numeroRessortissantEtranger']
        return numero_etranger
