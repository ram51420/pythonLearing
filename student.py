#student mark list

print("please enter  your name")
name=input()
print("Enter date of Birth")
date=int(input())
print("please enter Class teacher Name")
techername=input()
print("please your roll numer")
rolNo=int(input())
print("please enter tamil mark")
tamil=int(input())
print("please enter English mark")
english=int(input())
print("please enter maths mark")
maths=int(input())
print("please enter science mark")
sience=int(input())
print("please enter socialScience mark")
socialScience=int(input())

print("                                   Govt Higher secondary school")
print("                                     Avalurpet")
print("                                     Villupuram-604201")



print("Your is-      ",name)
print("Date Of Birth:",date)
print("Your Roll_No  ",rolNo)
print("Teacher Name  " ,techername)
print("Tamil mark                           ",tamil)
print("English mark                         ",english)
print("Mathsmark-                           ",maths)
print("sience mark-                         ",sience)
print("SocailSience mark-                   ",socialScience)
total=tamil+english+maths+sience+socialScience
print("                 Total mark is---",total,"    average--",total/5)

if tamil>40:
    print("Tamil      pass")
else:
    print("Tamil      Fail")

if english>40:
    print("english    pass")
else:
    print("english    Fail")

if maths>40:
    print("maths      pass")
else:
    print("maths      Fail")

if sience>40:
    print("sience      pass")
else:
    print("sience      Fail")

if socialScience>40:
    print("socialScie  pass")
else:
    print("socialSienc Fail")

if((tamil>40)and(english>40)and(maths>40)and(sience>40)and(socialScience>40)):
    print("                       congratulation your Pass")
else:
    print("                       Sorry Better Next Time Fail")

