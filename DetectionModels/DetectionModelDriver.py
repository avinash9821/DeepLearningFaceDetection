from sklearn.model_selection import train_test_split
import tensorflow as tf
import random
import numpy as np



random.seed(10)


def Model(targets):
    return tf.keras.Sequential([
        # 1st convolutional layer
        tf.keras.layers.Conv2D(64, kernel_size=(3, 3), input_shape=(100, 100, 1), padding="same",
                               activation="LeakyReLU"),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Dropout(0.2),
        # 2nd convolutional layer
        tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation="LeakyReLU"),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Dropout(0.3),
        # 3rd convolutional layer
        tf.keras.layers.Conv2D(16, kernel_size=(3, 3), activation="LeakyReLU"),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(32, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(16, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(8, activation="relu"),
        tf.keras.layers.Dense(targets, activation="softmax")
    ])


def driver(imageData, targetData):
    trainImages, testImages, trainTarget, testTarget = train_test_split(imageData, targetData, test_size=0.2,
                                                                        random_state=10)
    trainImages = trainImages.reshape(-1, 100, 100, 1)
    testImages = testImages.reshape(-1, 100, 100, 1)
    trainTarget = tf.keras.utils.to_categorical(trainTarget)
    testTarget = tf.keras.utils.to_categorical(testTarget)
    # Creating the model
    model = Model(len(set(targetData)))
    model.summary()
    # early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss')
    model.compile(tf.keras.optimizers.Adam(learning_rate=0.4), loss='categorical_crossentropy', metrics=['accuracy'])
    # Training the model
    output = model.fit(trainImages, trainTarget, batch_size=40, epochs=100,
                       validation_data=(testImages, testTarget))
    return output
