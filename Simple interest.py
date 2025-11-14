p=int(input("Enter the Principle Amount:"))
n=int(input("Enter the no of years:"))
SC=input("Senior Citizen y/n:")
G=input("M/F:")
if SC=="y" and G=="M":
    print("SI=",(p*n*12)/100)
elif SC=="y" and G=="F":
    print("SI=",(p*n*15)/100)
else:
    print("SI=",(p*n*10)/100)
