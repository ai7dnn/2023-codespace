# ==========================
# ====== 학습내용 점검 ======
# ==========================

# %% #1
print(''.join('java'))
print(''.join(list('java')))
print('*'.join('java'))
print('-'.join(list('java')))

# %% #2
s = 'ABCDE'
key = 1
print(''.join([chr(ord(c) + key) for c in s]))
key = 2
print(''.join([chr(ord(c) + key) for c in s]))
key = 3
print(''.join([chr(ord(c) + key) for c in s]))
key = 4
print(''.join([chr(ord(c) + key) for c in s]))

# %% #3
key = 1
print({i: (i + key) % 4 for i in range(10)})
key = 2
print({i: (i + key) % 4 for i in range(10)})
key = 3
print({i: (i + key) % 5 for i in range(10)})
key = 4
print({i: (i + key) % 5 for i in range(10)})

# %% #4
s = 'VWXYZ'
key = 2
d = {i: chr(ord('A') + (ord(i)-ord('A') + key) % 26) for i in s}
print(d.get('A', 'None')) 
print(d.get('V', 'None')) 
print(d.get('W', 'None')) 
print(d.get('X', 'None')) 
print(d.get('Y', 'None')) 
print(d.get('Z', 'None')) 

# %% #5 연산자 in
s = 'vscode pycharm jupyter'

# 연산자 in 사용 검색
print('code' in s)
print('py' in s)
print('jupy' in s)
print('vs py' in s)

# %% #6 메소드 find()
s = 'kaggle ananconda codespace colab'

print(s.find('kag'))
print(s.find('ana'))
print(s.find('gle')) 
print(s.index('ana'))
print(s.index('code')) 
print(s.index('codelab')) 

# %% #7
import re
m = re.search(r"\w+ \w+", "Isaac Newton, physicist")
print(m.group())       
print(m.groups())      
print(m.group(0))      
print(m.group(1))      

# %% #9
import re
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group())        
print(m.groups())       
print(m.group(0))      
print(m.group(1))      
print(m.group(2))      
print(m.group(1, 2))    

# ============================
# ====== 도전 프로그래밍 ======
# ============================

# %% CP#1
# 암호화된 원 문장을 4 줄만 복사
text = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg."""

#A python program to illustrate Caesar Cipher Technique
def encrypt(key, text):
    # 각각 대문자 코드 값 65, 소문자 코드 값 97 
    UCASE, LCASE = ord('A'), ord('a') 
    # 알파벳 갯수 26개
    CNT = ord('Z') - ord('A') + 1 
    
    result = ""
     # traverse text
    for char in text:         
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + key - UCASE) % CNT + UCASE)
        # Encrypt lowercase characters
        elif (char.islower()):
            result += chr((ord(char) + key - LCASE) % CNT + LCASE)
        else:
            result += char 
 
    return result
 
# 암호화된 문자열 복호화(복원)하는 키 값 13, 즉 'A' -> 'N'으로
key = 13
print("Shift : ", key)
print("암호문:")
print(text)
print()
print ("복호문:")
print(encrypt(key, text))

# %% CP#2
# -- 괄호 (단어)가 붙은 단어 찾기
import re

s = '() (책) (word) note ( regex )'
regex = r'\(\s*\w+\s*\)'

print('re.findall() 결과:')
print(re.findall(regex, s))
print('re.finditer() 결과:')
for m in re.finditer(regex, s):
    print(m)

# %% CP#3
# -- 숫자를 모두 *으로 대체
import re

txt = "전화번호 010-3017-9942 생년월일 150829"
print('원문:', txt)
stxt = re.sub(r'\d', "*", txt)
print('결과:', stxt)

# %% CP#4
# -- 점수만 추출문제 34.87 dd.ddd(.과 소수는 옵션)
import re

p = re.compile(r'[+-]?\d*[.]?\d*')
txt = "홍길동84.123 임걱정 +101.89 이현지 24.35 김미현 70 고현동-25.34"
flst = re.findall(p, txt)
flst = [n for n in flst if n]
print('원문:', txt)
print('결과:', flst)

# %% CP#5
# -- 위에서 추출한 점수의 판정, 부적격, PASS, FAIL
import re

p = re.compile(r'[+-]?\d*[.]?\d*')
txt = "홍길동84.123 임걱정 +101.89 이현지 24.35 김미현 70 고현동-25.34"
flst = re.findall(p, txt)
flst = [n for n in flst if n]
print('원문:', txt)
print('점수 추출:', flst)

result = {float(n): 'pass' if 100 >= float(n) >= 60 else 'invalid' if 100 < float(n) or float(n) < 0 else 'fail'
          for n in flst}
print('최종 판정:')
print(result)

# %% CP#6 
# -- 그룹없이 전화번호 검색
import re

def searchall(p, s):
    return [(m.group(), (m.start(), m.end())) for m in re.finditer(p, s)]

phone_number = 'kang +33 070-2345-7899 hwan +81 010 2345 7899 soo +1 23 863-1256'
#  (?:) Match expression but do not capture it.
iphone_regex = '(?:\+\d{1,4})?\s\d{2,3}[\s.-]\d{3,4}[\s.-]\d{4}'

print('검색된 모든 전화번호 목록:')
lst = searchall(iphone_regex, phone_number)
print(lst)

print()
match = re.search(iphone_regex, phone_number)
print('검색된 첫 객체:', match)
print('검색된 첫 전화번호: ', match.group())
# print(match.group(0)) # 오류
# print(match.group(1)) # 오류

# %% 
# CP#7 그룹 전화번로
# -- 그룹없이 전화번호 검색
import re

def searchall(p, s):
    return [(m.group(), (m.start(), m.end())) for m in re.finditer(p, s)]

phone_number = 'kang +33 070-2345-7899 hwan +81 010 2345 7899 soo +1 23 863-1256'
#  (?:) Match expression but do not capture it.
iphone_regex = '(\+\d{1,4})?\s(\d{2,3})[\s.-](\d{3,4})[\s.-](\d{4})'

print('검색된 모든 전화번호 목록:')
lst = searchall(iphone_regex, phone_number)
print(lst)

print()
p = re.compile(iphone_regex)
for m in re.finditer(p, phone_number):
    print('전화번호 전체: ', m.group())
    print('각 그룹의 튜플:', m.groups())
    print('그룹 별로 번호로 검색 출력:', m.group(1), m.group(2), m.group(3), m.group(4)) 
    print()

# %% CP#8 이름이 있는 전화번로
import re

def searchall(p, s):
    return [(m.group(), (m.start(), m.end())) for m in re.finditer(p, s)]

phone_number = 'kang +33 070-2345-7899 hwan +81 010 2345 7899 soo +1 23 863-1256'
#  (?:) Match expression but do not capture it.
iphone_regex = '(?P<code>\+\d{1,4})?\s(?P<area>\d{2,3})[\s.-](?P<pre>\d{3,4})[\s.-](?P<post>\d{4})'

print('검색된 모든 전화번호 목록:')
lst = searchall(iphone_regex, phone_number)
print(lst)

print()
p = re.compile(iphone_regex)
for m in re.finditer(p, phone_number):
    print('전화번호 전체: ', m.group())
    print('각 그룹의 튜플:', m.groups())
    print('그룹 별로 이름으로 검색 출력:', m.group('code'), m.group('area'), m.group('pre'), m.group('post')) 
    print()
 
# 종료 =======================
# %%
