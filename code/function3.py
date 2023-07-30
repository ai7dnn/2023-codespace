# function3.py

# 가변인자
def union(*ar):
    # 지역변수(리스트)
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호출
print( union("HAM", "SPAM") )
print( union("HAM", "SPAM", "EGG") )

# 람다 함수
g = lambda x, y: x * y
print( g(3, 4) )
print( g(5, 6) )
print( (lambda x: x*x)(3) )
print( globals() )

# 내장함수 필터
# 필터링 함수 정의
def getBiggerThan20(i):
    return i>20

lst = [10, 20, 30]
iterL = filter(None, lst)
iterL = filter(getBiggerThan20, lst)

for i in iterL:
    print(i)

# for i in iterL:
#     if i > 20:
#         print(i)

print('== 람다함수 ==')
iterL = filter(lambda x: x>20, lst)
for i in iterL:
    print(i)
