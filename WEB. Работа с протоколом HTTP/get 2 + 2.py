import requests
server = input() + ':' + input()
a = input()
b = input()
params = {
    'a': a,
    'b': b
}
res = requests.get(server, params=params).json()
print(*sorted(res['result']))
print(res['check'])