#check karna hai ki jo input me word mila hai, kya wo
#given language ka keyword hai? agar hai to output do ki haa
#wo keyword hai, nai to nai

keywords={"break","case","continue","default","defer","else","for","func","type","var"}

input_word = input()

if input_word in keywords:
    print(input_word,"is a keyword")
else:
    print(input_word,"is not a keyword")
