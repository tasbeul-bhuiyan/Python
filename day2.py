x=str(1)
print(type(x))
y=int("10")
print(type(y))
print(y)
z=float(10.5)
print(type(z)) 
print(z)
#print="fdsaf"
#print(print) invalid because variable cant be keyword
a,b=5,10
print(a,b)
c=[1,2,3]
print(c)
print(type(c))
#c=d,e,f is invalid
d,e,f=c 
print(d)
print(e)
print(f)
g,h,i="I ","have ","a plan"
print(g+h+i)
j,k=5,6
print(j+k)
#print(j+g) invalid because int and str cant be added
print(str(j)+g)
print(j,g)
l="hello"
def myfunc():
    print(l+" world")
   # myfunc() repeates it more that 996 times leading to recursion error
myfunc()
m="hi"#a global variable
def myfunc1():
    m="hello00000"#a local variable
    print(m)
myfunc1()
print(m)
def myfunc2():
    global n#declaring n as global variable inside function
    n="hello global"
myfunc2()
print(n)
def myfunc3():
    global m#modifying global variable inside function
    m="hello modified global"
myfunc3()
print(m)
#exit() to end the code execution
#print("This will not be printed")
o=5
o=complex(o)
print(o)
x="welcome"
print(x[3:])
print("hey");print("there"); print("everyone")  #semicolon usage to use multiple statements in a single line
