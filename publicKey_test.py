# -*- coding: utf-8 -*-
# 开发人员   ：黎工
# 开发时间   ：2020/6/23  20:41 
# 文件名称   ：publicKey_test.PY
# 开发工具   ：PyCharm

import time
import datetime


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


print(getYesterday())


"""
import rsa

# 生成公钥和秘钥
PublicKey, PrivateKey = rsa.newkeys(999)
text = '非对称加密'
# 使用公钥加密
en_data = rsa.encrypt(text.encode(),PublicKey)
print(en_data)

# 使用私钥解密
de_data = rsa.decrypt(en_data,PrivateKey)
print(de_data.decode())
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
import re
import hashlib


# rsa公钥加密内容
def rsa_encode(text, public_key):
    key = RSA.importKey(b64decode(public_key))
    cipher = PKCS1_v1_5.new(key)
    result = b64encode(cipher.encrypt(text.encode(encoding='utf-8'))).decode('utf-8')
    return result


# 用aes加密文本
def aes_encode(text, key):
    key = key.encode('utf-8')
    print(text)
    print(key)
    cipher = AES.new(key,AES.MODE_CBC,key)
    text = text + (16 - len(text) % 16) * chr(16 - len(text) % 16)
    result = b64encode(cipher.encrypt(text.encode(encoding='utf-8'))).decode('utf-8')
    print(result)
    return result


# aes解密文本
def aes_decode(cipher_text, key):
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, key)
    text = cipher.decrypt(b64encode(cipher_text)).decode('utf-8')
    print(text)
    result = re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f\n\r\t]').sub('',text)
    print(result)
    return result


def stringToMD5(str):
    # 创建md5对象
    m = hashlib.md5()
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()

    print('MD5加密前为：' + str)
    print('MD5加密后为：' + str_md5)

    return str_md5


if __name__ == '__main__':
    stringToMD5('666')
    aes_encode("hello","nsPppx2TME9Eaw==")
    # aes_decode("V/zPkCrT1o5hfXHUfbo66A==","nsPppx2TME9Eaw==")
