# %% 연산자 in
s = 'python kotrin'

# 연산자 in 사용 검색
print('py' in s)
print('kot' in s)
print('onkot' in s)

# %% 메소드 find()
s = 'python kotrin'

# 일반 문자열 메소드를 통한 검색
print(s.find('py'))
print(s.find('kot'))
print(s.find('onkot')) # 찾는 문자열이 없으면 -1

# %% 메소드 index()
s = 'python kotrin'
print(s.index('rin'))
print(s.index('java')) # 오류 발생

# %% 모듈 re
import re             # re.serarch() 사용
from re import search # serarch() 바로 사용

# %% function search
import re

m = re.search('thon', 'python kotlin')
print(type(m)) # re.Match 유형
print(m) # re.Match 객체 내용 

# %% method group() span() start() end()
from re import search

s = 'python kotrin'
m = search('thon', s)
print(m)
print(m.group()) # 실제 일치하는 문자열

# 일치하는 문자열의 위치 첨자
x, y = m.start(), m.end()
print(x, y, m.span())
print(s[x:y])

# %%
from re import search, findall

s = 'Copy file, move file1, rename file2 or remove file3'
p = 'file[12]?'
m = search(p, s)
print(m.group())
print(m.span(), m.start(), m.end())

fa = findall(p, s)
print(fa)

# %% 코딩 예제 09-07snum-regex.py
from re import search, findall

# 주민번호 데이터
data = """
        강 : 840234-1049118
        손 : 990312-1087254
        이 : 020602-2036115
        박 : 031216-3082966
       """

# 주민번호 추출 패턴
p = '\d{6}-\d{7}' # \d은 0~9 숫자 {n}은 n번 반복 

m = search(p, data)
print(m.group())

fa = findall(p, data)
print(fa)

# %% finditer
from re import findall, finditer

# 전체 검색 대상 문자열 
s = '...zoo,,.bar:%$baz 동물원' 
# 일반적인 _ 포함된 단어의 패턴
p = '\w+' # \w: word character, +: word character의 1회 이상 반복

lst = findall(p, s) # 일치하는 모든 단어 검색
print(lst)          # 일치하는 모든 단어 출력

it = finditer(p, s) # 일치하는 모든 단어의 이터레이터 검색
print(it)           # 일치하는 모든 단어의 이터레이터 출력

for i in finditer(p, s):
    print(i, i.group()) # 각각의 Match 객체의 출력

# %% 코딩 예제 09-08fruits-regex.py
import re

# 예제 문자열
text = "I have 3 apples, 2 bananas, and 4 oranges. What about you?"

# findall(): 패턴에 매칭되는 모든 결과를 리스트로 반환
numbers = re.findall('\d+', text)
print("숫자:", numbers)

# a | b | o 문자로 시작하고 단어 문자가 5회 이상 반복되는 단어 
fruits = re.findall('[abo]\w{5,}', text)
print("과일:", fruits)

# finditer(): 패턴에 매칭되는 모든 결과를 이터레이터로 반환
iterator = re.finditer('\d+', text)
print("숫자(finditer):")
for match in iterator:
    print(match, match.group())

# finditer()를 사용하여 숫자를 찾아내고 합산하기
total = 0
iterator = re.finditer('\d+', text)
for match in iterator:
    number = int(match.group())
    total += number
print("과일의 총 수량:", total)

# %% upgrade coding
import re

# 예제 문자열
text = "I have 3 apples, 2 bananas, and 4 oranges. What about you?"

# findall(): 패턴에 매칭되는 모든 결과를 리스트로 반환
numbers = re.findall('\d+', text)
print("수량 목록:", numbers)

print("수량 총합:", sum(map(lambda x: int(x), numbers)))

# %% match()
import re

# s = 'python kotlin' # 대상 문자열
s = 'kotlin python'
p = 'p\w+' # 검색할 정규식 패턴

# 함수 match()를 호출해 반환된 Match 객체를 변수 m에 저장한 후 if 처리
if m := re.match(p, s): # 반환된 Match 객체가 있다면
    print(f'처음부터 일치하는 패턴 {p} 이 {m.group()} 이네요')
