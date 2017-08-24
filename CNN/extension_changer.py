import os
import sys
from PIL import Image

def change_extension(directory, target_directory, from_ex, to_ex):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    images = filter(lambda x: x.endswith(from_ex), os.listdir(directory))

    print(images)
    index = 0
    for image in images:
        img = Image.open(directory + '/' + image)
        img.save(target_directory+'\\'+str(index)+to_ex)
        index+=1
    print('Updated ' + str(index) + ' images')

if len(sys.argv) != 5:
    print('Illegal args number')
    sys.exit()

change_extension(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
