num=29

is_prime=True

if num>1:
    for i in range(2,num):
        if(num%2)==0:
            is_prime=False
            break


if(is_prime):
    print(num,"is Prime")
else:
    print(num,"is not Prime")
