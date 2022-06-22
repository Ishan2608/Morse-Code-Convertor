morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-','u': '..-', 
    'v': '...-', 'w': '.--', 'x': '--.--', 'y': '-.--', 'z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

def text_to_morse_code():
    global morse_code
    task_type = input('What do you want to do? (encode/decode): ').lower()
    message = input('Enter you message here. ').lower()
    output = []
    if task_type == 'encode':
        for c in message:
            if c in morse_code:
                output.append(morse_code[c])
            else:
                output.append(c)
        print(" ".join(output))

    elif task_type == 'decode':
        message_array = []
        word = ""
        for c in range(len(message)):
            if message[c] != " " :
                word += message[c]
            elif message[c] == " " and message[c-1] != " ":
                message_array.append(word)
                word = ""
            elif message[c] == " " and message[c+1] == " ":
                message_array.append(" ")
                word=""
            if c == len(message)-1:
                message_array.append(word)
                word = ""

        for item in message_array:
            for l in morse_code:
                if item == morse_code[l]:
                    output.append(l)
                    break
                elif item == " ":
                    output.append(" ")
                    break
        print("".join(output))

        
keep_converting = True
while keep_converting:
    user_wish = input('Want to use morse code convertor?(y/n): ').lower()
    if user_wish == 'y' or user_wish == 'yes':
        text_to_morse_code()
    elif user_wish == 'n' or user_wish == 'no':
        keep_converting = False
        pass
    else:
        print('No comprehendable input entered.')
        keep_converting = False
