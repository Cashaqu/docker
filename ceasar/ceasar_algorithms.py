import torch
sample = 'Gaius Julius Caesar was born into a patrician family, the gens Julia on 12 July 100 BC.'
shift = 17
alphabet = 'ABCDEFGHIJKLMNOPQRSTVUWXYZabcdefghijklmnopqrstvuwxyz 0123456789'
dict_char = {char: i for i, char in enumerate(['None'] + [char for char in alphabet])}

def ceasar_cipher(text, shift, alphabet, decryption=False):
    output = ''
    if decryption == True:
        shift = -shift
    for x in range(len(text)):
        if text[x] in alphabet:
            output += alphabet[(alphabet.index(text[x]) + shift) % len(alphabet)]
        else:
            output += text[x]
    return output

# to torch tensor function
def to_torch(text, sen_len, dictionary):
    X = torch.zeros((len(text), sen_len), dtype=int)
    for i in range(len(text)):
        for j, k in enumerate(text[i]):
            if j >= sen_len:
                break
            #    if length of a sequence is less than the fixed length of a tensor, fill with 'None' (aka Padding)
            X[i,j] = dict_char.get(k, dict_char['None'])
    return X