else:                   # 반환된 Match 객체가 없다면
    print(f'처음부터 일치하는 패턴 {p} 이 없네요')

# %% match()
import re
s = 'kotlin python' # 검색 대상 문자열
p = 'k\w+ p\w+' # 검색할 정규식 패턴
# 함수 fullmatch()를 호출해 반환된 Match 객체를 변수 m에 저장
m = re.fullmatch(p, s) # 반환된 Match 객체가 있다면
print(f'전체 문자열이 일치하는 패턴 {p} 결과:')
print(m)

# %% findall()
import re

# 검색 대상 문자열
s = 'py1990 2000 python ja1995 java'
p = '[a-z]+\d+' # 정규 표현식 패턴
# 정규 표현식 패턴을 직접 사용해 추출 함수 호출
print(re.findall(p, s)) 

# %% re.compile()
# 검색 대상 문자열
txt1 = 'kot2011 kotlin swift sw2014'
txt2 = 'go go2009 typescrip ts2012'
pc = re.compile('[a-z]+\d+') # 정규 표현식 패턴을 컴파일
print(pc.pattern) # 정규 표현식 문자열 참조

# 컴파일된 패턴 객체를 사용해 추출 함수 호출
print(pc.findall(txt1))
print(pc.findall(txt2))

# 추출 함수의 첫번째 인자로 컴파일된 패턴 객체를 사용해 호출하는 방법
print(re.findall(pc, txt1))
print(re.findall(pc, txt2))

# %% 코딩 예제 09-09word4.py
import re 

# 검색 대상 문자열
text = "Hello, my name is John. I love Python programming!"

# 공백으로 구분된 4글자 단어를 찾는 정규식 패턴
pattern = re.compile(' \w{4} ')
# 텍스트에서 매치되는 단어들을 찾아 리스트로 반환
matches = pattern.findall(text)

# 결과는 실제 양쪽에 공백이 포함된 4글자 단어 출력
print("공백이 있는 4글자 단어들:", matches)
# 각 단어에서 공백을 제거한 결과 출력
print("공백이 없는 4글자 단어들:", end = ' ')
print(list(map(lambda s: str.strip(s), matches)))

# 정확히 4글자 단어를 찾는 정규식 패턴: 바로 다음에 학습 예정
pattern = re.compile(r'\b\w{4}\b')
# 텍스트에서 매치되는 단어들을 찾아 리스트로 반환
matches = pattern.findall(text)
print("정확히 4글자 단어들:", matches)

# %% 다음에 사용 =======================================

# findall()을 사용하여 특정 패턴과 매칭되는 모든 알파벳 문자열 찾아내기
word_letters = re.findall(r'\b[a-zA-Z]+\b', text)
print("단어들:", word_letters)

# %% raw string
s = 'python\n\tjava'
print(s)

s = r'python\n\tjava'
print(s)

# %% row string r'\b'
import re

# 대상 문자열
s = 'py, java.'

# 모든 단어의 경계 위치를 알기 위한 패턴 
p = r'\b' # 단어 경계

# 먼저 일치하는 모든 내용물 출력, 모두 공백문자 ''
print(re.findall(p, s))

# 모든 패턴을 조회해 반복
for match in re.finditer(p, s):
    print(match.span(), match.group()) # 각각의 위치와 공백문자 출력

# %% 단어 구분자 \b
from re import findall

# 대상 문자열
s = 'Matches the empty string, but only at the beginning or end of a word.'

# 모든 단어를 추출하기 위한 패턴 
p = r'\b\w+\b' # 단어 구분자 + 단어 + 단어구분자, 콤마 , 나 마침표 . 등 제거
print(findall(p, s)) # 모든 단어 추출해 출력

# %% 코딩 예제 09-10word.py 
import re

# 모든 패턴을 조회해 반복
def printAll(p, s):
    for match in re.finditer(p, s):
        print(match.span(), match.group()) # 각각의 위치와 공백문자 출력

# 예제 문자열
text = "나는 매일 아침 7시에 일어나서 커피를 마시고 출근합니다."

