import os
import sys
from PIL import Image
def create_dataset(directory, target_directory, extension, image_size):
    if (directory == ''):
        directory = os.curdir

    images = filter(lambda x: x.endswith(extension), os.listdir(directory))

    print(directory + '\t')
    print(images)
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    index = 0
    for image in images:
        img = Image.open(directory + '/' + image)
        resized_img = img.resize(image_size, Image.ANTIALIAS)
        resized_img.save(target_directory + '/' + str(index) + extension)
        index += 1
    print('Updated ' + str(index) + ' images')

# directory, target directory, extension, height, weight
print sys.argv
if len(sys.argv) != 6:
    print('Illegal args number')
    sys.exit()

create_dataset(sys.argv[1], sys.argv[2],
               sys.argv[3], (int(sys.argv[4]), int(sys.argv[5])))