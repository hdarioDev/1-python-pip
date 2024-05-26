import store
from fastapi import FastAPI

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

def run():
    store.get_products()

if __name__ == '__main__':
    run()
