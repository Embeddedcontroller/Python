import base64
import os

url = input()
base64_info = url[6:].replace('-', '+').replace('_', '/')
# print(base64_info)
info = base64.b64decode(base64_info).decode('utf-8')
# print(f'{info}')

params, base64_params = info.split('/?')
# print(f'{params}\n{base64_params}')
base64_params = base64_params.replace('-', '+').replace('_', '/')

address, port, protocol, method, obfs, password_base64 = params.split(':')
password_base64 = password_base64.replace('-', '+').replace('_', '/')
if len(password_base64) % 3 == 1:
    password_base64 += '=='
elif len(password_base64) % 3 == 2:
    password_base64 += '='
password = base64.b64decode(password_base64).decode('utf-8')

print('*' * 80)
# print(f'{address=}')
print(f'address: {address}')
print(f'port: {port}')
print(f'protocol: {protocol}')
print(f'method: {method}')
print(f'obfs: {obfs}')
print(f'password: {password}')

for param in base64_params.split('&'):
    key, base64_value = param.split('=')
    # print(base64_value)
    base64_value = base64_value.replace('-', '+').replace('_', '/')
    # print(base64_value)
    # if len(base64_value) % 3 == 1:
    #     base64_value += '=='
    # elif len(base64_value) % 3 == 2:
    #     base64_value += '='
    for i in range(3 - len(base64_value) % 3):
        base64_value += '='
    # print(f'{base64_value}')
    value = base64.b64decode(base64_value, ).decode('utf-8')
    print(f'{key}: {value}')
os.system("pause")