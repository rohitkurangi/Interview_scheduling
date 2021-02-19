from rest_framework.response import Response

headers_mapping = {"csv": {"content-type": "application/csv"},
                   "json": {"content-type": "application/json"}}

def ok_response(data={}, status=True, code=200, message="ok", headers='json'):
    mydata = {"data": data, "message": message, "status": True}
    return Response(data=mydata, status=code, content_type=headers_mapping[headers])

def error_response(data={}, status=False, code=401, message="error", headers='json'):
    mydata = {"data": data, "message": message, "status": False}
    return Response(data=mydata, status=code, content_type=headers_mapping[headers])



import base64
from Crypto.Cipher import AES

key="Interview"
string = "arzted2_sha256$36000$ATChcb3PbCBG$OLd2uYVtymtRmEG9wc0ACecF7jwutOJD4FZP36N7160="


BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


iv = "aesEncryptionKey"
key = "encryptionIntVec"

def encrypt_data(data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    c = cipher.encrypt(pad(str(data)))
    encoded = base64.b64encode(c)
    return encoded


def decrypted_data(data):
    dec = base64.decodestring(data)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    c2 = cipher.decrypt(dec)
    decoded = unpad(c2)
    return decoded