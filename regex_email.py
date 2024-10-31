# Написать функцию, находящаяся email, найти домен (после @) и имя почты (до @)
import re

def valid_email(email: str) -> list:
    list = [False, "", ""]
    arr = re.findall(r"[A-Za-z0-9_.]*@" + r"[A-Za-z0-9.]+\.[a-z]+", email)
    for word in arr:
        list[0] = True if (len(word) > 0) else False
        list[1] = word.split("@")[0]
        list[2] = word.split("@")[1]
    return list

emails = ["bar.and@gmail.com",
       "bar ab2@mail.ru. ",
       "asdsa af bar kos kos kos@ural.ru dasd"]
for email in emails:
    arr_email = valid_email(email)
    if arr_email[0]:
        print("True: " + arr_email[1] + " @ " + arr_email[2])
    else:
        print("False: " + arr_email[1] + " @ " + arr_email[2])