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
