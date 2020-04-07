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

