# %% 패키지 functools

# %% 모듈 functools 함수 reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)

# %%
print(reduce(lambda x, y: x + y, range(1, 3), 10))

# %%
from functools import reduce

fruits = ['apple', 'banana', 'pear', 'cherry']
combined = reduce(lambda x, y: x + ', ' + y, fruits)
print(combined)

# %%
fruits = ['apple', 'banana', 'pear', 'cherry']
print(', '.join(fruits))

# %%
from functools import reduce
 
# 리스트 항목
lst = [6, 1, 9, 3, 7]
 
# 리스트의 최대 수 출력
print(reduce(lambda a, b: a if a > b else b, lst))

# %%
from functools import reduce

# 장바구니에 담긴 상품들과 가격 정보
cart = [
    {'product': '사과', 'price': 500, 'quantity': 3},
    {'product': '바나나', 'price': 200, 'quantity': 5},
    {'product': '포도', 'price': 3000, 'quantity': 2},
    {'product': '귤', 'price': 100, 'quantity': 4},
    {'product': '메론', 'price': 4000, 'quantity': 2}
]

# 장바구니 상품들의 총액 계산 함수
def calculate_total_amount(acc, item):
    price = item['price']
    quantity = item['quantity']
    return acc + (price * quantity)

# reduce 함수를 사용하여 장바구니 총액 계산
total_amount = reduce(calculate_total_amount, cart, 0)

# 결과 출력
print(f"장바구니 총액: {total_amount}원")

# %% 모듈 functools 클래스 partial

# %%
# 인자 3 개를 출력하는 함수
def my_func(x, y, z):
    print(f'x:{x}, y:{y}, z:{z}')

# 모듈 functools에서 클래스 partial 가져오기   
from functools import partial

# 첫 번째 위치 인자를 1로 지정한 새로운 함수 pf1 생성 
pf1 = partial(my_func, 1)    
# 새로운 함수 pf1 호출 
pf1(2, 3) # x:1, y:2, z:3

# 첫 번째, 두 번째 위치 인자를 1과 2로 지정한 새로운 함수 pf2 생성 
pf2 = partial(my_func, 1, 2)    
pf2(3)   # x:1, y:2, z:3

# 첫 번째, 두 번째, 세 번째 위치 인자를 각각 1, 2, 3으로 지정한 새로운 함수 pf3 생성 
pf3 = partial(my_func, 1, 2, 3)    
pf3()    # x:1, y:2, z:3
#pf3(1)   # 오류발생

# %% 실습예제
from functools import partial

# 과일 가격
prices = {'apple': 1200, 'banana': 500, 'orange': 1500, 'grape': 3000}

# 세일 종류에 따라 선정된 총 과일 가격을 계산하는 함수
def calculate_total_price(coupon, *items):
    total_price = sum(prices[item] for item in items)
    discount = 0.0

    if coupon == '여름20프로세일':
        discount = 0.2
    elif coupon == '가을10프로세일':
        discount = 0.1

    discounted_price = total_price - (total_price * discount)
    return discounted_price

# partial을 사용하여 calculate_total_price 함수의 첫 번째 인수를 'SUMMER20'으로 고정한 새로운 함수 생성
summer_sale = partial(calculate_total_price, '여름20프로세일')
# partial을 사용하여 calculate_total_price 함수의 첫 번째 인수를 'FALL10'으로 고정한 새로운 함수 생성
fall_sale = partial(calculate_total_price, '가을10프로세일')

items = ['apple', 'banana', 'grape']

# summer_sale 함수를 호출하여 할인된 가격 계산
result = summer_sale(*items)
print(f"'여름20프로세일' 적용 총 가격: {result:.2f}원")

# 동일한 items에 대해 fall_sale 함수를 호출하여 할인된 가격 계산
result = fall_sale(*items)
print(f"'가을10프로세일' 적용 총 가격: {result:.2f}원")

# %%
from functools import partial

# pow(base: int, exp: int, mod: int) -> int
# square(x) == pow(x, 2) 
square = partial(pow, exp=2)

square(3) # pow(3, 2)
square(4) # pow(3, 2)

# cube(x) == pow(x, 3) 
cube = partial(pow, exp=3)

cube(5) # pow(5, 3)
cube(6) # pow(6, 3)

# %%
def func(a, b, c, d):
    print(f'a:{a}, b:{b}, c:{c}, d:{d}')
    return a * b - c % d

import functools
f1 = functools.partial(func, 10, d=3)       # a=10, b=?, c=??, d=3
print( f1(2, 20) )                          # a=10, b=2, c=20, d=3

f2 = functools.partial(func, 20, c=10, d=3) # a=20, b=?, c=10, d=3
print( f2(3) )                              # a=20, b=3, c=10, d=3

f3 = functools.partial(func, d=3)           # a=??, b=?, c=??, d=3
print( f3(10, 2, 20) )                      # a=10, b=2, c=20, d=3

