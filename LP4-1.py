def main():
  copies = int(input("Enter # of copies to be printed: "))
  price = 0.0
  cost = 0.0

  if copies > 0 and copies <= 99:
    price = 0.0
  elif copies > 99 and copies <= 499:
    price = 0.28
  elif copies > 499 and copies <= 749:
    price = 0.27
  elif copies > 749 and copies <= 1000:
    price = 0.26
  elif copies > 1000:
    price = 0.25
  else:
    print("Invaild nuumber of copies.")

  cost = price * copies
  print("Price per copy is $" + str(price))
  print("Total cost is $" + str(round(cost, 2)))
  pass


if __name__ == "__main__":
  main()