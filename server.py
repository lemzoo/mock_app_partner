from flask import Flask, abort
from requests import request


app = Flask(__name__)


@app.route('/partenaire', methods=['POST'])
def handle_request():
    message = request.get_json()
    context = message.get('context', {})
    mocked = context.get('mock', False)

    if mocked:
        return "Le message a bien ete traite avec succes"
    else:
        abort(400, "L'application partenaire est momentanement indisponible")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)
