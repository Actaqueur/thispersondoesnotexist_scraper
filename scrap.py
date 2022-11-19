# scrap visage with https://www.thispersondoesnotexist.com/

import requests
import os



# scrap 500 visage to save in a folder
def scrap():
    for i in range(500):
        r = requests.get('https://thispersondoesnotexist.com/image')
        with open("dataset/visage."+str(i)+".jpg", 'wb') as f:
            f.write(r.content)
        print("visage."+str(i)+".jpg")
