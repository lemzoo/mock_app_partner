from xmltodict import parse

from soap_mock import SoapMock


class VisaBioMock(SoapMock):

    def __init__(self):
        super().__init__('visabio')

    def get_variable_value(self, msg):
        namespaces = {
            'http://schemas.xmlsoap.org/soap/envelope/': None,
            'http://fr.gouv.interieur.bw/sm_get-vlsts_sync/starters/starter-soap-http/xsd': None,
            'http://www.visabio.fr/france/visabio/xsd/v1/nsmessages': None,
            'http://www.visabio.fr/france/visabio/xsd/v1/types/Application': None,
            'http://www.visabio.fr/france/visabio/xsd/v1/types/Common': None,
            'http://www.w3.org/2001/XMLSchema-instance': None,
            'http://www.visabio.fr/france/visabio/xsd/v1/nsmessages': None
        }

        data = parse(msg, process_namespaces=True, namespaces=namespaces)
        nsRetrieval = data['Envelope']['Body']['NSRetrieval']
        applicationExamination = nsRetrieval['Request']['Action']['ApplicationExamination']
        visaStickerNumber = applicationExamination['IdentifierChoice']['VisaStickerNumber']
        return visaStickerNumber
