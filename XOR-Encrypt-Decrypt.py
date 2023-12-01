def checkInputLength():
    global inputMsg, inputKey

    while len(inputMsg) <= 5 or len(inputKey) <= 5:
        print("Message dan Key tidak boleh kurang dari 5 karakter.")
        inputMsg = input('Masukkan Pesan: ')
        inputKey = input('Masukkan Key: ')

def equalizeLength():
    global finalKey

    if len(inputMsg) > len(inputKey):
        tempInputKey = inputKey * (len(inputMsg) // len(inputKey) + 1)
        finalKey = tempInputKey[:len(inputMsg)]
    else:
        finalKey = inputKey[:len(inputMsg)]

def equalizeBitDigit(inputData):
    formatted_binary_chars = [
        format(ord(char), '08b') for char in inputData
    ]

    result = ' '.join(formatted_binary_chars)
    return result


def printMsgAndKey():
    equalizeLength()

    print("\nPenyamaan Panjang Pesan dan Kunci:")
    print("Pesan: " + inputMsg)
    print(f"Panjang Karakter Pesan: {len(inputMsg)}")
    print("Key: " + finalKey)
    print(f"Panjang Karakter Kunci: {len(finalKey)}")
    print("\nBit Pesan:")
    print(equalizeBitDigit(inputMsg))
    print("Bit Key:")
    print(equalizeBitDigit(finalKey))

def xorBits(msgBit, keyBit):
    msgBit = msgBit.replace(" ", "")
    keyBit = keyBit.replace(" ", "")
    
    result = ''
    for a, b in zip(msgBit, keyBit):
        if a != b:
            result += '1'
        else:
            result += '0'

    return result

def printXORResult(XORResult):
    xorSplit = [XORResult[i:i+8] for i in range(0, len(XORResult), 8)]
    xorSplitSpace = ' '.join(xorSplit)

    print(xorSplitSpace)

def main():
    global inputMsg, inputKey, finalKey

    print("Enkripsi dan Dekripsi Berbasis ASCII 8 BIT\n")
    inputMsg = input('Masukkan Pesan: ')
    inputKey = input('Masukkan Key: ')

    checkInputLength()
    printMsgAndKey()

    messageBit = equalizeBitDigit(inputMsg)
    keyBit = equalizeBitDigit(finalKey)

    XORResult = xorBits(messageBit, keyBit)
    print("\nHasil XOR dari Bit Pesan dan Bit Key:")
    printXORResult(XORResult)

    print("\nHasil Enkripsi:")
    print(XORResult)

if __name__ == "__main__":
    main()
