'''
import hello
v1=hello.add(10,20)
v2=hello.sub(10,20)
print(v1)
print(v2)
'''

'''
import hello as h
v1=h.add(10,20)
v2=h.sub(10,20)
print(v1)
print(v2)
'''
'''
from hello import add 
v1=add(10,20)
print(v1)
'''
from hello import add as a,sub as b
v1=a(10,20)
v2=b(30,10)
print(v1)
print(v2)
