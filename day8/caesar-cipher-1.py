alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


cipher_text = ""

encoding = True


def encrypt(direction, text, shift, cipher_text):

    if direction == "encode":
        for letter in text:
            position = alphabet.index(letter)
            shifting_letter = (position + shift) % 26
            cipher_text += alphabet[shifting_letter]

        print(f"The encoded text is: {cipher_text}")


encrypt(direction, text, shift, cipher_text)
