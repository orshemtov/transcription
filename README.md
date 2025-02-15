# README

## Requirements

- Python 3.9

## Install

```bash
# Create a virtual env.
python3.9 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

## Run

```bash
fastapi dev # Dev mode
fastapi run # Production mode
```

Go to <http://localhost:8000/docs> to interract with the API.

## Test

```bash
pytest -s -vv
```

```json
{
  "metadata": {
    "duration": 18.3561875,
    "language": "en",
    "language_probability": 0.9975495934486389
  },
  "segments": [
    {
      "end": 4.0,
      "start": 0.0,
      "text": "The stale smell of old beer lingers."
    },
    {
      "end": 7.0,
      "start": 4.0,
      "text": "It takes heat to bring out the odor."
    },
    {
      "end": 10.0,
      "start": 7.0,
      "text": "A cold dip restores health and zest."
    },
    {
      "end": 12.0,
      "start": 10.0,
      "text": "A salt pickle tastes fine with ham."
    },
    {
      "end": 15.0,
      "start": 12.0,
      "text": "Tacos al pastor are my favorite."
    },
    {
      "end": 18.0,
      "start": 15.0,
      "text": "A zestful food is the hot cross bun."
    }
  ]
}
```
