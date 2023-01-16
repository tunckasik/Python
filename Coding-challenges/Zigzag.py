def zigzag(x):
    for i in range(x):
        if i % 2 == 0:
            print("* " * (x - i))
        else:
            print(" *" * (x - i))

    # At the last iteration the value of i = 5

    for j in range(x+1):
        if j % 2 == 0:
            print("+ " * (x - (x-j)))
        else:
            print(" +" * (x - (x-j)))
zigzag(6)

def savas(y):
    for i in range(y):
        print("Step ",i+1,":", end=" ") # added step number
        if i % 2 == 0:
            for j in range(y - i):
                print("+ ", end="") # added end="" to prevent new line
            print("") # added new line
        else:
            for j in range(y - i):
                print(" +", end="") # added end="" to prevent new line
            print("") # added new line
    # Reverse the step numbers and zigzag
    for a in range(y, 0, -1):
        print("Step ", a,":", end=" ") # added step number
        t = y - (y-a) # to ascend the value
        if a % 2 == 0:
            for k in range(t):
                print("* ", end="") # added end="" to prevent new line
            print("") # added new line
        else:
            for k in range(t):
                print(" *", end="") # added end="" to prevent new line
            print("") # added new line
savas(6)

# for i in range(10, 0, -1):
#     print(i)

# import math
# def zigzag_pattern(rows):
#     for i in range(1, rows + 1):
#         print("Step ",i,":", end=" ")
#         if i <= math.floor(rows/2):
#             print("a " * (rows - i + 1))
#         elif i == math.floor(rows/2) + 1:
#             print("* " * (rows - i + 1))
#         else:
#             for j in range(i - math.floor(rows/2) - 1):
#                 print("* ", end="")
#             for k in range(rows - i + 1):
#                 print("a ", end="")
#             print("")

# zigzag_pattern(5)