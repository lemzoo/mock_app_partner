 ![Codeship Status for lemzoo/mock_app_partner](https://app.codeship.com/projects/a3e12310-49de-0135-be9f-5a37e0b658e1/status?branch=master)](https://app.codeship.com/projects/232357)
 
# Mocker l'application partenaire

1 - Installation

Installing in a virtual env is a good practice

virtualenv -p /usr/bin/python3 venv_mock
. ./venv/bin/activate
Actually install the dependancies

pip install -r requirements.txt

2 - Starting the server

Run with the flask embedded serveur (for test and debug)

```python -m server```

The server should run on the port 5009

3 - Configuring a SoapMock instance

  mocks.append(SoapMock('visabio', 'Call', 'visas', 2))

arguments
 - *Route
 - *Xpath to the variable searched in post soap payload
 - directory to response files ( =route if not set)
 - response time in seconds (0 by default)


you must put response files in `reponses/service_name/` dir.
variable.xml, `__default__.xml` if the file does not exist