# 정규 표현식에 매칭되는 부분을 찾아내기
p = r'\b\w+\b'
matches = re.findall(p, text)
# 매칭된 결과 출력
print(matches)

printAll(p, text)

# %%
import re
print(re.split('h', 'python'))
print(re.split('th', 'python'))
print(re.split('n', 'python'))
print(re.split('p', 'python'))

# %%
import re
s = 'Word, word.'
pc = re.compile('\W+')

print(pc.split(s))      # 최대로 분할
print(pc.split(s, 1))   # 1회 분할
print(pc.split(s, 2))   # 2회 분할
print(pc.split(s, 3))   # 3회 분할

# %% 코딩 예제 09-11split.py
import re

# 인자 sentence에서 단어를 분리
def split_sentence_into_words(sentence):
    pc = re.compile(r'\W+')
    words = re.split(pc, sentence)
    return words

# 사용자로부터 문장 입력 받기
sentence = input("문장을 입력하세요: ")
# 사용자가 입력한 문장 출력
print(f'입력한 문장: {sentence}')

# 문장을 단어로 분리
word_list = split_sentence_into_words(sentence)

# 단어 출력
print('분할된 단어:')
for word in word_list:
    if word:
        print(word)

# %%
import re

s = 'abcde abcde abcde' # 대상 문자열
p = '\W'                # 검색 패턴
repl = '-'              # 대체 문자열

print(re.sub(p, repl, s))    # 모두 대체
print(re.sub(p, repl, s, 1)) # 1회 대체
print(re.sub(p, repl, s, 2)) # 2회 대체

p = '\d'                    # 검색 패턴
print(re.sub(p, repl, s))   # 없으면 원 문자열 반환

# %% 09-12subdomain.py
import re

def hide_domain(email):
    p = r'@\w+' # 정규식 패턴
    hidden_email = re.sub(p, '@*****', email)
    return hidden_email

# 사용자로부터 이메일 주소 입력 받기
email_address = 'hshong.py@gmail.com'
# 도메인 부분 가리기
hidden_email = hide_domain(email_address)

# 원 이메일 출력
print(email_address)
# 가려진 이메일 출력
print(hidden_email)

# %%
import re
print(re.findall('^r', 'rabbit raccoon parrot ferret'))
print(re.findall('^r', 'raccoon parrot ferret'))
print(re.findall('\Ar', 'rabbit raccoon parrot ferret'))
print(re.findall('\Ar', 'raccoon parrot ferret'))
     
print(re.findall('t$', 'rabbit'))
print(re.findall('t\Z', 'rabbit'))
print(re.findall('t$', 'trap'))
print(re.findall('t\Z', 'foot'))
print(re.findall('t$', 'foot'))
print(re.findall('t$', 'star'))

print(re.findall(r'\bfox\b', 'the red fox ran'))
print(re.findall(r'\bfox\b', 'the fox ate'))
print(re.findall(r'\bfox\b', 'foxtrot'))
print(re.findall(r'\bfox\b', 'foxskin scarf'))

# %%
import re

print(re.findall('c.e', 'clean cheap acert ecent'))
print(re.findall('\d', '6060-842 two 2b|^2b **___'))
print(re.findall('\D', 'The 5 cats 52 100'))
print(re.findall('\wee\w', 'trees bee4 The bee eels'))
print(re.findall('\Wbat\W', 'At bat wombat bat53'))
print(re.findall('\sfox\s', "the fox ate it's the fox foxfur"))
print(re.findall('\See\S', 'trees beef the bee stung The tall tree'))
print(re.findall('\^', 'ate. 2^3'))
print(re.findall('\.', 'ate. 2^3'))

# %%
import re

print(re.findall('gr[ea]y', 'gray green grey greek'))
print(re.findall('[a-e]', 'amber brand'))
print(re.findall('gr[^ea]y', 'grby grcy grey greek'))
print(re.findall('4[.^]\d', '4^3 4.2 44 23'))
print(re.findall('4[\^\.]\d', '4^3 4.2 44 23'))

