p=int(input("enter the principle amount : "))
t=int(input("enter time : "))
r=int(input("enter rate : "))
amount=p*(1+r/100)**t
ci=amount-p
print("The simple compound intrest is :",ci)
