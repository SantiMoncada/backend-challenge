# Get all users
curl http://127.0.0.1:8000/api/user -H 'Content-Type: application/json'

# get a user
curl http://127.0.0.1:8000/api/user/1 -H 'Content-Type: application/json'

# create a ne wuser
curl -X POST http://127.0.0.1:8000/api/user -H 'Content-Type: application/json' \
  -d '{"email": "mike@hey.com", "phone": 444444444, "name": "Michael"}'

#Send assistance to a customer
curl -X POST http://127.0.0.1:8000/api/assistance -H 'Content-Type: application/json' \
  -d '{"topic": "sales", "email": "Santi@hey.com"}'