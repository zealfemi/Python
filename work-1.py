try:
  for i in [1, 2, 3]:
    print(i**2)

except:
  print("Please enter numbers")


x = 5
y = 1

try:
  z = x/y
  print(z)

except:
  print("numbers cannot be divided by 0")

finally:
  print("All done!")


def ask():
    while True:
        try:
            num = int(input("Input an integer: "))
            squared = num ** 2
        except:
            print("Enter an integer")
            continue
        else:
            print(f"Your number squared is: {squared}")
            break
               
ask()
