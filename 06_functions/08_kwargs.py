def print_kwargs(**kwargs):
    # print(kwargs)
    for key,value in kwargs.items():
        print(f'{key}:{value}')
    print("------------------------------------------------")

# name arguments
print_kwargs(name="Ayush",age=24,place="nagpur")
print_kwargs(name="Ayush")
print_kwargs(name="Ayush",place="nagpur")