# #seceret code
# #vikram -> gggmarkivhh
import random
import string

choose=int(input("enter 1 for coding and 0 for decoding:"))
if choose==1:
  code=input("enter the name which should be encoded:")
  words=code.split(" ")
  nlist=[]
  random_=random.choices(string.ascii_letters + string.digits,k=3)
  random__=random.choices(string.ascii_letters + string.digits,k=3)
  random="".join(random_)
  random1="".join(random__)
  for i in words: 
    if (len(i) >= 3):
      word= random +i[1:] + i[0]+ random1
    
      nlist.append(word)
    else:
      nlist.append(i[::-1])
      
  print(" ".join(nlist))
else:
  decode=input("enter the name which should be decoded:")
  words=decode.split(" ")
  nlist1=[]
  for i in words:
    if (len(i) >= 3):
      word=i[-4] + i[3:len(i)-4]
      nlist1.append(word)
    else:
      nlist1.append(i[::-1])

  print(" ".join(nlist1))
  print(decode[::-1])