def reverse_string(word):
    if not str or len(word) < 2 or not isinstance(word, str):
        return "That's not going to work"

    listArray = list(word)
    listArray.reverse()
    return ''.join(listArray)

print(reverse_string('hello'))