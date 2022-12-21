# define a function that converts the given number to the roman numerals
def roman_numbers(num):
    # set the dictionary for roman numerals
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman = ""
    i = 0
    while num > 0 :
        div = num //value[i]
        num = num % value[i]
        while div:
            roman = roman + symbol[i]
            div = div-1
        i =  i + 1
    return roman

# flag to show warning to the user, default is False.
is_invalid = False

# start endless loop to get user input continuously
while True:
    #info text to be shown to the user
    info = """
    ### --- Roman Numerals --- ###
    |                                               |
    |   Please enter a number between 1 and 3999    |
    |   to exit; type "exit"                        |

    Your number :"""

    # get the user input after showing info text.
    # if is_invalid set to True then show additional warning to the user
    # pass the input the alphaNum variable after stripping white space characters
    num = input("\n!! This is not valid !!\n"*is_invalid + info).strip()
    #if the input is not int number
    if not num.isdecimal():
        #Then check, if the input is the "exit"
        if num.lower() == "exit":
        # If it is 'exit', then terminate the the program
            print("\nExiting the program, Thank you and Byee!")
            break
        # if the input is else than "exit"
        else:
            is_invalid = True
            continue
    # convert the given string to the integer
    number = int(num)
    if 0 < number < 4000:

        print(
            "\nRoman numerals of ", number, " is :", roman_numbers(number))
        is_invalid = False
    else:
        is_invalid = True