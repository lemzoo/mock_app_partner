#! /usr/bin/env python3

import json
from flask import Flask, abort, request

from mock_ants import AntsMock
from mock_visabio import VisabioMock


app = Flask(__name__)


def get_mocks():
    mocks = []
    mocks.append(AntsMock())
    mocks.append(VisabioMock())
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
    for mock in mocks:
        if mock.get_route() == partenaire:
            return mock.handle(request)
    abort(404, "L'application partenaire est momentanement indisponible")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5099)
