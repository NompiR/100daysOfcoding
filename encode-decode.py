alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
#this is my opinion idea
'''
word = "doze"
encode_letter = ""
ip = 4
for i in word:
    for j in range(0, len(alphabets)):
        if i == alphabets[j]:
            shift = (j + ip) - 26 #or use (j + ip) % 26
            encode_letter += alphabets[shift]

print(encode_letter)


same both it is from course

def encode(original_text, shift_amount):

    cipher_text= ""

    for letter in original_text:
        shift_position = alphabets.index(letter) + shift_amount
        shift_position %= len(alphabets)
        cipher_text += alphabets[shift_position]
        
    print(cipher_text)
'''


def encode_letter(words_l, let_len, word_shifts):
    encode_letters = ""
    for k in words_l:
        for m in range(0, let_len):
            if k == alphabets[m]:
                encode_letters += alphabets[m + word_shifts]
    return encode_letters

def decode_letter(let_len, word_shifts, e_letters):
    decode_letters = ""
    for h in e_letters:
        for z in range(0, let_len):
            if h == alphabets[z]:
                decode_letters += alphabets[z - word_shifts]
    return decode_letters

letter_len = len(alphabets)
e_letter = ""
d_letter = ""

input_choice_encode_decode = input("Want to encode type 'e' or decode type 'd': ")
words = input("Enter word you want to encode: ")
word_shift = int(input("Enter word shift number: "))

if input_choice_encode_decode == 'e':
    e_letter = encode_letter(words, letter_len, word_shift)
    print(e_letter)
else:
    d_letter = decode_letter(letter_len, word_shift, words)
    print(d_letter)
