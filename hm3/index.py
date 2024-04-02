sentence = input("Введіть речення з двох слів: ")

word1, word2 = sentence.split()

new_variable1 = "!{} {}?".format(word2.upper(), word1.capitalize())
new_variable2 = "!{} {}?".format(word2.upper(), word1.capitalize())
new_variable3 = f"!{word2.upper()} {word1.capitalize()}?"

print(sentence, end="<<<>>>")
print(new_variable1, end="<<<>>>")
print(new_variable2, end="<<<>>>")
print(new_variable3)
