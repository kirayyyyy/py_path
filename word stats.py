sentence = input("Enter a sentence: \n")
vowels = "aeuio"
numbers = "1234567890"
vowel = 0
num = 0
space = " "
spaces = 0
count = 0
for search in sentence:
    if search in vowels:
        vowel += 1
    if search in numbers:
        num += 1
    if search in space:
        spaces += 1
    count += 1
print ("Characters:",count)
print ("Vowels:",vowel)
print ("Digits:",num)
print ("Spaces:",spaces)