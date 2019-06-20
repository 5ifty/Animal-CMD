import requests
import json
import PIL
from PIL import Image
from io import BytesIO
import os


class animals():
    def __init__(self):
        bio = BytesIO()


        print("Welcome to the Animal display CMD the animals we can display are: dog, cat, birb, panda, duck and fox")
        print("Please type which animal picture you want displayed! (Please ensure that all requests are not capitalised or this may not work)")
        user_input = input()


        if user_input == "dog":
            url = "https://random.dog/woof.json"
            response = requests.get(url)
            data = response.text
            parsed = json.loads(data)
            pic = parsed["url"]
            print("Please wait while the image from the server opens on your PC!")
            image = Image.open(requests.get(pic, stream=True).raw)
            image.show()
            print("Image should be displayed, if not please try again!")
            print(f" \n \n \n \n \n This CMD was made by 5ifty in python. Please press the enter button to exit!")
            input()

        elif user_input == "cat":
            url = "https://nekos.life/api/v2/img/meow"
            response = requests.get(url)
            data = response.text
            parsed = json.loads(data)
            pic = parsed["url"]
            print("Please wait while the image from the server opens on your PC!")
            image = Image.open(requests.get(pic, stream=True).raw)
            image.show()
            print("Image should be displayed, if not please try again!")
            print(f" \n \n \n \n \n This CMD was made by 5ifty in python. Please press the enter button to exit!")
            input()

        elif user_input == "birb":

            url = "https://api.alexflipnote.xyz/birb"
            response = requests.get(url)
            data = response.text
            parsed = json.loads(data)
            pic = parsed["file"]
            print("Please wait while the image from the server opens on your PC!")
            image = Image.open(requests.get(pic, stream=True).raw)
            image.show()
            print("Image should be displayed, if not please try again!")
            print(f" \n \n \n \n \n This CMD was made by 5ifty in python. Please press the enter button to exit!")
            input()

        elif user_input == "panda":

            url = "https://some-random-api.ml/img/panda"
            response = requests.get(url)
            data = response.text
            parsed = json.loads(data)
            pic = parsed["link"]
            print("Please wait while the image from the server opens on your PC!")
            image = Image.open(requests.get(pic, stream=True).raw)
            image.show()
            print("Image should be displayed, if not please try again!")
            print(f" \n \n \n \n \n This CMD was made by 5ifty in python. Please press the enter button to exit!")
            input()


        elif user_input == "duck":

            url = "https://random-d.uk/api/v1/random"
            response = requests.get(url)
            data = response.text
            parsed = json.loads(data)
            pic = parsed["url"]
            print("Please wait while the image from the server opens on your PC!")
            image = Image.open(requests.get(pic, stream=True).raw)
            image.show()
            print("Image should be displayed, if not please try again!")
            print(f" \n \n \n \n \n This CMD was made by 5ifty in python. Please press the enter button to exit!")
            input()

        elif user_input == "red panda":

            url = "https://some-random-api.ml/img/red_panda"
            response = requests.get(url)
            data = response.text
            parsed = json.loads(data)
            pic = parsed["link"]
            print("Please wait while the image from the server opens on your PC!")
            image = Image.open(requests.get(pic, stream=True).raw)
            image.show()
            print("Image should be displayed, if not please try again!")
            print(f" \n \n \n \n \n This CMD was made by 5ifty in python. Please press the enter button to exit!")
            input()


        elif user_input == "fox":

            url = "https://some-random-api.ml/img/fox"
            response = requests.get(url)
            data = response.text
            parsed = json.loads(data)
            pic = parsed["link"]
            print("Please wait while the image from the server opens on your PC!")
            image = Image.open(requests.get(pic, stream=True).raw)
            image.show()
            print("Image should be displayed, if not please try again!")
            print(f" \n \n \n \n \n This CMD was made by 5ifty in python. Please press the enter button to exit!")
            input()

        else:
            print("Please choose one of the animals above!")
            print(f" \n \n \n \n \n This CMD was made by 5ifty in python. Please press the enter button to exit!")
            input()



if __name__ == '__main__':
    animals()
