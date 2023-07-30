# function2.py
# 전역변수와 지역변수
x = 1
def func(a: int):
    return a+x

# 호출
print(func(1))

def func2(a):
    x = 5
    return a+x

# 호출
print(func2(1))

# 기본값 지정
def times(a = 10, b = 20):
    return a * b

# 호출
print(times())
print(times(5))
print(times(5, 6))

# 키워드 인자
def connectURL(server: str, port: int|str) -> str :
    strURL = 'https://' + server + ':' + port
    return strURL

print( connectURL('credu.com', '80') )
print( connectURL(server='credu.com', port='80') )
print( connectURL(port='80', server='credu.com') )

