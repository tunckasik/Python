#Create an empty set
s = set()

# Add elements to set

s.add(7)
s.add(2)
s.add(3)
s.add(5)
s.add(1)
s.add(1)
#they are unique no duplication
print(s)

s.remove(3)
print(s)
print(f"We have {len(s)} of elements")