name="ayush Ghagre"

print(name)
print(name[0:6])
print(name[-1])

nums="0123456789"
print(nums[0:8:2]) 
# 0246 


#method
print(name.lower())
print(name.upper())
print(name.strip())
name.replace("Ayush","Piyush")
print(name)
print(name.split(" "))
print(name.find("y"))
print(name.count("a"))


chai_type="Masala"
quantity=2
order="I ordered {} cups of {} chai"
print(order.format(quantity,chai_type))

print(len(name))

chai="He said,\"Masala Chai is Awesome\""
print(chai)

st="hello\nworld"
print(st)
 
st2=r"hello\nworld"
print(st2)

# membership operator
print("hello" in st) 


# s.upper()        # Uppercase
# s.lower()        # Lowercase
# s.title()        # Title Case
# s.capitalize()   # First letter capital
# s.swapcase()     # Swap upper/lower case
# s.strip()        # Remove spaces from both ends
# s.lstrip()       # Remove left spaces
# s.rstrip()       # Remove right spaces
# s.replace(a,b)   # Replace substring
# s.split()        # String → List
# " ".join(lst)    # List → String
# names = ["Ayush", "Rahul", "Amit"]
# print(" ".join(names))
# s.find(x)        # First index (-1 if not found)
# s.index(x)       # First index (error if not found)
# s.count(x)       # Count occurrences
# s.startswith(x)  # Check prefix
# s.endswith(x)    # Check suffix
# s.isalpha()      # Only letters
# s.isdigit()      # Only digits
# s.isalnum()      # Letters and digits
# s.isspace()      # Only spaces
# s.center(10)     # Center align
# s.zfill(5)       # Pad with zeros
# s.partition(x)   # Split into 3 parts
# text = "apple-banana-orange"
# print(text.partition("-"))
# s.removeprefix(x)# Remove prefix
# s.removesuffix(x)# Remove suffix
# len(s)           # Length of string

