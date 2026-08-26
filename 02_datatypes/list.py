tea_varities = ["Black", "Green", "Oolong", "White"]

print(tea_varities[0])
print(tea_varities[-1])
print(tea_varities[1:3])
print(tea_varities[::-1])
print(tea_varities[1:1])
print(tea_varities[:])  
print(tea_varities[::2])

# tea_varities[1:2]=["lemon"]
# tea_varities[1:3]=["green","masala"]
# tea_varities[1:3]=[]
# print(tea_varities)


for t in tea_varities:
    print(t,end=" ")
print("\n")
if "Oalang" in tea_varities:
    print("I have oolang tea")


tea_varities.append("lemon")
tea_varities.insert(0,"Normal")
print(tea_varities.pop())
print(tea_varities.remove("White"))
print(tea_varities.count("Oolong"))
 

tea_copy=tea_varities.copy()
tea_varities.clear()
print("-----------------------------------")
print(tea_varities)
print(tea_copy)


squared_nums=[x**2 for x in range(10)]
print(squared_nums)

# lst.append(x)      # Add element at end
# lst.extend(iter)   # Add multiple elements
# lst.insert(i, x)   # Insert at index
# lst.remove(x)      # Remove first occurrence of value
# lst.pop()          # Remove and return last element
# lst.pop(i)         # Remove and return element at index
# lst.clear()        # Remove all elements
# lst.index(x)       # Find index of first occurrence
# lst.count(x)       # Count occurrences
# lst.sort()         # Sort list in ascending order
# lst.sort(reverse=True) # Sort descending
# lst.reverse()      # Reverse list
# lst.copy()         # Shallow copy of list

# buildin function
# len(lst)           # Length of list
# max(lst)           # Largest element
# min(lst)           # Smallest element
# sum(lst)           # Sum of elements
# sorted(lst)        # Returns sorted list