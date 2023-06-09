# -*- coding: utf-8 -*-
"""Finals.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wK2nJXBuCgydmbt_-O25Xkcq2_C0pEzM

# **FINALS**
"""

# connecting to google drive
from google.colab import drive
drive.mount("/content/drive")

# importing dataset
import os
path_dir = "/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/Cattle Breeds"
list_dir = os.listdir(path_dir)
path, dirs, files = next(os.walk(path_dir))

print(path)
print(dirs)
print(files)
print(list_dir)

# making new base directory
orig_dir = path_dir
base_dir = "/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new"
model_dir = "/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/models"

try:
    os.mkdir(path_dir)
    os.mkdir(model_dir)
    print("Directory created successfully!")
except FileExistsError:
    print("Directory already exists.")
except OSError as e:
    print(f"Directory creation failed: {e}")

# creating directory for train and validation
train_directory = os.path.join(base_dir, 'train')
validation_directory = os.path.join(base_dir, 'validation')

try:
    os.mkdir(validation_directory)
    os.mkdir(train_directory)
    print("Directory created successfully!")
except FileExistsError:
    print("Directory already exists.")
except OSError as e:
    print(f"Directory creation failed: {e}")



try:
    # creating directories for training dataset
    os.mkdir(os.path.join(train_directory, "Ayrshire cattle"))
    os.mkdir(os.path.join(train_directory, "Holstein Friesian cattle"))
    os.mkdir(os.path.join(train_directory, "Jersey cattle"))
    os.mkdir(os.path.join(train_directory, "Brown Swiss cattle"))
    os.mkdir(os.path.join(train_directory, "Red Dane cattle"))
    # creating directories for validation dataset
    os.mkdir(os.path.join(validation_directory, "Ayrshire cattle"))
    os.mkdir(os.path.join(validation_directory, "Holstein Friesian cattle"))
    os.mkdir(os.path.join(validation_directory, "Jersey cattle"))
    os.mkdir(os.path.join(validation_directory, "Brown Swiss cattle"))
    os.mkdir(os.path.join(validation_directory, "Red Dane cattle"))
    print("Directory created successfully!")
except FileExistsError:
    print("Directory already exists.")
except OSError as e:
    print(f"Directory creation failed: {e}")

import random
from shutil import copyfile

# creating a splitting function
def split_data(source, training, validation, split_size):
    files = []
    for name in os.listdir(source):
        file = source + name
        if os.path.getsize(file) > 0:
            files.append(name)
        else:
            print(name + " is zero length, so ignoring.")

    training_length = int(len(files) * split_size)
    valid_length = int(len(files) - training_length)
    shuffled_set = random.sample(files, len(files))
    training_set = shuffled_set[0:training_length]
    valid_set = shuffled_set[training_length:]

    for name in training_set:
        this_file = source + name
        destination = training + name
        copyfile(this_file, destination)

    for name in valid_set:
        this_file = source + name
        destination = validation + name
        copyfile(this_file, destination)

# declaring variable for the train and validation paths



# ayrshire
ayrshire_path_source = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/Cattle Breeds/Ayrshire cattle/'
ayrshire_path_training = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/train/Ayrshire cattle/'
ayrshire_path_validation = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/validation/Ayrshire cattle/'


# holstein_friesian
holstein_friesian_path_source = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/Cattle Breeds/Holstein Friesian cattle/'
holstein_friesian_path_training = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/train/Holstein Friesian cattle/'
holstein_friesian_path_validation = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/validation/Holstein Friesian cattle/'


# jersey
jersey_path_source = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/Cattle Breeds/Jersey cattle/'
jersey_path_training = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/train/Jersey cattle/'
jersey_path_validation = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/validation/Jersey cattle/'

# brown_swiss 
brown_swiss_path_source = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/Cattle Breeds/Brown Swiss cattle/'
brown_swiss_path_training = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/train/Brown Swiss cattle/'
brown_swiss_path_validation = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/validation/Brown Swiss cattle/'

# red_dane 
red_dane_path_source = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/Cattle Breeds/Red Dane cattle/'
red_dane_path_training = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/train/Red Dane cattle/'
red_dane_path_validation = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/validation/Red Dane cattle/'

split_size = .80

split_data(ayrshire_path_source, ayrshire_path_training, ayrshire_path_validation, split_size)
split_data(holstein_friesian_path_source, holstein_friesian_path_training, holstein_friesian_path_validation, split_size)
split_data(jersey_path_source, jersey_path_training, jersey_path_validation, split_size)
split_data(brown_swiss_path_source, brown_swiss_path_training, brown_swiss_path_validation, split_size)
split_data(red_dane_path_source, red_dane_path_training, red_dane_path_validation, split_size)

import matplotlib.pyplot as plt

directory_labels = ['Ayrshire cattle', 'Holstein Friesian cattle', 'Jersey cattle', 'Brown Swiss cattle', 'Red Dane cattle']
nimgs = {}

for i in directory_labels:
    nimages = len(os.listdir(train_directory + '/' + i + '/'))
    nimgs[i]=nimages
    
