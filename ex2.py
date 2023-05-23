arr = []
word = input('please enter a word')

while True:
    if word in arr:
        print('You entered the word '+word+' twice. Good bye…')
        break
    arr.append(word)
    word = input('please enter a word: ')