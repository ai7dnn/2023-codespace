s = 'Programming is an Art!'
print(s)

# 문자에 각각 5를 더하여 문자열을 출력
key = 5
for c in s:
    print(chr(ord(c) + key), end='')
print()

# 컴프리헨션 이해
print([i for i in range(10)])
print([chr(i) for i in range(ord('a'), ord('a') + 26)])

# 문자에 각각 5를 더한 문자 리스트를 출력
t = [chr(ord(c) + key) for c in s]
print(t)

# 문자열 str.join() 함수 이해
print(''.join('python'))
print(''.join(list('python')))
print('-'.join(list('python')))

# 문자에 각각 5를 더한 문자열 출력
e = '';
e = e.join([chr(ord(c) + key) for c in s])
print(e)

# 문자에 각각 5를 더한 문자열을 한 줄에 출력
print(''.join([chr(ord(c) + key) for c in s]))

e = '';
e = e.join([chr(ord(c) + key) for c in s])

# 비뀐 문자열을 다시 반대로 문자에 각각 5를 뺀 문자열을 한 줄에 출력
key = -key
print(''.join([chr(ord(c) + key) for c in e]))

