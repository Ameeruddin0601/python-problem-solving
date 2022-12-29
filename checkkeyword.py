#check if given input word is a keyword of given language

keywords={"break","case","continue","default","defer","else","for","func","type","var"}

input_word = input()

if input_word in keywords:
    print(input_word,"is a keyword")
else:
    print(input_word,"is not a keyword")
