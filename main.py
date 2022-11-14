try:
    value = int(input("Please input a value between 1 and 10: "))
except ValueError:
    print("The value you enter must be a number!!!")
else:
    if (1 < value < 10):
        print(f"The value you entered is : {value}")
    else:
        print("The value you entered was not in the correct range!!!")



