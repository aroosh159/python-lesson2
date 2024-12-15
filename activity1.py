name = "Aroosh"
age = 13
Student = True

print(type(name))
print(type(age))
print(type(Student))

print("\n After type casting.....")
age = str(age)
print(type(age))

#Operators
num1 = 42
num2 = 2

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
print(num1%num2)
print(num1**num2)

print(num1==num2)
print(num1<num2)
print(num1>num2)
print(num1!=num2)

result = 7+3/2*(2-4)//4-5%44
print(result)

#string operations

first_name = "Aroosh"
last_name = "Ali" 

print(first_name+last_name)
print("Ayesha"*4)

word = "Divisional" 

print("lenght of the word is :",len(word))
print("First letter of the word is :",word[0])
print("last letter of the word is :",word[9])
print("lSlicing of the word is :",word[0:5])

#Swapping

x = input("Enter the value of x:")
y = input("Enter the value of y:")

temp = x
x = y
y = temp 

print("\n AFter Swapping")
print(x)
print(y)
#finish