def caesar_cipher(text, shift, direction):
    result = ""
    if direction == "decode":
        shift = -shift
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

def main():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'end' to stop:\n").lower()
        if direction == "end":
            break
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        print(f"The {direction}d text is: {caesar_cipher(text, shift, direction)}")

if __name__ == "__main__":
    main()
