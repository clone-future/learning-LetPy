def encrypt(s, k):
    letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    word = s.upper()
    q = len(letters)
    word_num = {}
    listUp = 0
    result = ""
    for i, j in enumerate(word):
        if j in letters:
            if (letters.find(j) + k) > q or (letters.find(j) + k) <= 0:
                listUp = (letters.find(j) + k) % q
                word_num[i] = letters[listUp]
            else:
                word_num[i] = letters[letters.index(j) + k]
        else:
            word_num[i] = j
        result = result + word_num[i]
    return result
message = input()
encrypted_message = encrypt(message, 135)
decrypted_message = encrypt(encrypted_message, -135)
print(encrypted_message)
print(decrypted_message)