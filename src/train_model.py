from src.preprocess import load_dataset
from sklearn.model_selection import train_test_split
import tensorflow as tf
X,y=load_dataset("dataset")
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=tf.keras.Sequential([
 tf.keras.layers.Conv2D(32,(3,3),activation="relu",input_shape=(128,128,3)),
 tf.keras.layers.MaxPooling2D(),
 tf.keras.layers.Conv2D(64,(3,3),activation="relu"),
 tf.keras.layers.MaxPooling2D(),
 tf.keras.layers.Flatten(),
 tf.keras.layers.Dense(128,activation="relu"),
 tf.keras.layers.Dense(1,activation="sigmoid")
])
model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])
model.fit(X_train,y_train,epochs=5,validation_data=(X_test,y_test))
model.save("models/best_model.keras")
print("Training Complete")
