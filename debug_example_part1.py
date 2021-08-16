# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Python Basics 
# (Abschnitt 3)
# 
# - Collections
# - Conditions, Loops, Functions, List Comprehension
# - Lambda Expressions, Map&Filter, Methods

# %%
# help(list)


# %%
#pwd


# %%
float(4)/2


# %%
var1 = 2**3
print("var1 is {erg}.".format(erg=var1))
print("var1 really is {}".format(var1))


# %%
5%2

# %% [markdown]
# # Part 2 - Collections
# [Link1 - Doc](https://jpt-pynotes.readthedocs.io/en/latest/more-types.html)  
# [Link2 - Medium](https://medium.com/@paulrohan/python-list-vs-tuple-vs-dictionary-4a48655c7934)  
# [Link3 - geeksforgeeks](https://www.geeksforgeeks.org/difference-between-list-vs-set-vs-tuple-in-python/)  
# 
# - **Lists**  
#   - `[]`
#   - dynamic sized arrays  
#   - mutable, ordered sequence of items 
#   - can store any type of element
#   - other languages:  
#     - vector (C++) 
#     - ArrayList (Java)
#     
# - **Dictionaries**  
#   - `{}`
#   - associative array
#   - mutible
#     
# - **Tuples**  
#   - `()`
#   - immutable, ordered sequence (cannot be changed or replaced)
#   - can store any type of element
#   - not the extensive functionality that the list class provides
#   
# - **Sets**  
#   - immutable, unordered collection of items
#   - unique!
# 
# ### Python Types and Structures
# 
# - **Logical**: bool
# - **Numeric**: int, float, complex
# - **Sequence**: list, tuple, range
# - **Text Sequence**: str
# - **Binary Sequence**: bytes, bytearray, memoryview
# - **Map**: dict
# - **Set**: set, frozenset
# %% [markdown]
# ## Lists

# %%
# Lists
list1 = ['str', 13, 21, 47]
list1.append('b')
print(list1)
print(list1[3])
print(list1[:3])
print(list1[-1:])
list1[-1] = 'New'
print(list1)


# %%
# Lists 2
list2 = [1, 2, 3, [4, 5, ['Goal']]]
print(list2)
print(list2[-1][-1][0])

# %% [markdown]
# ### List Copy and reversion

# %%
list1 = ['str', 13, 21, 47]
print(list1)
list2 = list1
list2[2] = "new value"  # Only copies pointer to same list!
print(list1)
print()



list_copy = list1.copy()  # Creates separat copy of list.
list_copy2 = list1.copy()
print(list1.__repr__)
print(list2.__repr__)
print(f"list_copy == list_copy2: {list_copy == list_copy2:}")
print(f"list_copy is list_copy2: {list_copy is list_copy2:}")

print(f"Showing '__repr__' of a list: {list_copy.__repr__}")
print(f"Showing '__str__' of a list: {list_copy.__str__}/n/n")
print()



# Retrieving reversed iterator instead of reversing list!
list_reveresd_iter = reversed(list_copy)
print(list_reveresd_iter)
for val in list_reveresd_iter:
    print(val)
    
print(list_copy)



# Reversing whole list.
list_copy2.reverse()
print(list_copy2)

# %% [markdown]
# ## Dict

# %%
# Arrays
d = {'key1': {'innerKey': [1, 2, 3]}}
print(d['key1'])
print(d['key1']['innerKey'][1])


# %%
d2 = {}
print(type(d2))
d2["key1"] = "value1"
d2["key2"] = "value2"
print(d2)
print(d2["key1"])
for k, v in d2.items():
    print(f"{k} --> {v}")


# %%
class Person:
    race = "human"
    name: str
    age: int

d3 = {}
d3["Olli"] = Person()
d3["Leni"] = Person()


d3["Olli"].name = "Oliver Zott"
d3["Olli"].age = 37
d3["Olli"].race = "blub"


d3["Leni"].name = "Magdalena Bergmann"
d3["Leni"].age = 34

print(Person.race)


for k, v in d3.items():
    print(f"{k} --> {v.name}, {v.age}, race: {v.race}")
    
for k, v in d3.items():
    print(f"{k} -> {v}")

# %% [markdown]
# ## Tuple

# %%
t = (1, 2, 3)
print(t)
print(t[1])
# t[1] = 2  # no item assignement posible (immutable)

# %% [markdown]
# ## Set
# 

# %%
s = {7, 1, 2, 3, 1, 3, 2, 2, 5}
print(s)

# %% [markdown]
# # Part 3 - Conditions, Loops, Functions
# 
# - if-elif-else
# 
# - for
# 
# - while
# 
# - for-in / range  
#   - list from range

# %%
# if - elif - else
x, y = 7, 7
if x > y:
    print("x({}) is greater then y({})".format(x,y))
elif y > x :
    print("x({}) is lesse then y({})".format(x,y))
else:
    print("x({}) is equal to y({})".format(x,y))
        


# %%
# for 
sqe = [1, 2, 3, 4, 5]
for val in sqe:
    print(val)


# %%
# while
i = 1
while i < 5:
    print('i is {}'.format(i))
    i += 1


# %%
# for-in / range
for i in range(5):
    print(i)

print(range(5))

list(range(5))

# %% [markdown]
# ### List Comprehension

# %%
# Without list-comprehension

x = list(range(5))
y = []

for item in x:
    y.append(item**2)
print(y)


# %%
# with list-comprehension
z = list(range(5, 12))
z2 = [item**2 for item in z]

# %% [markdown]
# ### Functions
# 
# INFO: press `Shift + Tab` for Description !!

# %%
def func1 (param1: int = 11) -> None:
    """
    Description:
    Just some test-function
    """
    print('Square of {} is {}'.format(param1, param1**2))


# %%
print(func1())
print(func1(17))


# %%
# press `Shift + Tab`
func1

# %% [markdown]
# ## Part 4 - Lambda Expressions / Map & Filter / Methods
# %% [markdown]
# ### Lamda Expressions

# %%
# without lambda-expresion

def times2(var):
    return var*2

times2(7)


# %%
# with lambda expression

times3 = lambda var: var*3

times3(8)

# %% [markdown]
# ### Map & Filter

# %%
seq = range(1, 9)
seqList = list(seq)
print("List 'seq' is: {}'".format(seqList))
print(type(seq))
print(type(seqList))


# %%
resultMap = map(times3, seqList)
print(resultMap)
print(list(resultMap))


# %%
# Combine lambda & maps
resultLaMa = list(map(lambda var: var-3, seq))
print(resultLaMa)


# %%
# Filter
resultLaFi = filter(lambda item: item%2!=0, seq)
print(list(resultLaFi))

# %% [markdown]
# ### Standard Methods
# 
# - upper() / lower()
# - split
# - check existence
# - Iterate Lists

# %%
# str method

str1 = 'Hello, whats goin on here?'
print(str1.split('whats'))
print(str1.split()[1:4])


# %%
# dict methods

print(d)
print(d.keys())
print(d.items())

# use `Shift` to show usable methods 


# %%
# pop()

lst = [1, 2, 3, 'new']
print(lst.pop())
print(lst.pop(0))


# %%
# check existence
x in lst


# %%
# Iterate Lists

x = [(1, 2), (3, 4), (5, 6)]
for a, b in x:
    print(a)
    print(b)


# %%
word = 'string'
word[1]


# %%
a = [1,2,3]
b = map(lambda x: x+5, a)
list(b)


# %%



