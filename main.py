nric = input('Enter an NRIC number: ')
  
# Type your code below
flag = 0
if nric[0] != "S" and nric[0] != "T" and nric[0] != "F" and nric[0] != "G":
  flag += 1
nric2 = nric[1:-1]
if nric2.isdigit() == False:
  flag += 1
elif len(nric2) != 7:
  flag += 1
if flag >= 1:
  print("NRIC is invalid.")
else:
  sum = 2*int(nric2[0]) + 7*int(nric2[1]) + 6*int(nric2[2]) + 5*int(nric2[3]) + 4*int(nric2[4]) + 3*int(nric2[5]) + 2*int(nric2[6])
  if nric[0] == "T" or nric[0] == "G":
    sum += 4
  checkdigit = sum%11
  if nric[0] == "S" or nric[0] == "T":
    ST = ["J","Z","I","H","G","F","E","D","C","B","A"]
    alpha = ST[checkdigit]
  else:
    FG = ["x","W","U","T","R","Q","P","N","M","L","K"]
    alpha = FG[checkdigit]
  if alpha == nric[8]:
    print("NRIC is valid.")
  else:
    print("NRIC is invalid.")