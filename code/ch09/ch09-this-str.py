# %% 문자열 선언과 출력
# 변환하고자 하는 문자열
s = 'Programming is an Art!'
print(s)

# 문자에 각각 1을 더하여 문자열을 출력
key = 1
for c in s:
    print(chr(ord(c) + key), end='')
print()

# %% 코딩 예제 09-01encodestr.py
# 변환하고자 하는 문자열
origin = 'Programming is an Art!'

# 위 문자열을 암호화해 문자열 생성
key = 2
encode = ''
for c in origin:
    encode += chr(ord(c) + key)

# 원 문자열과 암호화된 문자열 출력    
print(f'origin 문자열: {origin}')
print(f'encode 문자열: {encode}')

#%% 문자열 메소드 join()
# 문자열 str.join() 함수 이해
print(' '.join('python'))

# 리스트 함수를 문자열을 인자로 호출하면 각 문자를 항목으로 하는 리스트 생성
print(list('python'))
# 문자열이 각각의 항목 중간에 들어간 문자열 생성
print('*'.join(list('python')))
print('-'.join(list('python')))

# 문자열 객체를 빈문자열로 지정하면 인자인 문자 리스트가 그대로 문자열로 변환
print(''.join(list('python')))

origin = 'Programming is an Art!'
encode = ''.join(origin)
print(encode)

# %% 변환을 컴프리헨션으로
# 문자열 'python'의 각 문자를 key 값만큼 ASCII 코드 값으로 이동시킨 후,
# 해당 코드를 문자로 변환하여 리스트에 저장해 출력
key = 1
clst = [chr(ord(c) + key) for c in 'python']
print(clst)

# %% 코딩 예제 09-02encodecomp.py 리스트 컴프리헨션
# 원 문자열
origin = 'Programming is an Art!'

# 리스트 컴프리헨션으로 문자열 암호화 수행 
key = 1
ecdlst = [chr(ord(c) + key) for c in origin]
print(f'origin 리스트: {list(origin)}')
print(f'encode 리스트: {ecdlst}')

# 암호화된 문자 항목의 리스트를 문자열로 변환하기 위해 ''.join() 사용 
encode = ''.join(ecdlst)
print(f'origin 문자열: {origin}')
print(f'encode 문자열: {encode}')

# %% 키와 값의 딕셔너리
# #딕셔너리 이해
d = {}
for i in range(10):  # 알파벳 인코딩 딕셔너리 생성
    d[i] = str(i+1)
print('일반 반복과 사전으로 생성:')
print(d)

print('사전 컴프리헨션으로 생성:')
d = {i: str(i+1) for i in range(10)}
print(d)

# %% 알파벳 순환 이해 
key = 1
cnt = 5
d = {chr(65 + i): chr(65 + (i + key) % cnt) for i in range(cnt)}
print(d)

# %% 코딩 예제 09-03dict4encode.py
# 알파벳 인코딩 딕셔너리 생성
d = {}
# 알파벳 수 26 계산
cnt = ord('Z') - ord('A') + 1  
# 기준 알파벳 A의 코드 값 65
A = ord('A')

# A에서 Z까지 {A: A, B: B, ...} 사전 생성
for i in range(cnt):
    d[chr(A + i)] = chr(A + i)
print('일반 반복과 사전으로 생성:')
print(d)

# A에서 Z까지 {A: B, B: C, ..., Y: Z, Z: A} 사전 생성
print('사전 컴프리헨션으로 생성:')
# 암호화를 위한 문자 이동 횟수
key = 1
d = {chr(A + i): chr(A + (i + key) % cnt) for i in range(cnt)}
print(d)

# %% 알파벳 첫 문자의 코드 번호
A, a = 'A', 'a'
print(f'A: {ord(A)}')
print(f'a: {ord(a)}')

# %% 반복으로 알파벳 사전 생성
# 인코딩을 위한 키, 값의 딕셔너리 생성
key = 3
d = {} # 딕서니리 만들기
for c in (65, 97): # 알파벳 A(65)와 a(97)에서부터 각각 시작하여
    for i in range(26): # 알파벳 수 26개만큼 인코딩 딕셔너리 생성
        d[chr(c + i)] = chr(c + (i + key) % 26) # 알파벳 순환