# %%
import re
print(re.findall('ar*o', 'cacao arugula carrot artichoke'))
print(re.findall('re+', 'green trap tree ruined'))
print(re.findall('ro?a', 'roast root rant rear'))
print(re.findall('\we{2}\w', 'deer red seer enter'))
print(re.findall('2{3,}4', '6712-2224 224 2222224 123'))
print(re.findall('2{,3}4', '6712-24 2224 35 136'))
print(re.findall('12{1,3}3', '1234 15335 1222384 1222223'))

# %%
import re
# print(re.findall('((ab){2})', 'abab ababababab'))
print(re.findall('(ab){2}', 'abab ababababab'))
print(re.search('(ab){2}', 'abab ababababab'))
print(re.findall('(ab)+', 'abab ababababab'))
print(re.search('(ab)+', 'abab ababababab'))

# %%
import re
def searchall(p, s):
    fi = re.finditer(p, s)
    lst = [(m.group(), (m.start(), m.end())) for m in fi]
    return lst
                     
print(searchall('(ab){2}', 'abab ababababab'))

print(searchall('(ab)+', 'abab ababababab'))

# %% greedy or lazy
import re
print(re.findall('ab', 'a ab abb'))
print(re.findall('ab?', 'a ab abb'))
print(re.findall('ab*', 'a ab abb'))
print(re.findall('ab+', 'a ab abb'))

# %% lazy 최대한 짧게 
import re
print(re.findall('ab??', 'a ab abb'))
print(re.findall('ab*?', 'a ab abb'))
print(re.findall('ab+?', 'a ab abb'))

# %%
import re
print(re.findall('a{2,4}', 'aaaaa'))
print(re.findall('a{2,4}?', 'aaaaa'))

# %%
import re

def searchall(p, s):
    fi = re.finditer(p, s)
    lst = [(m.group(), (m.start(), m.end())) for m in fi]
    return lst

print(searchall('(bar)', 'foo bar baz'))
print(searchall('bar', 'foo bar baz'))

# %%
import re
print(re.search('(bar)+', 'foo bar baz'))
print(re.search('(bar)+', 'foo barbar baz'))
print(re.search('(bar)+', 'foo barbarbarbar baz'))

# %%
import re
print(re.findall('bar+', 'foo bar baz'))
print(re.findall('bar+', 'foo barbar baz'))
print(re.findall('bar+', 'foo barbarbarbar barrrr baz'))

# %%
import re
print(re.search('(ba[rz]){2,4}(qux)?', 'bazbarbazqux'))
print(re.search('(ba[rz]){2,4}(qux)?', 'barbar'))


# %% group
import re
m = re.search('(\w+),(\w+),(\w+)', 'foo,quux,baz')
print(f'groups(): {m.groups()}')
print(f'group(): {m.group()}')

print(f'group(0): {m.group(0)}')
print(f'group(1): {m.group(1)}')
print(f'group(2): {m.group(2)}')
print(f'group(3): {m.group(3)}')
#print(f'group(3): {m.group(4)}')

print(m.group(2, 3))
print(m.group(3, 2, 1))
print(m.group(0, 2, 3, 1))
print((m.group(3), m.group(2), m.group(1)))

# %%
import re
regex = r'(\w+),\1'
m = re.search(regex, 'python,python')
print(m)
print(m.group())
print(m.groups())
print(m.group(1))

regex = r'(\w+),(\1)'
m = re.search(regex, 'python,python')
print(m.groups())
print(m.group(2))
      
import re
regex = r'(\w+),\1'
print(re.search(regex, 'kotlin,kotlin'))
print(re.search(regex, 'python,kotlin'))

# %%
import re
m = re.search('(?P<pl1>\w+),(?P<pl2>\w+),(?P<pl3>\w+)', 'python,java,kotlin')
print(m.groups())
print(m.group('pl1'))
print(m.group(1))
print(m.group('pl2'))
print(m.group(2))
print(m.group('pl3'))
print(m.group(3))

print(m.group(1, 2, 3))
print(m.group('pl1', 'pl2', 'pl3'))

