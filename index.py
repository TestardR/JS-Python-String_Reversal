def reverse_string(str):
    listArray = list(str)
    listArray.reverse()
    return ''.join(listArray)

print(reverse_string('hello'))