f4 = functools.partial(func, d=4)           # a=??, b=?, c=??, d=4
print( f4(30, c=40, b=2) )                  # a=30, b=2, c=40, d=4
print( f4(30, c=40, b=2, d=3) )             # a=30, b=2, c=40, d=3
print( f4(30, 2, 40, 3) )                   # a=30, b=2, c=40, d=3

# %% 실습예제
from functools import partial

# 함수 process_info: 4개의 인자 
def process_info(name, age, city, occupation):
    return f"Name: {name}, Age: {age}, City: {city}, Occupation: {occupation}"

# functools.partial을 사용하여 process_info 함수의 occupation 인수를 고정한 새로운 함수 생성
student = partial(process_info, occupation='학생')
developer = partial(process_info, occupation='개발자')

# personal_info 함수를 호출할 때 위치 인자와 추가 키워드 인자를 함께 전달
p1 = student('김 지희', 21, city='서울')
print(p1)
p2 = developer('최 민혁', 26, city='부산')
print(p2)

# %% 예제
import functools

def process_order(menu_item, additional_request):
    return f"You ordered {menu_item} with {additional_request}."

# functools.partial을 사용하여 process_order 함수의 첫 번째 인수를 'Burger'로 고정한 새로운 함수 생성
order_burger = functools.partial(process_order, 'Burger')
menu_item = input("Enter the additional request for your burger: ")

result = order_burger(menu_item)
print(result)

# %%
from functools import partial

def foo(x, y, z):
    print(f'x:{x}, y:{y}, z:{z}')
    
foo1 = partial(foo, 1)    
foo2 = partial(foo, 1, 2)    
foo3 = partial(foo, 1, 2, 3)    

foo1(2,3) # x:1, y:2, z:3
foo2(3)   # x:1, y:2, z:3
foo3()    # x:1, y:2, z:3



# %% 연습문제
import functools

# 짝수를 판별하는 함수
def is_even(number):
    return number % 2 == 0

# 1 ~ 10 사이의 정수 리스트 
numbers = list(range(1, 11))

# functools.partial을 사용하여 is_even 함수를 호출하여 필터링하는 새로운 함수 생성
filter_even = functools.partial(filter, is_even)

result = list(filter_even(numbers))
print(result)  # 출력: [2, 4, 6, 8, 10]






# %%
import os

print(os.name)
print(os.getcwd())

# %%
import os 
     
print(os.getcwd()) 
# Changing the CWD 
os.chdir('../') 
print(os.getcwd()) 

# %%

    
# %%
import os 
  
# Directory 
directory = "py-code-test"
# Parent Directory path 
parent_dir = "D:/"
  
# Path 
path = os.path.join(parent_dir, directory) 
  
os.mkdir(path) 
print(f"폴더 생성: {directory}") 

# %%
import os 
  
# Get the list of all files and directories 
path = "D:/py-code"
dir_list = os.listdir(path) 
  
print(f"폴더: {path} 하부에 있는 파일과 폴더 {dir_list} ") 

# %%
import os

# 상대 경로
relative_path = 'py-fold/hello.py'
print("상대 경로:", relative_path)

# 상대 경로를 절대 경로로 변환
absolute_path = os.path.abspath(relative_path)
print("절대 경로:", absolute_path)

# 기본 이름 얻기
basename = os.path.basename(absolute_path)
print("기본 이름:", basename)

# 디렉토리 부분 얻기
dirname = os.path.dirname(absolute_path)
print("디렉토리:", dirname)

#print(os.path.exists(dirname))

# 경로의 존재 여부 확인
exists = os.path.exists(absolute_path)
print("경로의 존재 여부:", exists)

# 경로가 파일인지 확인
is_file = os.path.isfile(absolute_path)
print("파일 여부:", is_file)

# 경로가 디렉토리인지 확인
is_dir = os.path.isdir(absolute_path)
print("디렉토리 여부:", is_dir)

# 여러 경로 결합
path1 = './py-fold/'
path2 = 'hello.py'
combined_path = os.path.join(path1, path2)
print("결합된 경로:", combined_path)

# 경로를 디렉토리 부분과 기본 이름 부분으로 분리
dirname2, basename2 = os.path.split(combined_path)
print("분리된 디렉토리 부분:", dirname2)
print("분리된 기본 이름 부분:", basename2)

# 파일 경로를 기본 이름 부분과 확장자 부분으로 분리
filename, extension = os.path.splitext(combined_path)
print("분리된 확장자 부분:", extension)

# 파일 크기 얻기
file_size = os.path.getsize(combined_path)
print("파일 크기:", file_size, "바이트")

# %%
# Regular Expression 가져오기
import re

s = 'Hello, world! Hello Python! hello RE!' 

# match('pattern', 'string')
print(re.match('Hello', s)) # 문자열의 처음과 일치하지 않음
print(re.match('world!', s)) # 문자열의 처음과 일치하지 않음

