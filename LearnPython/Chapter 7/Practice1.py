def check(userInput):
    Vowels = "aeiouAEIOU"
    countvowels = 0
    countconsonents = 0
    for char in userInput:
        if char.isalpha():
            if char in Vowels:
                countvowels = countvowels + 1
            else:
                countconsonents = countconsonents + 1
    return countvowels, countconsonents


Vowels, consonents = check("Anillohar is a educated person")
print("Vowels is : ", Vowels)
print("Consonents is : ", consonents)
