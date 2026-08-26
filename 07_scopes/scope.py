username="Ayush Ghagre"

def func():
    username="Piyush Ghagre"
    print(username)

print(username)
func()

x=99

def func2(y):
    z=x+y
    return z

result=func2(100)
print(result)


def func3():
    global x
    x=12
# func3()
print(x)

# def f1():
#     x=88
#     def f2():
#         print(x)
#     f2()
# f1()

def f1():
    x=88
    def f2():
        print(x)
    return f2
myResult=f1()
myResult()

def outer(num):
    def actual(x):
        return x**num
    return actual


f1=outer(3)
print(f1(4))