items = [
  { 'product': 'shirt', 'price': 100 },
  { 'product': 'pants', 'price': 300 },
  { 'product': 'pants 2', 'price': 200 }
]

prices = list(map(lambda item: item['price'], items))

print(prices)

def add_taxes(item):
  item['taxes'] = item['price'] * .19

  return item

new_items = list(map(add_taxes, items))

print(new_items)
print(items)