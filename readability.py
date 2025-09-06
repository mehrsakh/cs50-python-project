from cs50 import get_string
# import cs50

text = get_string("Text: ")

numOfLetters = 0
numOfWords = 1
numOfSentences = 0

for i in range(len(text)):
    if text[i].isalpha():
        numOfLetters += 1
    elif text[i].isspace():
        numOfWords += 1
    elif text[i] in ['.', '!', '?']:
        numOfSentences += 1


L = numOfLetters / numOfWords * 100
S = numOfSentences / numOfWords * 100

index = 0.0588 * L - 0.296 * S - 15.8
index = round(index)


if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
