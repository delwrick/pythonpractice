height = int(input('How tall is you? (in cm) '))
credits = int(input('How much money you got? '))

if height >= 137 and credits >= 10:
  print('Enjoy the ride!')
elif height < 137 and credits >= 10:
  print('Haha you are too short for this ride')
elif height >= 137 and credits < 10:
  print('Get your money up you do not have enough')
else:
  print('Dang u short and got no paper get outta here')