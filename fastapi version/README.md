1. Create virtual environment

2. `pip install -r requirements.txt`

3. Fire-up the program

    1. `uvicorn --app-dir src run:app --reload`

    2. `python src/run.py`

* **On terminal**

```bash
$ curl http://localhost:5000/ -v
{'message': 'Welcome To TextSummarization.com'}
$ curl -X POST http://127.0.0.1:8000/summary -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"text\":\"This is a very long paragraph\",\"max_length\":20}"
{"summary_text": "This is a very long ar"}
```