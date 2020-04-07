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
