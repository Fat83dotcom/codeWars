def rot13(message):
    cypherMsg = ''
    for letter in message:
        letterAscii = ord(letter)
        if 65 <= letterAscii <= 90:
            letterCypher = letterAscii + 13
            if letterCypher > 90:
                letterCypher -= 26
            cypherMsg += chr(letterCypher)
        elif 97 <= letterAscii <= 122:
            letterCypher = letterAscii + 13
            if letterCypher > 122:
                letterCypher -= 26
            cypherMsg += chr(letterCypher)
        else:
            cypherMsg += letter
    return cypherMsg


print(rot13('afefeNgg, ttT 090'))
