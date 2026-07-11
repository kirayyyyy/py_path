password = input ("Enter password:")
count = 0
numbers = "1234567890"
vowel = "aeiou"
hasvowel = 0
hasnum = 0
for search in password:
    if hasvowel < 1:
        if search in vowel:
            hasvowel += 1
    if hasnum < 1:
        if search in numbers:
            hasnum += 1
if len(password) >= 8:
        count += 1
if hasvowel != 1:
    print ("- No vowel")
if hasnum != 1:
    print ("- No digit")
if count < 1:
    print("- Too shorts")
if hasvowel == 1 and hasnum == 1 and count == 1:
    print("Strong password!")