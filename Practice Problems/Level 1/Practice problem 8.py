
def calculate_net_amount(trans_list):
    net_amount = 0 
    for i in trans_list:
        x = i.split(':')
        if x[0]=='D':
            net_amount += int(x[1])
        else:
            net_amount-= int(x[1])
    return net_amount

trans_list=["D:350","W:100","W:500","D:1000"]
print(calculate_net_amount(trans_list))
