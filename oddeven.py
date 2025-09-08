def even_odd_checker():
    print("Even or Odd Checker")
    number = int(input("Enter a number:"))

    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")

even_odd_checker()
