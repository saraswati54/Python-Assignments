#Module2
#Assignment2
#1stANS
total = int(input('What is the total amount for your online shopping?'))
country = input('Shipping within the US or Canada?')
if country == "US":
    if  total < 50:
        print("Shipping Costs $6.00") 
    elif 50 <= total <= 100:
         print("Shipping Costs $9.00")
    elif 100<= total <= 150:
         print("Shipping Costs $12.00")
    else:
         print("FREE")
#if country == "Canada":
else :
    if  total < 50:
        print("Shipping Costs $6.00") 
    elif 50 <= total <= 100:
         print("Shipping Costs $9.00")
    elif 100<= total <= 150:
         print("Shipping Costs $12.00")
    else:
         print("FREE")         

#2ndANS

name = input("enter name ")
print("Welcome", name)   


#3rdANS
fahrenheit = float(input("Temperature value in degree fahrenheit: "))
celsius = (fahrenheit-32)/1.8

print(" The %.2f degree Fahreheit is equal to: %.2f Celsius" %(fahrenheit, celsius))
print(" Converted to Temperature: %.2f Celsius" %(celsius))

#4thANS
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <=40:
    print(h * r)
elif h > 40:
    print(40* r + (h-40)*1.5*r)    
 # h-40 is for substraction then you get how many time you work extra for an get extra pay 

#5thANS
a2 = [4,7,3,2,5,9]
b2 = enumerate(a2)
for i in b2:
    print(i)


#7thANS

dict1 = {'a':1 , 'b':2}
#dict2 = (map(reversed, dict1.items()))
dict2 = {v: k for k,v in dict1.items()}
print(dict2)

#8thANS
a3 = ['a','b','c','d']
b3 = enumerate(a3)
print(b3)
d3 = dict((i,j) for i,j in b3)
#d3= {tuple(key): idx for  idx, key in enumerate(a3)}
print(d3)

#9thANS

score = float(input("Enter score: "))

if 0.0 > score > 1.0:
    print("Score is out of range") 
elif score >= 0.9:
    print("Grade A")
elif 0.9 > score >= 0.8:
    print("Grade B")
elif  0.8 > score >= 0.7:
    print("Grade C")
elif 0.7 > score >= 0.6:
    print("Grade D")
else: 
    print("F")