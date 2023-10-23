photo=input("Give your photo")
panCard=input("Do you have pan card")
adhaarCard=input("you have adhaar card")
if(photo):
    if(panCard):
        if(adhaarCard):
            res="your account was created"
        else:
            res="adhaar card missing"
    else:
        res="pan card missing"
else:
    res="photo missing"
if(res=="your account was created"):
    print("Welcome to our bank Your eligiable opening account")
else:
    print("sorry  we are not open your with this",res," document")
