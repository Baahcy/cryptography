import hashlib

print("!" * 60)
print("!!!!!!!      This is a md5 convertor       !!!!!!!!!!!")
print("!" * 60)

str = input('Enter your pass phase: ')

result = hashlib.md5(str.encode())

print('The md5 hash is : ',result.hexdigest())

