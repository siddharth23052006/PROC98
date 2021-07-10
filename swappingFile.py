def swapFileData():
  file1 = 'sampleText1.txt'#input('Enter the name of the first file, the data of which you want to swap. ')
  file2 = 'sampleText2.txt'#input('Enter the name of the second file, the data of which you want to swap. ')

  with open(file1, 'r') as a:
    data_a = a.read()

  with open(file2, 'r') as b:
    data_b = b.read()
  
  
  with open(file1, 'w') as a:
    a.write(data_b)

  
  with open(file2, 'w') as b:
    b.write(data_a)
  
  print('File data has been swapped successfully!')

swapFileData()