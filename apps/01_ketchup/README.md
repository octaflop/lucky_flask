# Hello, World!

To host our web pages we will be using an adorable little python web library known as [Flask](http://flask.pocoo.org)

Go ahead an make a new file and call it `myapp.py`.

Paste the following into the file

```python
from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "It's working!!!"

if __name__ == "__main__":
    app.static_folder = '../static'
    app.static_url_path = 'static'
    app.debug = True
    app.run()
```

and run `python myapp.py`. Open your browser to http://localhost:5000/

*You may need to close the other python server by hitting `ctrl+C`*

Before we dive too much deeper, try changing `"It's working!!!"` to `"Hello world!"`

Note that the server will restart itself. Refresh the web page.

Cool, right?
