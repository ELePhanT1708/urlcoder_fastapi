# urlcoder_fastapi
EndPoint for encode url from  several different parameters 


What can you do with it?
----
1. With post request you send list of parameters
2. And backend will send you generated url with this parameters


UseCase :
---
- post_request :
{ 'id': 3,
  'name': 'Ramil',
  'on_page': 10,
}
- response : 
{ 'url': 'http://localhost:8000/?id=3&name=Ramil&on_page=10 }

