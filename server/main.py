import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3,4,5]

@app.get("/products")
def get_data():
    return [{
        "id": 1,
        "title": "Playera",
        "price": 25,
        "description": "bla bla bla",
        "image": "https://www.google.com"
    }]

@app.get("/page", response_class=HTMLResponse)
def get_page():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

def run():
    store.get_products()

if __name__ == '__main__':
    run()
