def is_palindrome(word):
    word = word.lower().replace(' ', '')
    return word == word[::-1]

inputdata = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')

palindromes = filter(is_palindrome, inputdata)

print(list(palindromes))
