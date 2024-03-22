from requests import get, post, delete


print(get('http://localhost:5000/api/jobs').json())
print(get('http://localhost:5000/api/jobs/1').json())
print(get('http://localhost:5000/api/jobs/999').json())
print(get('http://localhost:5000/api/jobs/wwwqe').json())

# новости с id = 999 нет в базе

print(post('http://localhost:5000/api/jobs',
           json={
               'team_leader':1,
               'job': "Сделать проект по вебу",
               'work_size': 42,
               'is_finished': False}).json())


