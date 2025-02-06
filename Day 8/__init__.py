alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def decrypt(type_in,original_text,shifting):
    encrypt_word=[]
    for text in original_text:
        if text not in alphabet:
            encrypt_word+=text
        else:
            if type_in=='decrypt':
                shifted_position= alphabet.index(text)-shifting
            else:
                shifted_position = alphabet.index(text) + shifting
            shifted_position %=len(alphabet)
            encrypt_word.append(alphabet[shifted_position])
    print(f" Here is the {type_in}d result: {''.join(encrypt_word)}")


prog_is_on=True
while prog_is_on:

    type_in= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text=input("Type your text: \n").lower()
    shift=int(input("Type the shift number\n"))

    decrypt(type_in,text,shift)
    play=input("Do you want to do it again?y/n")
    if play=='n':
        prog_is_on=False
        print("See you later!")





