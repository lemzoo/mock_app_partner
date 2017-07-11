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
