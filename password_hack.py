# import random
# import pyautogui
#
# chars="abcdefghijklmnopqrstuvwxyz0123456789"
#
# allchar=list(chars)
#
# pwd=pyautogui.password("Enter a password:")
#
# sample_pwd=""
#
# while(sample_pwd !=pwd):
#     sample_pwd=random.choices(allchar,k=len(pwd))
#
#     print("<==="+str(sample_pwd)+"===>")
#
#     if(sample_pwd ==list(pwd)):
#         print("the password is:"+ "".join(sample_pwd))
#         break


import hashlib

pass_found=0
i_hash=input("Enter a hashed password: ")
p_doc="filepath"
p_file=open(p_doc,'r')

for word in p_file:
    enc_word=word.encode("utf-8")
    hash_word=hashlib.md5(enc_word)
    digest=hash_word.hexdigest()

    if digest == i_hash:
        print("Password found: ", word)
        pass_found=1
        break

if not pass_found:
    print("Password not found")