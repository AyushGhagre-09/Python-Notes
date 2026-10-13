

def number(n):
    print(n)

if __name__=="__main__":
  print("hello world")
  number(5)

num1=10
num2=20


# __name__ is a built-in variable that identifies the current module.
# When a Python file is executed directly, __name__ = "__main__".
# When a Python file is imported, __name__ contains the module's name.
# if __name__ == "__main__": runs the code inside it only when the file is executed directly.
# It prevents that specific code block from running when the file is imported.
