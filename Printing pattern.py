
n = eval(input("Enter size:"))
ch = input("pattern")
pattern = int(input("Please choose  your print pattern(number):"))

if pattern == 1:
    for i in range(n):
        for j in range(n):
            print(ch, end ="")
        print()
elif pattern ==2:
    for i in range(n):
        for j in range(n-i):
            print(ch, end ="")
        print()

elif pattern ==3:
    for i in range(n):
      for j in range(i+1):
        print(ch, end ="")
      print()

elif pattern ==4:
    for i in range(n):
      for j in range(n-i-1):
        print(' ',end="")
      for k in range(i+1):
        print(ch, end="")
        print(' ',end="")
      print()
#calculate spaces n-i
elif pattern == 5:
    for i in range(n):
      for j in range(n-i-1):
        print(' ',end="")
      for k in range(i+1):
        print(ch, end="")
        print(' ',end="")
      print()
    for i in range(n):
      for j in range(i+1):
        print(' ',end="")
      for k in range(n-i-1):
        print(ch, end="")
        print(' ',end="")
      print()