print('일반 반복과 사전으로 생성:')
print(d)

# %% 코딩 예제 09-04encodedict.py
# 알파벳 매핑에 사용되는 사전을 컴프리헨션으로 생성
key = 3
d = {chr(c + i): chr(c + (i + key) % 26) for c in (65, 97) for i in range(26)} 
print('알파벳 매핑 사전:')
print(d)

# 암호화 대상 문자열 
origin = 'Programming is an Art!'
# 암호화 수행 
# d.get(c, c): 키 c가 있으면 값, 없으면(알파벳이 아니면) 값은 동일한 c
encode = "".join([d.get(c, c) for c in origin])

# 원래의 문자열 출력 
print(f'origin 문자열: {origin}')
# 변환된 인코딩 문자열을 출력
print(f'encode 문자열: {encode}')

# %% function 
# key를 사용해 알파벳 매핑에 사용되는 사전을 컴프리헨션으로 생성
def makedic(key):
    return {chr(i+c): chr((i + key) % 26 + c) for c in (65, 97) for i in range(26)} 

# 사전 d를 사용해 문자열 text를 암호화한 문자열 반환
def encryption(d, text):
    # d.get(c, c): 키 c가 있으면 값, 없으면(알파벳이 아니면) 값은 동일한 c
    return "".join([d.get(c, c) for c in text]) 

# 암호화 대상 문자열 
origin = 'Beautiful is better than ugly.'
# 암호화 사전 생성
key = 13
d = makedic(key)
# 암호화 
encode = encryption(d, origin)
print(encode)

# %% 코딩 예제 09-05encodedecode.py
# 알파벳 매핑에 사용되는 사전을 컴프리헨션으로 생성
def makedic(key):
    return {chr(i+c): chr((i + key) % 26 + c) for c in (65, 97) for i in range(26)} 

# 사전 d를 사용해 문자열 text를 암호화한 문자열 반환
def encryption(d, test):
    # d.get(c, c): 키 c가 있으면 값, 없으면(알파벳이 아니면) 값은 동일한 c
    return "".join([d.get(c, c) for c in test]) 

# 암호화 대상 문자열 
origin = 'Beautiful is better than ugly.'
# 암호화 사전 생성
key = 13
d = makedic(key)
# 암호화 
encode = encryption(d, origin)

# 원래의 문자열 출력 
print(f'origin 문자열:\t{origin}')
# 변환된 인코딩 문자열을 출력
print(f'encode 문자열:\t{encode}')

# 다시 인코딩된 문자열을 원래의 문자열로 다시 복원하기 위한 딕셔너리 생성
d = makedic(-key)
decode = encryption(d, encode)
# 다시 원래의 문자열로 복원 출력
print(f'decode 문자열:\t{decode}')

# %% 모듈 this.py
s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg."""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))

# %% 코딩 예제 09-06this4comp.py
# 암호화된 원 문장을 4 줄만 복사
s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg."""

# 암호화된 문자열 복호화(복원)하는 키 값 13, 즉 'A' -> 'N'으로
key = 13 
# 각각 대문자 코드 값 65, 소문자 코드 값 97 
UCASE, LCASE = ord('A'), ord('a') 
# 알파벳 갯수 26개
CNT = ord('Z') - ord('A') + 1 

# 알파벳을 key 값인 13번째 후의 값으로 지정하는 사전 생성
# 가장 뒤의 Z이면 다시 A부터 순환하도록 계산: (i + key) % 26   
d = {chr(i+c): chr((i + key) % CNT + c)
               for c in (UCASE, LCASE) for i in range(CNT)} 
# print(f'암호화 사전 출력: {d}')

# d.get(c, c): 키 c가 있으면 값, 없으면(알파벳이 아니면) 값은 동일한 c
print("".join([d.get(c, c) for c in s]))

# %% 모듈 this.py
s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))

# %% 수업 연습
s = 'python'

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(c + i)] = chr(c + (i + 13) % 26)
        
print("".join([d.get(c, c) for c in s])) 


# %% 수업 연습
s = 'python'

d = {chr(i + c): chr(c + (13+i) % 26) for c in (65, 97) for i in range(26)}
print(''.join([d.get(c, c) for c in s]))
