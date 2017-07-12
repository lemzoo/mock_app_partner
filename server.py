from flask import Flask, abort, request
from soap_mock import SoapMock

app = Flask(__name__)


@app.route('/partenaire', methods=['POST'])
def handle_home():
    message = request.get_json()
    context = message.get('context', {})
    mocked = context.get('mock', False)

    if mocked:
        return "Le message a bien ete traite avec succes"
    else:
        abort(400, "L'application partenaire est momentanement indisponible")

@app.route('/partenaires/<partenaire>', methods=['POST'])
def handle_request(partenaire):
    mocks = []
    mocks.append(SoapMock('visabio', 'Call', 'visabio', 1))
    
    response = ''
    
    for mock in mocks:
        if mock.get_route() == partenaire:
            response, status = mock.handle(request)
            break

    if response !='':
        return response, status
    
    abort(400, "L'application partenaire est momentanement indisponible")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)
