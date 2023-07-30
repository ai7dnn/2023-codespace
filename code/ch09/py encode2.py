s = 'Programming is Art!'
print(s)

# 딕셔너리 이해
d = {}
for i in range(10):  # 알파벳 인코딩 딕셔너리 생성
    d[i] = str(i+1)
print(d)

d = {}
for i in range(ord('A'), ord('A') + 26):  # 알파벳 인코딩 딕셔너리 생성
    d[chr(i)] = chr(i)
print(d)

# 인코딩을 위한 키, 값의 딕셔너리 생성
key = 3
d = {} # 딕서니리 만들기
for c in (65, 97): # 알파벳 A, a에서 부터 시작하여
    for i in range(26): # 알파벳 인코딩 딕셔너리 생성
        d[chr(i+c)] = chr((i + key) % 26 + c)

print(d)

# 변환된 인코딩 문자열을 출력
# d.get(c, c): 키 c가 있으면 값, 없으면(알파벳이 아니면) 값은 동일한 c
print("".join([d.get(c, c) for c in s]))

# 인코딩 문자열을 e에 저장
e = '';
e = e.join([d.get(c, c) for c in s])
print(e)

# 다시 인코딩된 문자열을 원래의 문자열로 다시 변환하기 위한 딕셔너리 생성
key = -key
d = {} # 딕서니리 만들기
for c in (65, 97): # 알파벳 A, a에서 부터 시작하여
    for i in range(26): # 알파벳 인코딩 딕셔너리 생성
        d[chr(i+c)] = chr((i + key) % 26 + c)

# 변환된 인코딩 문자열을 출력
print("".join([d.get(c, c) for c in e]))