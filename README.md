1. Create virtual environment

2. `pip install -r requirements.txt`

3. Fire-up the program, goto `src` directory

    1. For Linux or Mac, 
        * `export FLASK_APP=flaskapp`
        * `export FLASK_ENV=development`
        * `flask run`

    2. For Windows, 
        * `set FLASK_APP=flaskapp`
        * `set FLASK_ENV=development`
        * `flask run`

    3. Or, run `python run.py`

4. (Optional) For testing,
    * Open another terminal and goto `testing` directory
    * Then run, `python test_1.py`

Or

```bash
$ curl http://localhost:5000/ -v
{'message': 'Welcome To TextSummarization.com'}
$ curl http://localhost:5000/summary -d "text=This is very long article" -d "max_length=20" -X POST -v
{"summary_text": "This is very long ar"}
```