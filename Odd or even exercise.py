print("Hello !\nIt's been a long day, right?\nLet me help you with your even and odd numbers.")
play = "Yes"
while play == "Yes":
    number = int(input("What number will you like to check? "))
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f'{number} is an odd number')
    play = input("Will you like to check another number?\nPlease answer: 'Yes' or 'No'")
    continue
print("Thank you for using me . Have a fruitful and a purposeful life")
