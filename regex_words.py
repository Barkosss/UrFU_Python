# Нахождение слова, встречающегося не менее 3 раза в тексте
import re
from collections import Counter


def find_word(text: str) -> str:
    #return re.findall(r"(.+\S)[\w\s]+?\1[\w\s]+?\1", text)
    return re.findall(r"(\w+)((\s*\w+)*\s+\1){2}", text)

arr = [["kos", "sd kos kos kos bar"],
       ["bar", "bar kos kos bar bar"],
       ["kos", "asdsa af bar kos kos kos"]]
for accept, words in arr:
    if accept == find_word(words)[0]:
        print("True: " + accept + " | " + words)
    else:
        print("False: " + accept + " | " + words)
#print(find_word("sd kos kos kos bar"))