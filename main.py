nric = input('Enter an NRIC number: ')
  
# Type your code below
valid = ["S","T","F","G"]
flag = 0
count = 0
for i in valid:
  if nric[0] == i:
    count += 1
if count == 0:
  flag += 1
nric2 = nric[1:-1]
if nric2.isnumeric() == False:
  flag += 1
elif len(nric2) != 7:
  flag += 1
if flag >= 1:
  print("NRIC is invalid.")
else:
  digit_weight = [2,7,6,5,4,3,2]
  sum = 0
  for i in range(7):
    sum += int(nric2[i])*digit_weight[i]
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