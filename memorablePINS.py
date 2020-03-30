def digitToWord(a):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwyz'
    mod = a % 5
    div = a // 5
    temp1 = consonants[div]
    temp2 = vowels[mod]
    return temp1 + temp2


pin = int(input("Enter the PIN : "))
temp = pin
encrypt = []
while(temp != 0):
    a = temp % 100
    t = digitToWord(a)
    encrypt.append(t)
    temp = temp // 100

encrypt.reverse()
print(''.join(encrypt))
