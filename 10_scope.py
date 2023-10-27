price = 100 # global

def increment():
  price = 200
  result = price + 10

  print(result)

  return result

print(price)

print(increment())