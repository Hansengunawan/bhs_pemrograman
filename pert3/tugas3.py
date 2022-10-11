#Operator Aritmatika pada Pemrograman Python

a="Hansen"
b="\n20210801355"
c="\nSample Operator in Pyhton"
d="\nOperator Aritmatika in Python"

print (a,b,c,d)

#Penjumlahan (+)
print("----------------")
print ("Penjumlahan (+)")
nilai1=int(input("nilai 1 = "))
nilai2=int(input("nilai 2 = "))
total=nilai1+nilai2
print("nilai penjumlahan", total)

#Pengurangan
print("Pengurangan (-) ")
total=nilai1-nilai2
print("nilai pengurangan", total)

#Perkalian
print("Perkalian (*) ")
total=nilai1*nilai2
print("nilai perkalian", total)

#Pembagian
print("Pembagian (/)")
total=nilai1/nilai2 
print("nilai pembagian", total)

#Modulus/nilai sisa
print("Modulus (%) ")
total=nilai1%nilai2
print("nilai modulus", total)

#exponentiation/pangkat
print("Exponentiation (**) ")
total=nilai1**nilai2
print("nilai exponentiation", total)

#floordivision/nilai terdekat
print("Floordivision (//) ")
total=nilai1//nilai2
print("nilai terdekat", total)


#Operator Penugasan pada Pemrograman Python
print("----------------")
print("Operator Penugasan in Python")

#Pengisian Nilai
print("Pengisian Nilai (=)")
x1=int(input("x1 = "))
print(x1)

#Pengisian dan Penambahan
print("Pengisian dan penambahan (+=) ")
x1 +=8
print(x1)

#Pengisian dan Pengurangan
print("Pengisian dan Pengurangan (-=)")
x1-= 2
print(x1)

#Pengisian dan Perkalian
print("Pengisian dan Perkalian (*=) ")
x1*= 2
print(x1)

#Pengisian dan Pembagian 
print("Pengisian dan Pembagian (/=) ")
x1/=2
print(x1)

#Pengisian dan Modulus
print("Pengisian dan Modulus (%=)")
x1%=3
print(x1)

#Pengisian dan FloorDivision
print("Pengisian dan FloorDivision (//=)")
x1//=2
print(x1)

#Pengisian dan Exponentiation
print("Pengisian dan Exponentiation (**=) ")
x1**=3
print(x1)

#Pengisian dan AND
# Note table
# x=1 y=1 x&y=1
# x=1 y=0 x&y=0
# x=0 y=1 x&y=0
# x=0 y=0 x&y=0 
print("Pengisian dan AND (&=)")
y=20
y&=12 
print(y)

#Pengisian dan OR
# Note table
# x=1 y=1 x|y=1
# x=1 y=0 x|y=1
# x=0 y=1 x|y=1
# x=0 y=0 x|y=0
print("Pengisian dan OR (|=)")
y|= 6
print(y)

#Pengisian dan XOR
# Note table
# x=1 y=1 x|y=0
# x=1 y=0 x|y=1
# x=0 y=1 x|y=1
# x=0 y=0 x|y=0
print("Pengisian dan XOR (^=)")
y^=4
print(y)

#Pengisian dan Right Shift
print("Pengisian dan Right Shift (>>=) ")
y>>=2
print(y)

#Pengisian dan Left Shift
print("Pengisian dan Left Shift (<<=)")
y<<=3
print(y)

print("----------------")

#Operator Perbandingan In Python
print("Operator Perbandingan In Python")

#Equal/Setara
print("Equal (==)")
y2 = 2
print (y==y2)

#Not Equal/Tidak Setara
print("Not Equal (!=)")
print (y!=y2)

#Greater than/Lebih besar dari
Nilai1=4
Nilai2=2

print("Greater than (>)")
print("Nilai 1 = ", Nilai1)
print("Nilai 2 = ", Nilai2)
print(Nilai1>Nilai2)

#Less than/Lebih kecil dari
print("Less than (<)")
print(Nilai1<Nilai2)

#Greater than or equal to
print("Greater than or equal to (<=)")
print(Nilai1>=Nilai2)

#Less than or equal to
print("Less than or equal to (<=)")
print(Nilai1<=Nilai2)

print("----------------")

#Operator Logika in Python
print("Operator Logika in python")

#and (returns true if both statements are true)
print("and (returns true if both statements are true)")
print(Nilai1>3 and Nilai1<5)

#or (returns true if one of the statements is true)
print("or (returns true if one of the statements is true)")
print(Nilai1>3 or Nilai2<5)

#not (reverse the result, returns False if the result is true)
print("not (reverse the result, returns False if the result is true)")
print(not (Nilai1>3 and Nilai2<5))

print("----------------")

#Operator Identitas in Python
print("Operator Identitas in Python")

#is Returns True if both variables are the same object
print("is (Returns True if both variables are the same object)")
k = ["ketoprak, gado-gado"]
l = ["ketoprak, gado-gado"]
j = k

print(k)
print(l)

print(k is j)
#returns True because j is the same object as k

print(k is l)
#returns False because k is not the same object as l, even if they have the same content

print(k==l)
#to demonstrate the difference betweeen "is" and "==": this comparison returns True because k is equal to ;

print("----------------")

#Operator Membership in Python
print("Operator Membership in Python")

#in Returns True if a sequence with the specified value is present in the object	
print("(in Returns True if a sequence with the specified value is present in the object)")

print("gado-gado," in k)
#returns True because a sequence with the value "gado-gado" is in the list

print("karedok" in k)
#returns False because a sequence with the value "karedok" not in the list

print("----------------")

#not in Returns True if a sequence with the specified value is not present in the object
print("not in (Returns True if a sequence with the specified value is not present in the object)")

print("karedok" not in k)
# returns True because a sequence with the value "karedok" is not in the list

