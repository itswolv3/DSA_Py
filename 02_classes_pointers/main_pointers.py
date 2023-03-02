num1 = 11
num2 = num1

print("Before num2 value is updated:")
print(f"num1 = {num1}")
print(f"num2 = {num2}")
print(f"num1 points to: {id(num1)}")
print(f"num2 points to: {id(num2)}")

num2 = 22

print("\n")

print("After num2 value is updated:")
print(f"num1 = {num1}")
print(f"num2 = {num2}")
print(f"num1 points to: {id(num1)}")
print(f"num2 points to: {id(num2)}")

print("\n")

dict1 = { "value": 11 }
dict2 = dict1

print("Before dict2 is updated:\n")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")
print(f"dict1 points to: {id(dict1)}")
print(f"dict2 points to: {id(dict2)}")

print("\n")

dict2["value"] = 22 
print("After dict2 is updated:\n")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")
print(f"dict1 points to: {id(dict1)}")
print(f"dict2 points to: {id(dict2)}")
