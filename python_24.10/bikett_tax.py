bikeAmount=int(input("Enter Bike amount with out tax"))
tax=0
if bikeAmount>100000:
    tax=15/100*bikeAmount
if bikeAmount>50000 and bikeAmount<=100000:
    tax=10/100*bikeAmount
if bikeAmount<=50000:
    tax=5/100*bikeAmount
print("this you need to pay road tax",tax)
