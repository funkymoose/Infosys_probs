
def count_digits_letters(sentence):
    countd = 0
    countl = 0
    for j in sentence:
            if j.isdigit():
                countd += 1
            elif j.isalpha():
                countl += 1
    return [countl, countd]

sentence = "Infosys Mysore 570027"
print(count_digits_letters(sentence))

# or

def count_digits_letters(sentence):
    countd = 0
    countl = 0
    for j in sentence:
            countd += 1 if j.isdigit() else 0   
            countl += 1 if j.isalpha() else 0
    return [countl, countd]

sentence = "Infosys Mysore 570027"
print(count_digits_letters(sentence))
