# urlcoder_fastapi
EndPoint for encode url from  several different parameters 


What can you do with it?
----
1. With post request you send list of parameters
2. And backend will send you generated url with this parameters

For play with API:
---
1. Clone rep
2. create venv and install requirements.txt
3. in src/urlcoder directory in terminal write:
      uvicorn app:app --reload
4. check http://127.0.0.1:8000/docs
5. check functionality

UseCase :
---
- post_request :
{ 'id': 3,
  'name': 'Ramil',
  'on_page': 10,
}
- response : 
{ 'url': 'http://localhost:8000/?id=3&name=Ramil&on_page=10 }

