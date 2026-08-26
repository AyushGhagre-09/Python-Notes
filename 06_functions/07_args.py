def sum_all(*args):
    print(*args)
    print(args)
    return sum(args)

print(sum_all(1,2,3,4))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7))


#  *args-> unpacked tuple it is not itertable
#  args-> packed tuple it is itertable
#  *args->it is recommended to use same name as *args