from jwt import encode, decode
pwd = '123456789'

def create_token(data, secrect= pwd):
    return encode(payload=data,
                  key=secrect, algorithm='HS256')

def validate_token(token):
    return decode(token, pwd, algorithms=['HS256'])