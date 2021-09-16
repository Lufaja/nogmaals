# name of student: Lukas
# number of student: 99068059
# purpose of program: calculate change
# function of program: calculate change
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #Amount you have to pay
payed = int(float(input('Payed amount: ')) * 100) #Amouunt you payed
change = payed - toPay #Amount of change you need to get
overview = "Overview: "

if change > 0: #If there is change it will run the code belo
  coinValue = 500 #the highest coin value
  
  while change > 0 and coinValue > 0: #As long as there is still change left an the value is not 0
    nrCoins = change // coinValue #

    if nrCoins > 0: #if it's possible to give coins of the current value this code will run
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #Shows ammount of coins an value of coins
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #Ask how many coins of this value you give back
      change -= nrCoinsReturned * coinValue #updates how much is left of the total change
      overview = str(overview) + str(nrCoins) + ' coins of ' + str(coinValue) + ' cents. '
# comment on code below: Value of coins
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #when not all change is given back it will tell you here
  print('Change not returned: ', str(change) + ' cents')
else:
  print(overview)
  print('done')