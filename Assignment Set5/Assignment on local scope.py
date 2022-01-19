#lex_auth_012693816779112448160

def calculate(distance,no_of_passengers):
    cost = (distance/10)*70
    earned = 80*no_of_passengers
    return (earned-cost) if earned>cost else -1
  
distance=20
no_of_passengers=1
print(calculate(distance,no_of_passengers))
