# %% class collections.Counter

# %%
'''
Dict subclass for counting hashable items. Sometimes called a bag
or multiset.  Elements are stored as dictionary keys and their counts
are stored as dictionary values.
'''

# count elements from a string
c = Counter('abcdeabcdabcaba')  
print(type(c))
print(c)                       # dict of counting
print(sorted(c))               # list all unique elements

print(c.most_common())         # three most common elements
print(c.most_common(3))         # three most common elements
print(c.values())         # total of all counts
print(sum(c.values()))         # total of all counts
print(c.total())
print(c.elements())
print(list(c.elements()))

''.join(sorted(c.elements()))   # list elements with repetitions

print(c['a'])
print(c['c'])

'''

    >>> c['a']                          # count of letter 'a'
    5
    >>> for elem in 'shazam':           # update counts from an iterable
    ...     c[elem] += 1                # by adding 1 to each element's count
    >>> c['a']                          # now there are seven 'a'
    7
    >>> del c['b']                      # remove all 'b'
    >>> c['b']                          # now there are zero 'b'
    0

    >>> d = Counter('simsalabim')       # make another counter
    >>> c.update(d)                     # add in the second counter
    >>> c['a']                          # now there are nine 'a'
    9

    >>> c.clear()                       # empty the counter
    >>> c
    Counter()

    Note:  If a count is set to zero or reduced to zero, it will remain
    in the counter until the entry is deleted or the counter is cleared:

    >>> c = Counter('aaabbc')
    >>> c['b'] -= 2                     # reduce the count of 'b' by two
    >>> c.most_common()                 # 'b' is still in, but its count is zero
    [('a', 3), ('c', 1), ('b', 0)]

'''

# %%
# 패키지 collectuons에 있는 다양한 
from collections import Counter 

# 조사와 공백 제거    
s = '간장 공장 공장장은 강 공장장이고 된장 공장 공장장은 공 공장장이다.'
lst = s.replace('은', '').replace('이고', '').replace('이다.', '').split()
print(lst)

# 단어의 출현 횟수를 클래스 Counter로 생성 
cnt = Counter(lst)
print(type(cnt), cnt)   

# 각각의 키에 대한 횟수 랭킹 출력
print(cnt.most_common(2))
print(cnt.most_common())
# 각각의 키에 전체 횟수 출력
print(cnt.total())

# 각각의 키에 대한 횟수 반환 출력
print(cnt['공장장'])
print(cnt['공장'])

# %%
from collections import Counter
c = Counter('mississippi')  
print(c)

# %% class collections.defaultdict

# %%
# collections.defaultdict 가져오기
from collections import defaultdict  

# 디폴트값이 int(값을 지정하지 않은 키에 대해서는 값이 0으로 지정)인 딕셔너리 
int_dict = defaultdict(int)          
print(int_dict)

print(int_dict['a'])
print(int_dict)

int_dict['a'] += 1 
int_dict['a'] += 1 
int_dict['b'] += 1 
print(int_dict)

# %% 본문
from collections import defaultdict    

# 디폴트값이 list(값을 지정하지 않은 키에 대해서는 값이 빈 리스트 []로 지정)인 딕셔너리 
lst_dict = defaultdict(list, pl=['java'])
print(lst_dict)

print(lst_dict['pl'])
print(lst_dict['env'])

lst_dict['pl'] += ['kotlin']
# lst_dict['pl'].append('python')
lst_dict['env'] += ['window']
lst_dict['env'] += ['linux']

print(lst_dict)
print(lst_dict['pl'])
print(lst_dict['env'])

# %%
from collections import defaultdict    

# 디폴트값이 lst(값을 지정하지 않은 키에 대해서는 값이 빈 리스트 []로 지정)인 딕셔너리 
lst_dict = defaultdict(list)
print(lst_dict)

print(lst_dict['a'])
print(lst_dict)

lst_dict['a'] += ['animal']
lst_dict['a'] += ['any']
lst_dict['b'] += ['banana']
print(lst_dict)

# %%
from collections import defaultdict

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

print(d)
print(d['i'])
print(d['m'])
sorted(d.values())
sorted(d.keys())
sorted(d.items())

# %%
from collections import Counter
s = 'mississippi'
cnt = Counter(s)
print(cnt)

# %%
words = ['강나루', '강가', '나비', '나침반', '파이썬', '파김치']

by_letter = {}
for word in words:
    if not word[0] in by_letter: # 현재 사전에 키가 없으면 
        by_letter[word[0]] = [word] # 처음으로 리스트로 대입
    else: # 이미 키가 한번 만들어진 경우
        by_letter[word[0]].append(word) # 리스트 마지막에 추가
    
dict(by_letter)

# %%
from collections import defaultdict

words = ['강나루', '강가', '나비', '나침반', '파이썬', '파김치']

by_letter = defaultdict(list)
for word in words: # defaultdict는 바로 다음 코드가 가능
    by_letter[word[0]].append(word)
    
print(by_letter)        # 전체 출력
print(by_letter['강'])  # 각각의 키로 출력
print(by_letter['나'])  # 각각의 키로 출력
print(by_letter['파'])  # 각각의 키로 출력

# %%
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('white', 4)]

d = defaultdict(set)
for k, v in s:
    d[k].add(v)

print(d)
print(d['red'])
print(d['blue'])
print(d['white'])

print(sorted(d.items()))
print(sorted(d.values()))
print(sorted(d.keys()))

# %%
from random import choices
# 1 ~ 20 사이의 정수 중에서 중복을 허학해 10개 선택
numbers = choices(range(1, 21), k=10)
print(numbers)

from collections import defaultdict
#numbers = [32, 4, 5, 7, 62, 38, 21, 62]
even_odd = defaultdict(set)

for num in numbers:
    if num % 2 == 0:
        # 키가 even인 set에 num 삽입
        even_odd['even'].add(num)
    else:
        # 키가 odd인 set에 num 삽입
        even_odd['odd'].add(num)

print(even_odd)
print(even_odd['even'])
print(even_odd['odd'])

# %% 연습문제
from collections import defaultdict

logs = [
    ('2023-06-30', 'user1', 'login'),
    ('2023-06-30', 'user2', 'login'),
    ('2023-07-01', 'user1', 'logout'),
    ('2023-07-01', 'user3', 'login'),
    ('2023-07-02', 'user2', 'logout')
]

user_count = defaultdict(int)

for log in logs:
    date, user, action = log
    if action == 'login':
        user_count[date] += 1
    else:
        user_count[date] -= 1

print(user_count)

# %% 연습문제
from collections import defaultdict

documents = [
    'I love apples.',
    'Apples are delicious.',
    'I have an apple tree.',
    'Do you like apples?'
]

word_locations = defaultdict(list)

for i, document in enumerate(documents):
    words = document.lower().split()
    for j, word in enumerate(words):
        word_locations[word].append((i, j))

search_word = 'apples'
print(word_locations[search_word])
print(word_locations)

# %% 연습문제
from collections import defaultdict

documents = [
    'I love apples.',
    'Apples are delicious.',
    'I have an apple tree.',
    'Do you like apples?'
]

word_locations = defaultdict(set)

# 문서의 인덱스와 단어의 위치를 저장
for i, document in enumerate(documents):
    words = document.lower().split()
    for j, word in enumerate(words):
        word_locations[word].add((i, j))

search_word = 'apples'

# 단어의 등장 위치와 문서 번호 출력
for location in word_locations[search_word]:
    document_index, word_index = location
    print(f"The word '{search_word}' appears in document {document_index} at index {word_index}.")

# %%