plt.figure(figsize=(9, 6))
plt.bar(range(len(nimgs)), list(nimgs.values()), align='center')
plt.xticks(range(len(nimgs)), list(nimgs.keys()))
plt.title('Distribution of different classes in Training Dataset')
plt.show()

# declaring the default size of pictures
img_width = 64
img_height = 64

# declaring batchsize
batch_size = 16

from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1/255.0,
                                   rotation_range=30,
                                   zoom_range=0.4,
                                   horizontal_flip=True     
                        )

train_generator = train_datagen.flow_from_directory(train_directory,
                                                    batch_size=batch_size,
                                                    class_mode='categorical',
                                                    target_size=(img_height, img_width))

validation_datagen = ImageDataGenerator(rescale = 1/255.0)

validation_generator = validation_datagen.flow_from_directory(validation_directory,
                                                              batch_size=batch_size,
                                                              class_mode='categorical',
                                                              target_size=(img_height, img_width)
                                                             )

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense


def baseline_model():
  # Define the model architecture
  model = Sequential()

  model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)))
  model.add(MaxPooling2D(pool_size=(2, 2)))

  model.add(Conv2D(64, (3, 3), activation='relu'))
  model.add(MaxPooling2D(pool_size=(2, 2)))

  model.add(Conv2D(128, (3, 3), activation='relu'))
  model.add(MaxPooling2D(pool_size=(2, 2)))

  model.add(Flatten())

  model.add(Dense(256, activation='relu'))
  model.add(Dense(128, activation='relu'))
  model.add(Dense(5, activation='softmax'))  # num_classes is the number of cattle breeds
  return model

model = baseline_model()

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit_generator(train_generator,
                              epochs=30,
                              verbose=1,
                              validation_data=validation_generator)

baseline_model_test_loss, baseline_model_test_acc = model.evaluate(validation_generator)
print("\nTest loss: {:.4f}".format(baseline_model_test_loss))
print("Test accuracy: {:.4f}%".format((baseline_model_test_acc)*100))

accuracy = history.history['accuracy']
validation_accuracy = history.history['val_accuracy']

epochs=range(len(accuracy))

figure_one = plt.figure(figsize=(14,7))

plt.plot(epochs, accuracy, 'r', label = "Training Accuracy")
plt.plot(epochs, validation_accuracy, 'b', label = "Validation Accuracy")
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training and validation accuracy')
plt.legend(loc='lower right')
plt.show()

model_path = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/models/model_best.h5'
model.save(model_path)

import tensorflow as tf
model_path = '/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/models/model_best.h5'
loaded_model = tf.keras.models.load_model(model_path)

import numpy as np
from keras.utils.image_utils import array_to_img, img_to_array, load_img

img_size = (64,64)
indices = train_generator.class_indices
print(indices)

import matplotlib.pyplot as plt
image = load_img("/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/validation/Ayrshire cattle/Ayrshirecattle51_c.jpg", target_size = img_size)
x = img_to_array(image)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
classes = loaded_model.predict(images)
plt.imshow(image)
max_value = max(classes[0])
max_index = list(classes[0]).index(max_value)
np.around(classes[0], decimals = 2)
print('Real: Ayrshire cattle', ', Predicted:',list(indices.keys())[max_index])

image = load_img("/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/validation/Brown Swiss cattle/BrownSwisscattle121_c.jpg", target_size = img_size)
x = img_to_array(image)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
classes = model.predict(images)
plt.imshow(image)
max_value = max(classes[0])
max_index = list(classes[0]).index(max_value)
np.around(classes[0], decimals = 2)
print('Real: Brown Swiss cattle', ', Predicted:',list(indices.keys())[max_index])

image = load_img("/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/validation/Holstein Friesian cattle/HolsteinFriesiancattle72.jpg", target_size = img_size)
x = img_to_array(image)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
classes = model.predict(images)
plt.imshow(image)
max_value = max(classes[0])
max_index = list(classes[0]).index(max_value)
np.around(classes[0], decimals = 2)
print('Real: Holstein Friesian cattle', ', Predicted:',list(indices.keys())[max_index])

image = load_img("/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/validation/Jersey cattle/Jerseycattle130_c.jpg", target_size = img_size)
x = img_to_array(image)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
classes = model.predict(images)
plt.imshow(image)
max_value = max(classes[0])
max_index = list(classes[0]).index(max_value)
np.around(classes[0], decimals = 2)
print('Real: Jersey cattle', ', Predicted:',list(indices.keys())[max_index])

image = load_img("/content/drive/MyDrive/CPES2 - 3rd Year/2nd Semester/CPE 019 - Emerging Technologies 2/finals/FINALS/cattle_breeds_new/validation/Red Dane cattle/RedDanecattle0_c.jpg", target_size = img_size)
x = img_to_array(image)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
classes = model.predict(images)
plt.imshow(image)
max_value = max(classes[0])
max_index = list(classes[0]).index(max_value)
np.around(classes[0], decimals = 2)
print('Real: Red Dane cattle', ', Predicted:',list(indices.keys())[max_index])