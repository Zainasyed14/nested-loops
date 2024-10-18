first = int(input("Enter starting value : "))
second = int(input("Enter final value : "))
for i in range(first, second):
    num=i
    flag= True
    for k in range(2, num):
        if num%k ==0:
            flag=False
            break
    if flag==True:
         print(i)