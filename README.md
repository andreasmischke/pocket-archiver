# Pocket Archiver

## Setup

1.  Create virtualenv: `virtualenv venv --python=python3`
2.  Activate your virtualenv: `source ./venv/bin/activate`
3.  Use pip to install the dependencies: `pip install -r requirements.txt`
4.  Copy the `config.py.template` to `config.py` and fill in the missing values

## Usage

Run the pocket\_archiver.py with python3 and pipe the JSON formatted output
where you want to store it. Make sure to use the virtualenv. E.g.:

```bash
./venv/bin/python pocket\_archiver.py > data.json
```

