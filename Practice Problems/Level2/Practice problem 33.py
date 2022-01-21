
def integer_to_english(number):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety', 1000:'one thousand' }
    if number<=20:
        return d[number]
    elif number<=99:
        if number%10==0:
            return d[number]
        else:
            return(d[number//10*10]+" "+d[number%10])
    elif number<1000:
        if number%100==0:
            return d[number//100]+ " hundred"
        return(d[number//100]+' hundred and '+integer_to_english(number%100))
    elif number==1000:
        return d[number]
    else:
        return -1

number=789
print(integer_to_english(number))
