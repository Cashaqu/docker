import requests
import json
from Ceasar.ceasar_algorithms import ceasar_cipher, shift, alphabet


url = 'http://localhost:8000/prediction'

def test_post_ceasar(url):
    input_text = 'This is test sentence'
    encoded_text = ceasar_cipher(input_text, shift=shift, alphabet=alphabet)

    print(f'Original text:    {input_text}')
    print(f'To Model input:    {encoded_text}')

    response = requests.post(url, data=json.dumps({'text': input_text}))
    prediction_output = response.json()

    print(f'Prediction text:    {prediction_output["text"]}')