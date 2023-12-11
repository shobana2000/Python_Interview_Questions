user_input=input("Enter your Sentence: ")
# print(user_input)

def reverse_words(sentence):

    words=sentence.split()
    # print(val)
    reverse_sentence=' '.join(reversed(words))

    return reverse_sentence

val=reverse_words(user_input)
print(val)