# %% groupdic()
import re
m = re.search('(?P<pl1>\w+),(?P<pl2>\w+),(?P<pl3>\w+)', 'python,java,kotlin')
d = m.groupdict()
print(d)
print(d['pl1'], d['pl2'], d['pl3'])


# %%
import re
m = re.search(r'(?P<equal>\w{2}\d{2})==(?P=equal)', 'ab12==ab12')
print(m)
print(m.group('equal'))

# %%
m = re.search(r'(?P<equal>\w{2}\d{2})==(\1)', 'ab12==ab12')
print(m)
print(m.group('equal'), m.group(1), m.group(2))

# %%
m = re.search(r'(?P<equal>\w{2}\d{2})==(\1)', 'ab12==ab12')
print(m)
print(m.groupdict())

# %%
import re
m = re.search('(?P<pl1>\w+),(?:\w+),(\w+)', 'python,java,kotlin')
print(m.group())
print(m.groups())
print(m.group('pl1'))
print(m.group(1))
print(m.group(2))

print(m.group(1, 2))
print(m.group('pl1', 2))

# %% comments
import re
print(re.search('py(?# This is a comment) kot', 'foo py kot qux'))

# %% pipe |
import re
print(re.findall('bar|foo', 'foo bar baz'))
print(re.findall('foo|bar', 'foofoobar'))

# %%
import re

def searchall(p, s):
    return [(m.group(), (m.start(), m.end())) for m in re.finditer(p, s)]
print(searchall('(foo|bar)+', 'foofoobar'))

lfun = lambda p, s: [(m.group(), (m.start(), m.end())) for m in re.finditer(p, s)]
print(lfun('(foo|bar)+', 'foofoo bar'))

# %% 코딩 예제 09-13firstlastline.py
import re

text = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.'''

pFirst = re.compile(r'^.+')
# pFirst = re.compile(r'^[^\n]+')
print(pFirst.pattern)
pLast = re.compile(r'.+$')
# pLast = re.compile(r'[^\n]+$')
print(pLast.pattern)

print(f'첫 번째 줄: {pFirst.findall(text)}')
print(f'마지막 줄: {pLast.findall(text)}')

# %% flags = re.I
import re
print(re.findall('[ab]+', 'ababABAB'))
print(re.findall('[ab]+', 'ababABAB', re.I))
print(re.findall('[Ab]+', 'ababABAB', re.IGNORECASE))

# %% flags = re.S
import re
# 모든 문자를 의미하는 메타 문자 .에는 \n은 불포함되므로 None
print(re.search('py.kot', 'py\nkot')) 
# 모든 문자를 의미하는 메타 문자 .에 \n을 포함하는 옵션 re.DOTALL, re.S
print(re.search('py.kot', 'py\nkot', re.DOTALL))
print(re.search('py.kot', 'py\nkot', re.S))

# %% flags = re.M
import re
print(re.findall('^py', 'py\npy'))
print(re.findall('on$', 'python\npython'))
print(re.findall('\Apy', 'py\npy'))
print(re.findall('on\Z', 'python\npython'))

print(re.findall('^py', 'py\npy', re.M))
print(re.findall('on$', 'python\npython', re.MULTILINE))

print(re.findall('\Apy', 'py\npy', re.M))
print(re.findall('on\Z', 'python\npython', re.MULTILINE))

# %% flags = re.X
import re
print(re.findall('py kot', 'py kot'))
print(re.findall('\d{3} \w{3}', '123 swi'))

# 공백이 무시되므로 일치하는 것이 없음
print(re.search('py kot', 'py kot', re.X))
print(re.search('\d{3} \w{3}', '123 swi', re.VERBOSE))

print(re.search('\w{4} # 단어 문자 4개와 일치', 'java', re.X))
print(re.search('\w{4} # 단어 문자 4개와 일치', 'java # 단어 문자 4개와 일치'))

# %% 코딩 예제 09-14searchpnum.py
import re

# 주석이 있는 정규식 
regex = r'''^               # Start of string
            (\(\d{2,3}\))?  # Optional area code (032)
            \s*             # Optional whitespace
            \d{3,4}         # Three or four digit prefix
            [-\ ]           # Separator character, - or empty space 
            \d{4}           # Four-digit line number
            $               # Anchor at end of string
            '''

# 다음은 위 정규식과 일치
print(re.search(regex, '(02) 3017 8972', re.VERBOSE))
print(re.search(regex, '(032)260-3145', re.VERBOSE))
print(re.search(regex, '(001)2610-9918', re.X))
print(re.search(regex, '(018)  2670-1992', re.X))
# 다음은 정규식과 일치하지 않음
print(re.search(regex, '018-2670-1992', re.X))

# 다음으로도 가능
pattern = re.compile(regex, re.VERBOSE)
print(pattern.search('3017-8972')) #정상적인 방법

# 비정상적인 방법으로 pattern으로는 옵션 flags 지정이 불가능 
print(pattern.search('3017-8972', re.VERBOSE)) 

# %%
import re

# 대소문자 무시 (IGNORECASE)
pattern = re.compile('apple', re.IGNORECASE)
result = pattern.match('Apple')  # 대소문자를 무시하고 매치됨
print(result)  # <re.Match object; span=(0, 5), match='Apple'>

result = pattern.match('Apple', re.IGNORECASE)  # 대소문자를 무시하고 매치됨
print(result)  # <re.Match object; span=(0, 5), match='Apple'>

# %%
import re
print(re.findall('^py', 'PY\npy\npY', re.I | re.M))

# %%
import re
print(re.findall('bar', 'FOO\nBAR\nbaR', re.I))
print(re.findall('(?i)bar', 'FOO\nBAR\nbaR'))

# %%
import re
print(re.findall('^bar', 'FOO\nBAR\nbaR', re.I | re.M))
print(re.findall('(?im)^bar', 'FOO\nBAR\nbaR'))

# %% 코딩 예제 09-15findemail.py
import re

text = '''Dave dave@google.com
Steve steve@gmail.com
kang hs+-kang@gmail.com
robert Rob%rob@gmail.com
Ryan ryan@yahoo.com
'''
# 정규식 패턴 (?i): re.IGNORECASE
pattern = r'(?i)[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

# 대소문자 미구분 정규식 패턴 생성
# re.IGNORECASE makes the regex case-insensitive
# regex = re.compile(pattern, flags=re.IGNORECASE)
regex = re.compile(pattern)

# 패턴에 맞는 모든 항목 출력
print(regex.findall(text))

# %%
# 위까지 본문
# ============================================================================

# %%
# 학습내용 점검 
# ============================================================================

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

# %%
s = '''rabbit \nraccoon parrot ferret'''
print(re.findall('^r', s))
print(re.findall('^r', s, re.M))

# %%
s = 'Account Number - 12345, Amount - 586.32'
p = '[0-9]+'
repl = 'OOOO'

print('Original string')
print(string)

result = re.sub(p, repl, string)

print('After replacement')
print(result)

# %%
import re
result = re.sub('abc',  '',    input)           # Delete pattern abc
result = re.sub('abc',  'def', input)           # Replace pattern abc -> def
result = re.sub(r'\s+', ' ',   input)           # Eliminate duplicate whitespaces using wildcards
result = re.sub('abc(def)ghi', r'\1', input)    # Replace a string with a part of itself


# %%
import re

s = 'Hello, world! Hello Python! Hello RE!' 
print(re.findall('Hello', s))  
print(re.findall('world!', s)) 
''
# 일치하는 모든 문자열에 대한  전체에서 패턴 일치 첫 번째 찾기
print(re.finditer('Hello', s)) 
for w in re.finditer('Hello', s):
    print(w, w.group())
print()

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


# %%
from re import findall

# 대상 문자열
s = 'grby grcy'
# s = 'gray grey'

# 모든 단어를 추출하기 위한 패턴 
p = r'gr[^ea]y' # 단어 구분자 + 단어 + 단어구분자, 콤마 , 나 마침표 . 등 제거
print(findall(p, s)) # 모든 단어 추출해 출력

# %%
import re

p = re.compile(r'[bp]anana\b')
s = 'banana panana pananana ganana'
fa = p.findall(s)
print(fa)

# %%
