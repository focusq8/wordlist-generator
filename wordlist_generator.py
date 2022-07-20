import itertools
chrs = 'abcdefghijklmnopqstuvwxyz1234567890' 
number = int(input("number: "))
email = "@gmail.com"
for loop in itertools.product(chrs,repeat=number):  
   print(''.join(loop))
   #print(''.join(loop))+email
   with open('list_accounts.txt','a') as file:
      file.write(''.join(loop)+"\n")