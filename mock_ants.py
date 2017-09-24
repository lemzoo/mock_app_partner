from xmltodict import parse

from soap_mock import SoapMock

from flask import logging

logger = logging.getLogger(__name__)

class AntsMock(SoapMock):

    def __init__(self):
        super().__init__('ants')

    def get_variable_value(self, msg):
        separator = '/'
        namespaces = {
            'http://schemas.xmlsoap.org/soap/envelope/': None,
            'TETRATimbreNameSpace': None
        }

        data = parse(msg, process_namespaces=True, namespaces=namespaces)
        if 'consommation' in data['Envelope']['Body']:
            stamp_number = data['Envelope']['Body']['consommation']['numeroTimbre']
            return 'consommation/' + stamp_number
        
        if 'reserver' in data['Envelope']['Body']:
            stamp_number = data['Envelope']['Body']['reserver']['numeroTimbre']
            return 'reserver/' + stamp_number

        if 'isReservable' in data['Envelope']['Body']:
            stamp_number = data['Envelope']['Body']['isReservable']['numeroTimbre']
            return 'isreservable/' + stamp_number
 
        return ''
