try:
  print(0 / 0)
except ZeroDivisionError as error:
  print(error)

try:
  assert 1 != 1, 'one is not equal to one'
except AssertionError as error:
  print(error)

try:
  age = 10

  if age < 18:
    raise Exception('Minors are not allowed')
except Exception as error:
  print(error)

print('Hello')