"""
Користувач вводить число до 4000. Вивести число римськими цифрами.

"""



import re
def if_numb(text):
    text = re.match(r'^[^4][\d]{1,3}',text)
def val_numb():
    while not if_numb():
        print("input number")
number = val_numb()