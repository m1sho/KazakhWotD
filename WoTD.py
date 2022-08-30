
import bs4 as bs
import random
from libretranslatepy import LibreTranslateAPI
class menu:
    lt = LibreTranslateAPI("https://translate.argosopentech.com/")



    lang_Choice = input("choose a language: \n Bulgarian \n Russian\n Kazakh ")
    if lang_Choice=="bg" or "Bulgarian":
        s= str (print(random.choice(open("bg_50k.txt").read().split())))

    print(lt.translate(s, "bg", "en"))
    
 class translate:
    url = 'https://translate.google.ca/#zh-CN/en/%E6%B2%BB%E5%85%B7'
res = requests.get(url)
res.raise_for_status
soup = bs4.BeautifulSoup(res.text, "html.parser")
translation = soup.select('#result_box span')
print(translation)







# add choice to view word in context

















