def combo(iter1, iter2):
  output = []
  for index, value in enumerate(iter1):
    output.append((value, iter2[index]))
  print(output)
  return output


combo([1, 2, 3], 'abc')