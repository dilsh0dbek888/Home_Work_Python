import re

email = input("email kiriting : \n>>>>")

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'


ema_il = re.match(andoza, email)
if ema_il:
    print(f"{email} Bu email to'g'ri.")
else:
    print(f"{email} Bu noto'g'ri email")




tel_nomer = input("Telfon raqam kiriting :\n>>>")

andoza = '^[\+]?[(]?998[)]?[-\s\.]?[0-9]{2}[)]?[0-9]{3}[-\s\.]?[0-9]{4}$'

moslik = re.match(andoza, tel_nomer)

if moslik:
    if tel_nomer.startswith('+'):
        print(f"{tel_nomer} - Aloqa")
    else:
        print(f"{tel_nomer} - Raqam")
else:
    print(f"{tel_nomer} - Xato")