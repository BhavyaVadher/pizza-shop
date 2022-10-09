print("WECLCOME TO BHAVYA'S PIZZA STORE")
a = input("What size of pizza do you want to buy: 'S''M''L' :")

if a=='S':
    b = 15
    print(f"Prize of your pizza is ${b}")
elif a=='M':
    b = 20
    print(f"Prize of your pizza is ${b}")
elif a=='L':
    b = 25
    print(f"Prize of your pizza is ${b}")
    
p = input("Do you want pepperoni: 'Y''N' :")
if p =='Y':
    if a =='S':
        b += 2
    else:
        b += 3
        
c = input("Do you want extra cheeze: 'Y''N' :")
if c =='Y':
    b += 1

print(f"Your final bill is ${b}")
               