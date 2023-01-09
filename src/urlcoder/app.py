from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UrlParameters(BaseModel):
    data: dict = {'id': 3, 'name': 'Ramil', 'on_page': 10, }


@app.post("/")
async def urlcoder(parameters: UrlParameters):
    base_url = 'http://localhost:8000/?'
    url_tail = ''
    for key, value in parameters.data.items():
        url_tail += f'{key}={value}&'
    result_url = base_url + url_tail
    return {'url': result_url }
