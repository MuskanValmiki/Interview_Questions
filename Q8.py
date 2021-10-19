row = 1
col = 1
while row <= 5:
    while col <= 17 :
      if (col == 2) or ((row  != 5) and (col == 11 or col == 15)) or ((row == 1 or row == 5) and (col < 4)) or (row == 1 and (col ==6 or col == 8)) or (row == 2 and (col == 5 or col == 7 or col == 9)) or (row == 3 and (col == 5 or col == 9)) or (row == 4 and (col == 6 or col == 8)) or (row == 5 and (col == 7)) or (row == 5 and (col > 11 and col < 15)):
      	print ("*",sep =" ", end = " ")
      else:
      	print (" ", end = " ")
      col += 1
    col = 1
    row += 1
    print ()