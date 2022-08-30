
import random
from libretranslatepy import LibreTranslateAPI
class menu:
    lt = LibreTranslateAPI("https://translate.argosopentech.com/")



    lang_Choice = input("choose a language: \n Bulgarian \n Russian\n Kazakh ")
    if lang_Choice=="bg" or "Bulgarian":
        s= str (print(random.choice(open("bg_50k.txt").read().split())))

    print(lt.translate(s, "bg", "en"))







# add choice to view word in context

















