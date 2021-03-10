import string


def change_string(plain_text, shift=1):
    letters = string.ascii_letters
    print(letters)
    mask = letters[shift:] + letters[:shift]
    print(mask)
    trantab = str.maketrans(letters, mask)
    return plain_text.translate(trantab)


print(change_string("murshid"))
