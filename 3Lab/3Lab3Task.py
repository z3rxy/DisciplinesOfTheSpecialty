#Вариант 3. Напишите программу для расшифровки текста,
#зашифрованного в соответствии с таким алгоритмом: каждая буква
#заменяется на следующую, а последняя буква в алфавите заменяется на
#первую.

def decrypt(text):
    decrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('а') - 1) % 33 + ord('а')) if char != 'а' else ord('я'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
        else:
            decrypted_char = char

        decrypted_text += decrypted_char

    return decrypted_text

encrypted_text = input("Введите зашифрованный текст: ")
decrypted_text = decrypt(encrypted_text)

print(f"Расшифрованный текст: {decrypted_text}")

