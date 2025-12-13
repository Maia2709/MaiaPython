#  davaleba 7 მომხმარებელს შეჰყავს წინადადება, ამოცანა: გამოიანგარიშე თითოეული სიტყვის სიგრძე და
# დააბრუნე dictionary
# მაგალითად: "Python is fun" → {"Python": 6, "is": 2, "fun": 3}

def words_length(sentence):
    return {word: len(word) for word in sentence.split()}
sentence = input("შეიყვანეთ წინადადება: ")
print(words_length(sentence))