print(re.search('world!', s)) # 문자열 전체에서 패턴 일치 첫 번째 찾기
print(re.search('python', s)) # 문자열 전체에서 패턴 일치 없음

# %%
# Regular Expression 가져오기
import re

s = 'Hello, world! Hello Python! hello RE!' 
m = re.match('Hello', s)
print(m)  # 문자열의 처음과 일치
print(m.group())  
print(m.span())  
print(m.start(), m.end())  

m = re.search('world!', s)
print(m) # 문자열 전체에서 패턴 일치 첫 번째 찾기
print(m.group())  
print(m.span())  
print(m.start(), m.end())  

# %%
import re

s = 'Hello, world! Hello Python! hello RE!' 
# match('pattern', 'string')
print(re.findall('Hello', s))  # 문자열의 처음과 일치
print(re.findall('world!', s)) # 문자열의 처음과 일치하지 않음

print(re.finditer('Hello', s)) # 문자열 전체에서 패턴 일치 첫 번째 찾기
for w in re.finditer('Hello', s):
    print(w, w.group())
print()

# %%
import re

s = 'int float string bool'
# string -> int 
result = re.sub('string', 'int', s)
print(result)

# %%
import re

s = 'hskang@gmail.com, bird@naver.com, river@dongyang.ac.kr'

# m = re.match(r'([a-z]+)@([a-z]+)\.com', s)
m = re.search('[a-z]+@[a-z]+[.]com', s)
print(m.group())

# result = re.sub(r'([a-z]+)@([a-z]+)\.com', 'new-address', s)
result = re.sub('[a-z]+@[a-z]+[.]com', 'anonymous-email-address', s)
print(result)

# %%
s = 'Hello, world! Hello Python! hello RE!' 
print(re.match('world', s))

s = 'Hello, world! Hello Python! hello RE!' 
print(re.search('world', s))

pattern = re.compile('Hello')
print(pattern.findall(s))
pattern = re.compile('world')
print(pattern.findall(s))


# %%
import re

s = '''A regular expression (or RE) specifies a set of strings that matches it.
      이 모듈의 함수를 사용하면 특정 문자열이 주어진 정규 표현식과 일치하는지 확인할 수 있습니다.'''

# []는 문자 집합을 나타내는데 a-z는 모든 영어 소문자만, +는 1번 이상 반복
pattern = re.compile('[a-z]+')
print(pattern.findall(s))

# []는 문자 집합을 나타내는데 A-Z는 모든 영어 대문자만, +는 1번 이상 반복
pattern = re.compile('[A-Z]+')
print(pattern.findall(s))

# 소문자, 대문자, 숫자, +는 1번 이상 반복
pattern = re.compile('[a-zA-Z0-1가-힣]+')
print(pattern.findall(s))

st = 'regular1234'
# 소문자, 대문자, 숫자, ?는 0번 또는 1번 이상 표시
pattern = re.compile('[a-zA-Z0-1]?')
print(pattern.findall(st))


# 소문자, 대문자, 숫자, *는 0번 또는 그 이상 표시
pattern = re.compile('[a-zA-Z0-1]*')
print(pattern.findall(string))
# 결과: ['The', '', 'Regular', '', 'Expresion', '', '', '', '', '', '1', '', '', '', '', '', '', '', '', '', '']


# 주민번호 뒷 번호를 *******로 치환
string = '090320-3212345'
# 기호 '-'와 0~9까지의 숫자 7개 반복의 패턴 정의
pattern = '-[0-9]{7}'
#  sub(정규표현식, 바꿀문자열, 입력문자열)
print ( re.sub(pattern, '-*******', string) )
# 결과: 090320-*******


#split 예제
pattern = re.compile(':')
print ( pattern.split('key:value') )
# 결과: ['key', 'value'] 


string = """Ross McFluff: 834.345.1254 155 Elm Street
Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way
Heather Albrecht: 548.326.4584 919 Park Place"""


entries = re.split("\n+", string)
print (entries)
# 결과: 개행 문자를 기준으로 분리한 문자열 4개의 list 
# ['Ross McFluff: 834.345.1254 155 Elm Street', 
# 'Ronald Heathmore: 892.345.3428 436 Finley Avenue', 
# 'Frank Burger: 925.541.7625 662 South Dogwood Way', 
# 'Heather Albrecht: 548.326.4584 919 Park Place']

# :와 ' ' 공백(space)을 패턴으로 4개의 list로 분리
result = [re.split(":? ", entry, maxsplit=4) for entry in entries]
print (result)
# 결과:  성, 이름, 전화번호, 우편번호, 거리명 list 저장됨
# [
#    ['Ross', 'McFluff', '834.345.1254', '155', 'Elm Street'], 
#    ['Ronald', 'Heathmore', '892.345.3428', '436', 'Finley Avenue'], 
#    ['Frank', 'Burger', '925.541.7625', '662', 'South Dogwood Way'], 
#    ['Heather', 'Albrecht', '548.326.4584', '919', 'Park Place']
# ]
