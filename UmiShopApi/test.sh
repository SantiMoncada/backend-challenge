curl http://127.0.0.1:8000/user -H 'Content-Type: application/json'
curl http://127.0.0.1:8000/user/4 -H 'Content-Type: application/json'

curl -X POST http://127.0.0.1:8000/user -H 'Content-Type: application/json' \
  -d '{"email": "mike@hey.com", "phone": 444444444, "name": "Michael"}'
curl -X POST http://127.0.0.1:8000/assistance -H 'Content-Type: application/json' \
  -d '{"topic": "sales", "email": "Santi@hey.com"}'