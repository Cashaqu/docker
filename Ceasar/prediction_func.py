#   function for predict
from Ceasar.ceasar_algorithms import ceasar_cipher, shift, alphabet, to_torch, dict_char
import torch
#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def prediction(test, model):
    test_enc = [ceasar_cipher(test, shift, alphabet)]
    test_tensor = to_torch(test_enc, 100, dict_char)
    model.eval()
    #predict = model(test_tensor.to(device))
    predict = model(test_tensor)
    predict = predict.squeeze(0)
    predict_test = ''
    for i, j in enumerate(predict):
        if j.argmax() != 0:
            predict_test += list(dict_char.keys())[list(dict_char.values()).index(j.argmax())]
    return predict_test