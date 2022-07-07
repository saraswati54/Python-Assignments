#Module4 Assignment
#ANS1
import re
x = '123-45-6789'
#y = re.findall('^\d{3}-\d{2}-\d{4}$',x)
##y = re.findall("^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$",x)
y = re.findall("^\d{3}-?\d{2}-?\d{4}$",x)
print(y)


#ANS2
import re

Date = 2020|2|2

dmatch = re.fullmatch(r'^("^\d{3}-?\d{2}-?\d{4}$)', Date)
#dmatch = re.findall(r'^(\d{4}(0[1-9]|1[0-2])|(0[1-9]|[12][0-9]|3[01])$)', Date)
print(dmatch)

#ANS3
import re

email = "sammy@gmail.com"
#y = re.findall(r'([\w.-]+)@gmail.com',email)
y = re.findall( '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email)
print(y)

#ANS4
import re
ip="25.255.45.67"    

op=re.match('(\d+).(\d+).(\d+).(\d+)',ip)

if ((int(op.group(1))<=255) and (int(op.group(2))<=255) and int(op.group(3))<=255) and (int(op.group(4))<=255):

    print("valid ip")

else:

    print("Not valid")

#ANS5
    
x1=int(input("enter x1 : "))

x2=int(input("enter x2 : "))

y1=int(input("enter y1 : "))

y2=int(input("enter y2 : "))

result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)