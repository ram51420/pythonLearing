
amt=0
eb=int(input("enter your reading"))
if eb<=100:
    amt=0
if eb>=100  and eb<=200:
    amt=(eb-100)*5
if eb>200:
    amt=500+(eb-200)*10
print("Amount pay", amt)
