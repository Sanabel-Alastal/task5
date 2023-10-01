
# Q1)..
name = input("What's your name? ")
age = input("How old are you? ")
street = input("What's your street? ")
city = input("What's your city? ")
country = input("What's your country? ")
print("1)"+"*"*100)

# Q2)..
print("\"Name :"+name+"\"")
print("\"Age :"+age+"\"")
print("\"Address :"+street+" ,"+city+" ,"+country+" ."+"\"")
print("2)"+"*"*100)

# Q3)..
print("\""+"Hello {"+name+"} Your age is " + age+ " Years Old, Your Address is "+ street +" ,"+city+" ,"+country+" ."+"\""
)
print("3)"+"*"*100)

# Q4)..
print(type(name))
print(type(age))
print(type(street))
print(type(city))
print(type(country))
print("4)"+"*"*100)

# Q5)..
print("\""+"Hello \'"+name+"\' , How Are You? \ \"\"\" Your Age Is " + "\""+age+"\""+"\""+" + And Your Country Is: "+country
)
print("5)"+"*"*100)

# Q6)..
print("\""+"Hello "+name+", How Are You? \ \n \"\"\" Your Age Is "+ "\""+age+"\""+"\""+" + And \n Your city Is: "+city
)
print("6)"+"*"*100)

# Q7)..
namee = 'ITF Gsg Python'
print("First Letter Is \""+namee[0]+"\"")
print("Third Letter Is \""+ namee[2]+"\"")
print("Last Letter Is \""+ namee[-1]+"\"")
print("7)"+"*"*100)

# Q8)..
print(namee[-3::])
print(namee[0:3])
print(namee[0:7:2])
print(namee[-1:-7:-1])
print("8)"+"*"*100)

# Q9)..
naame = "$&$&Mohammed$&$&"
print(naame.strip("$&$&"))
print("9)"+"*"*100)

# Q10)..
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7","Love"))
print("10)"+"*"*100)

# Q11)..
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print("11)"+"*"*100)

# Q12)..
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))
print("12)"+"*"*100)

# Q13)..
first_name = "soso"
s = "***********"
print(first_name.ljust(15,"*"))
print('%s%s%s'%(s,first_name,s))
print(first_name.rjust(15,"*"))
print("13)"+"*"*100)


# # Q14) What is the difference between (title) and (capitalize) methods in Python string methods
# title() >> function make the first letter in each word uppercase and all letters after the first letter are make lower case
mas= "i love GSG and python langauge"
print(mas.title())
# The capitalize() >> function returns a string with the first character in the capital.
print(mas.capitalize())
print("14)"+"*"*100)

# Q15)..
name_one = "SaMER"
name_two = "Abed"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())
print("15)"+"*"*100)

# Q16) How can we Check if name_one contains Only Upper Case letters, and name_two contains Only Lower Case letters?
print(name_one.isupper())
print(name_two.islower())
print("16)"+"*"*100)

# Q17) How can we Check if name_one starts with (S) letters or Not ? and name_two ends with (HD) letters or Not?
print(name_one[0] == "S")
print(name_two[-2:] == "HD")
print("17)"+"*"*100)

# # Q18)..
msgg = "I Love Python And Although I Love GSG with Zakaria"
ss = str(msgg.count("Love"))
sss = str(msgg.count("t"))
print("Number of <Love> is: " + ss)
print("Number of <t> is: " + sss)
print("18)"+"*"*100)

# Q19)..
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7","love",1))
print("19)"+"*"*100)

# Q20)..
test1="ZakZak"
finaltext=test1.replace(" ", "").replace(".", "").replace(",", "").lower()
snabel= (finaltext[::-1])
half = int(len(finaltext) / 2)
firstString = finaltext[:half]
secondStrtring = finaltext[half:]
if snabel == finaltext and firstString == secondStrtring :
    print (test1,"is a palindrome and " ,test1,"is a symmetrical")
elif snabel == finaltext and firstString != secondStrtring :
    print (test1,"is a palindrome but " ,test1,"is not a symmetrical")
elif snabel != finaltext and firstString == secondStrtring :
    print (test1,"is not a palindrome but ",test1,"is a symmetrical")
else :
    print (test1,"is a not palindrome and ",test1,"is not a symmetrical")

test2="zakaria"
finaltext=test2.replace(" ", "").replace(".", "").replace(",", "").lower()
snabel= (finaltext[::-1])
half = int(len(finaltext) / 2)
firstString = finaltext[:half]
secondStrtring = finaltext[half:]
if snabel == finaltext and firstString == secondStrtring :
    print (test2,"is a palindrome and " ,test2,"is a symmetrical")
elif snabel == finaltext and firstString != secondStrtring :
    print (test2,"is a palindrome but " ,test2,"is not a symmetrical")
elif snabel != finaltext and firstString == secondStrtring :
    print (test2,"is not a palindrome but ",test2,"is a symmetrical")
else :
    print (test2,"is a not palindrome and ",test2,"is not a symmetrical")

test3="A war at Tarawa."
finaltext=test3.replace(" ", "").replace(".", "").replace(",", "").lower()
snabel= (finaltext[::-1])
half = int(len(finaltext) / 2)
firstString = finaltext[:half]
secondStrtring = finaltext[half:]
if snabel == finaltext and firstString == secondStrtring :
    print (test3,"is a palindrome and " ,test3,"is a symmetrical")
elif snabel == finaltext and firstString != secondStrtring :
    print (test3,"is a palindrome but " ,test3,"is not a symmetrical")
elif snabel != finaltext and firstString == secondStrtring :
    print (test3,"is not a palindrome but ",test3,"is a symmetrical")
else :
    print (test3,"is a not palindrome and ",test3,"is not a symmetrical")

test4="madam"
finaltext=test4.replace(" ", "").replace(".", "").replace(",", "").lower()
snabel= (finaltext[::-1])
half = int(len(finaltext) / 2)
firstString = finaltext[:half]
secondStrtring = finaltext[half:]
if snabel == finaltext and firstString == secondStrtring :
    print (test4,"is a palindrome and " ,test4,"is a symmetrical")
elif snabel == finaltext and firstString != secondStrtring :
    print (test4,"is a palindrome but " ,test4,"is not a symmetrical")
elif snabel != finaltext and firstString == secondStrtring :
    print (test4,"is not a palindrome but ",test4,"is a symmetrical")
else :
    print (test4,"is a not palindrome and ",test4,"is not a symmetrical")