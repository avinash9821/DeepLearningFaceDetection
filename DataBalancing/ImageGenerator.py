import os

from keras.preprocessing.image import ImageDataGenerator


def generator():
    return ImageDataGenerator(
        rotation_range=40,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)


def imageGenerator(image, n, targetName):
    # image = Image Data as numpy values
    # n = Number of Images to generate
    image = image.reshape((1,) + image.shape)
    i = 0
    os.mkdir("/Users/dirisala/FaceDetection/GenerateData/"+targetName)
    for batch in generator().flow(image,
                                  save_to_dir="/Users/dirisala/FaceDetection/GenerateData/"+targetName,
                                  save_prefix=targetName+str(i),
                                  batch_size=1,
                                  save_format='jpg'):
            i += 1

            if i >= 200:
                break