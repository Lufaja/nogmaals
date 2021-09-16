score = 50
tot = 0
som = "50"
while tot < 1000:
    tot = tot + score
    print(str(som) + "=" + str(tot))
    score = score + 1
    som = str(som) + "+" + str(score)