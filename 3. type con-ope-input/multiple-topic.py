# int()
print("\nuse_input -> string -> use int() -> integer")
age = input("Enter your age: ")
age = int(age)
print(age+5)
print("\n Shortcut -> int(input()) -> integer")
age = int(input("Enter your age: "))
print(age+7)

#float()
print("\nuse_input -> string -> use float() -> decimal")
temp = input("Enter your temperature: ")
temp = float(temp)
print(temp)
print("\n Shortcut -> float(input()) -> decimal")
temp = float(input("Enter your temperature: "))
print(temp)

#str()
print("\n value -> string")
age1 = 25
age1_text = str(age1)
print(type(age1_text))

# Bool()
print("\n value -> boolean")
print(bool(1)) 
print(bool(0)) 
print(bool(""))
print(bool("Hello"))

# Operators
## 1. Arthmetic Operators
print("\n 1. Arthmetic Operators +,-,*,/,%,//,**")
print("Floor Division : ",5//2)
print("Power Multiplication : ",2**3)
## 2. Comparison Operators
print("\n 2. Comparison Operators ==,!=,>,<,>=,<= ")
print("Comparison is Equal then answer is True.")
print("Comparison is Not Equal then answer is False.")
## 3. Logical Operators
### And
print("\n 3. Logical Main/Important Operators and, or, not ")
print("\nAND :- Both conditions are True then answer is True.")
cpu = 70
memory = 60
print(cpu<80 and memory<80)
### OR
print("\nOR :- If any one condition is True then answer is True.")
cpu = 95
memory = 50
print(cpu>90 or memory>90)
### NOT
print("\nNOT :- It reverses the result. True <==> False")
status = True
print(not status)


# Assignment Operators
print("\n 4. Assignment Operators =,+=,-=,*=,/=,%=,**=,//=")
print("Normal Use")
count = 10
count = count+1
print(count)

print("\nShort Cut Use")
count = 10
count += 1
print(count)
count -= 1
print(count)
count *= 2
print(count)
count /= 2
print(count)
count %= 2
print(count)
count **= 2
print(count)
count //= 2
print(count)










