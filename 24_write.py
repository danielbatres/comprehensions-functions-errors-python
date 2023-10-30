with open('./text.txt', 'w+') as file:
  for line in file:
    print(line)
  

  file.write('\nnew items in this file\n')
  file.write('another line')
