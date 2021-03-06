# load MNIST dataset in keras
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
digit = train_images[4]
# Create the network architecture
from keras import models
from keras import layers

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

# Compile the network
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# Prep image data by reshaping it from uint8 to float32
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# Prep labels by categorically encoding them
from keras.utils import to_categorical

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# train the data, fitting the model to the training data
network.fit(train_images, train_labels, epochs=5, batch_size=128)

# make sure the model performs well on the test set too
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc:', test_acc)
print('test_loss:', test_loss)

# lets check out the 4th image from mnist

import matplotlib.pyplot as plt
#plt.imshow(digit, cmap=plt.get_cmap('binary'))
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()