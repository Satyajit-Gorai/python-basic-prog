import random
import urllib.request

def dwn_img(url):
    name = random.randrange(1,1000)
    full_name= str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)
    
    
dwn_img("https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRO3Kv8qo5R62iRvthx-FSZjMiMcWLqTSBMjFqat8UVmeaD0B2c")