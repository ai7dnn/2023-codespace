# %%
a = list(range(-10, 11))
print(a)

f = filter(lambda x: x>0, a)
print(list(f))

# %%
class Person:
    def __init__(this):
        this.name = 'default name'
    def print(this):
        print(f'{this.name}')

p = Person()
p.print()
# %%
class Person:
    def __init__(me):
        me.name = 'default name'
    def print(me):
        print(f'{me.name}')

p = Person()
p.print()

# %%
print(globals())
# %%
