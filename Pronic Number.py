def isPronic(num):
  check = 0
  a = num + 1
  for i in range(0,a):
    if i * (i + 1) == num:
      check = 1
      break
  if check == 1:
    return True
  else:
    return False
isPronic(20)
