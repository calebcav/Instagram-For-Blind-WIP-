import object_detection
import speech
from gtts import gTTS
import subprocess


def createDictionary(lst):
    d = {}

    for thing in lst:
        if thing[0] in d:
            d[thing[0]] += 1
        else:
            d[thing[0]] = 1
    return d




text = "next page"

if text == "next page":
    lst = object_detection.listOfObjects("image")
    d = createDictionary(lst)
    seenItems = set()
    for obj in lst:
        if obj[0] not in seenItems:
            seenItems.add(obj[0])
            if d[obj[0]] > 5:
                Helen = gTTS(text = f"There are many {obj[0]}s")
            elif d[obj[0]] > 1:
                Helen = gTTS(text = f"There are a couple of {obj[0]}s")
            else:
                Helen = gTTS(text = f"There is a {obj[0]}")
            Helen.save("items.mp3")
            subprocess.call(["afplay", "items.mp3"])




