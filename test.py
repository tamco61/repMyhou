from requests import get
# 1 test
print(get('http://localhost:5000/api/jobs').json())
print(get('http://localhost:5000/api/jobs/1').json())
print(get('http://localhost:5000/api/jobs/9999').json())
print(get('http://localhost:5000/api/jobs/q').json())


# 2 test
from requests import get, post
print(post('http://localhost:5000/api/jobs',
           json={'id': 4,
                 'job': 'Заголовок',
                 'collaborators': 'Текст',
                 'team_leader': 1,
                 'work_size': 20,
                 'is_finished': True}).json())  # корректный
print(post('http://localhost:5000/api/jobs').json())  # пустой запрос
print(post('http://localhost:5000o/api/jobs',
           json={'job': 'Заголовок'}).json())  # не все элементы присутствуют
print(post('http://localhost:5000/api/jobs',
           json={'id': 1,
                 'job': 'Заголовок',
                 'collaborators': 'Текст',
                 'team_leader': 1,
                 'work_size': 20,
                 'is_finished': True}).json())  # с таким id уже есть работа


# 3 test

from requests import get, post, delete
print(post('http://localhost:5000/api/jobs',
           json={'id': 1,
                 'job': '1 job',
                 'collaborators': '5, 7, 8',
                 'team_leader': 2,
                 'work_size': 203,
                 'is_finished': False}).json())
print(delete('http://localhost:5000/api/jobs/1').json())
print(delete('http://localhost:5000/api/jobs/765').json())
print(delete('http://localhost:5000/api/jobs/').json())
print(delete('http://localhost:5000/api/jobs/rte').json())
print(get('http://localhost:5000/api/jobs').json())


# 4 test

from requests import get, post, delete, put
url = 'http://127.0.0.1:5000/'
print(get(f'{url}/api/jobs').json())
print(put(f'{url}/api/jobs/1', json={'job': 'second job'}).json())
print(put(f'{url}/api/jobs/9999', json={'job': '5465478'}).json())
print(get(f'{url}/api/jobs').json())