from requests import get, post, delete, put

url = 'http://127.0.0.1:5000/'
print(get(f'{url}/api/jobs').json())
print(put(f'{url}/api/jobs/1', json={'job': 'second job'}).json())
print(put(f'{url}/api/jobs/9999', json={'job': '5465478'}).json())
print(get(f'{url}/api/jobs').json())


