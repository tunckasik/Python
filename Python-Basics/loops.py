from decimal import Decimal
import decimal


for i in [0,1,2,3,4]:
    print(i)

#if we want to loop with a specific loop
print ("----------------")

for i in range(6):
    print(i)

# we can use 'for' for any kind of list
names = ["Ali", "Mesut", "Serkan"]
for name in names:
    print(name)

word = "TUNCKASIK"
for char in word:
    print(char)

x = 'abcd'
for num in range(5, 11):
  print(num)
    # 5 6 7 8 9 10

x = 'abcd'
for i in x:
    print(i.upper())
    # A B C D

x = 'abcd'
for i in range(len(x)):
    print(i)
    # 0 1 2 3

for num in range(0, 11):
	if num %2 != 0: print(num)
print(num)

print("------------")

# x = 2021
# for i in x:
#   print(i)

print(bin(20))
print(bin(5))

