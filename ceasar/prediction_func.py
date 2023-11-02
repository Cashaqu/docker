from ceasar.ceasar_algorithms import ceasar_cipher, shift, alphabet, to_torch, dict_char

def prediction(test, model):
    test_enc = [ceasar_cipher(test, shift, alphabet)]
    test_tensor = to_torch(test_enc, 100, dict_char)
    model.eval()
    #predict = trained_model(test_tensor.to(device))
    predict = model(test_tensor)
    predict = predict.squeeze(0)
    predict_test = ''
    for i, j in enumerate(predict):
        if j.argmax() != 0:
            predict_test += list(dict_char.keys())[list(dict_char.values()).index(j.argmax())]
    return predict_test