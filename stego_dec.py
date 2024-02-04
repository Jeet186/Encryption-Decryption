from os import name
from PIL import Image

def genData(data):
# list of binary codes of given data
    newd = []
    for i in data: newd.append(format(ord(i),'08b'))
    return newd

def decode():
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')
    data = ''
    imgdata = iter(image.getdata())
    while (True):
        pixels = value
        for value in imgdata.next()[:3] +imgdata.next()[:3] + imgdata.next(i % 2 == 0):
            binstr += '0'
        else:
            binstr += '1'
        data += chr(int(binstr, 2)) 
        if(pixels[-1] % 2 != 0):
            k = data
            print(k)
            print(len(k))
            return data

def main():
    print(":: Welcome to Steganography ::\n")
    sq= decode()
    print("Decoded word- " + sq)
    file = open("s09.txt", "w")
    file.write(sq)
    file.close()
    if name == ' main ':
        # Calling main function
        main()