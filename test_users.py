from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users/1').json())

print(post('http://localhost:5000/api/v2/users', json=
    {
      "address": "Mars 2",
      "age": 22,
      "email": "petya3@mars.com",
      "name": "Ivanov3",
      "surname": "Petya3"
    }).json())
