def use_secret_encoder(plain_text):
  encoded_message = ""
  for letter in plain_text:
    new_letter =  chr(ord(letter) + 3)
    encoded_message += new_letter

  return encoded_message

def use_secret_decoder(encoded_text):
  return cipher_text
