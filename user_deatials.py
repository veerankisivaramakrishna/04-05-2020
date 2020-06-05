name = input("Enter Your Nmae:(FirstName-LatName):")
mobile = (input("Enter Your Phone No:"))
adress = input("Enter Your Adress:")
print("----------------- User Enter Detals----------------")
print("Your Enterd Values are")
print("User Full Name Is:",name)
print("User Moble No. is:",mobile)
print("User Adress Is:",adress)
print("------------------ THE END-----------------")

data = name.split("_")
#print("splted data:" data)
if len(data) < 2:
    print("Invalid Name: Enter your Full Name This Format : (Frst Nmae-LastNmae)")
if len(mobile)!=10:
          print("Inavalid Mobile Number")
else:
   mobile = int(mobile)
