# Dealing with lists

states = ["California", "Texas", "Florida", "New York"]
popluation = [123456,3465,67776,78898]

dict_states = {"States": states,
               "Population":popluation}

print(states[0])
print(states[1])
print(states[2])
print(states[3])

print(states[-0])
print(states[-1])
print(states[-2])
print(states[-3])

print(states[::-1])


# For loops 

for state in states:
    if state == "Florida":
        print(state)


# Export data in python 
# First way
with open("test.txt","w") as file:
    file.write("Data Successfully Scrapped!")

# Second Way
import pandas as pd
df = pd.DataFrame.from_dict(dict_states)
print(df)
df.to_csv("test.csv",index=False)

# Handling Exception Errors 
new_list = [2,4,6, "California"]

for element in new_list:
    try:
        print(element/2)
    except:
        print("The element is not a number!")

# While-Break Statements
n = 4
while n>0:
    print(n)
    n = n-1
    if n == 2:
        break
print("Lood Ended!")











