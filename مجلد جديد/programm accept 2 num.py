num1=eval(input("please enter first number: "))
num2=eval(input("please rnter second number: "))
process=input("enter the process(product ‘*’ or sum ‘+’ or subtract ‘-‘or division ’/’): ")
if process=="*":
    print("the product is: ",num1*num2)
elif process=="+":
    print("the sum is: ",num1+num2)
elif process=="-":
    print("the subtract is: ",num1-num2)
elif process=="/":
    print("the division is: ",num1/num2)
else:
    print("there is an error")