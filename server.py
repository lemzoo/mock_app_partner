from flask import Flask, abort, request
from soap_mock import SoapMock
import json

app = Flask(__name__)

def get_mocks():
    mocks = []
    mocks.append(SoapMock('visabio', 'Call'))
    return mocks


@app.route('/partenaire', methods=['POST'])
def handle_home():
    message = request.get_json()
    context = message.get('context', {})
    mocked = context.get('mock', False)

    if mocked:
        return "Le message a bien ete traite avec succes"
    else:
        abort(400, "L'application partenaire est momentanement indisponible")

@app.route('/partenaires/list', methods=['GET'])
def handle_list_request():
    mocks = get_mocks()
    response = '{'
    for mock in mocks:
        response += '"%s": {"status": "%s", "tag": "%s", "directory": "%s", "response time": "%s", "files": %s}' % (
            mock.route, 
            'enabled' if mock.enabled else 'disabled', 
            mock.variable_xpath, 
            mock.responses_dir + mock.separator + mock.directory, 
            mock.response_time,
            json.dumps(mock.get_response_files())
        )
    response += '}'
    return response

@app.route('/partenaires/<partenaire>', methods=['POST'])
def handle_mock_request(partenaire):
    mocks = get_mocks()
    
    response = ''
    status = 404
    
    for mock in mocks:
        if mock.get_route() == partenaire:
            status, response = mock.handle(request)
            break

    if response !='':
        return response
    
    abort(status, "L'application partenaire est momentanement indisponible")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5099)
