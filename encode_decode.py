alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', 
'17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

#caesar cipher
def caesar_cipher(message, user_letter, coding_method):
    '''
    shifts each letter key times over

    ex. if key = 1: a = b, b = c ... z = a
    '''

    output = '' #represents final encoded/decoded string

    if coding_method == 'encode':
        
        key = alphabet.index(user_letter) + 1

    else:

        key = (alphabet.index(user_letter) + 1) * -1 #shift key is negative for decoding

    for x in message:
        letter = x.lower() #makes characters lowercase to match case with pre-defined alphabet list

        if letter != ' ':

            letter_index = alphabet.index(letter) + key #shifts the index letter as per the shift key

            if letter_index > 25:
                letter_index -= 26 #loops the alphabet back to a after z

            new_letter = alphabet[letter_index]

            if x.isupper():
                output += new_letter.upper() #maintains any uppercase letters from initial message

            else:
                output += new_letter

        else: #maintains any spaces from initial message
            output += ' '

    return output

#alphanumeric cipher
def alphanumeric_cipher(message):
    '''
    each letter in alphabet corresponds to a number such that a = 1, b = 2 ... z = 26
    '''

    output = ''

    try: #runs if decoding message
        int(message[0])
        
        original = numbers
        compare = alphabet

        message = message.split()

    except ValueError: #runs if encoding message
        original = alphabet
        compare = numbers
        
    for char in message:
        
        indx = original.index(char)

        new_char = compare[indx]

        if new_char.isdigit():
            output += new_char + ' '
        
        else:
            output += new_char

    return output

#atbash cipher
def atbash_cipher(message):
    '''
    inverts alphabet such that a = z, b = y ... z = a
    '''

    output = ''

    for x in message:
        letter = x.lower()

        if x != ' ':

            letter_index = alphabet.index(letter)
            new_letter_index = (letter_index + 1) * -1 #negative runs through alphabet list backwards
            new_letter = alphabet[new_letter_index]

            if x.isupper():
                new_letter = new_letter.upper()
        
        else:
            new_letter = ' '

        output += new_letter

    return output

#main program loop
while True:

    user_cipher = input('Please select a cipher: \n 1. Caesar Cipher \n 2. Alphanumeric Cipher \n 3. Atbash Cipher \n 4. Quit \n')

    if user_cipher == '1':

        #caesar cipher main loop
        while True:
        
            user_choice = input('Please select one of the following: \n 1. encode \n 2. decode \n 3. quit \n')
            
            if user_choice == '1':

                user_message = input('Please enter your message: ')
                user_letter = input('Which letter is equivalent to A? ')
                user_encoded = caesar_cipher(user_message, user_letter, 'encode')

                print('Your encoded message is: ' + user_encoded)
            
            elif user_choice == '2':

                user_message = input('Please enter your message: ')
                user_letter = input('Which letter is equivalent to A? ')
                user_decoded = caesar_cipher(user_message, user_letter, 'decode')

                print('Your decoded message is: ' + user_decoded)

            elif user_choice == '3':
                break

            else:
                print('Please enter 1, 2, or 3.')

    elif user_cipher == '2':

        #alphanumeric cipher main loop
        while True:

            user_choice = input('Please select one of the following: \n 1. encode \n 2. decode \n 3. quit \n')

            if user_choice == '1':
                user_message = input('Please enter your message (no spaces): ')
                user_encoded = alphanumeric_cipher(user_message)
                print('Your encoded message is: ' + user_encoded)

            elif user_choice == '2':
                user_message = input('Please enter your message (split numbers with spaces): ')
                user_decoded = alphanumeric_cipher(user_message)
                print('Your decoded message is: ' + user_decoded)
            
            elif user_choice == '3':
                break

            else:
                print('Please enter 1, 2, or 3.')

    elif user_cipher == '3':
        
        #atbash cipher main loop
        while True:

            user_choice = user_choice = input('Please select one of the following: \n 1. encode \n 2. decode \n 3. quit \n')

            if user_choice == '1':
                user_message = input('Please enter your message: ')
                user_encoded = atbash_cipher(user_message)
                print('Your encoded message is: ' + user_encoded)

            elif user_choice == '2':
                user_message = input('Please enter your message: ')
                user_decoded = atbash_cipher(user_message)
                print('Your decoded message is: ' + user_decoded)
            
            elif user_choice == '3':
                break

            else:
                print('Please enter 1, 2, or 3.')

    else:
        print('Goodbye!')
        break