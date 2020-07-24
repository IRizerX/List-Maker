import random, string

text = string.ascii_letters + string.digits
length = int(input('Enter Word Length : '))
count = int(input('How Many Words : '))

with open('IRizerX.txt', 'a') as file:
    for x in range(count):
        word = ''.join(random.choice(text) for x in range(length))
        if x == range(count)[-1]:
            file.write(word)
        else:
            file.write(word + '\n')
    input('All Done!, Press Any Key To Exit!')
