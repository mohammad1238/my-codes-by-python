l=[]
decimal_num=int(input("enter the decimal number: "))
result=decimal_num
while result!=0:
    remind=result%2
    l.append(remind)
    result=result//2
l.reverse()
y=[]
for m in l:
    x=str(m)
    y.append(x)
binary_num="".join(y)
print(binary_num)