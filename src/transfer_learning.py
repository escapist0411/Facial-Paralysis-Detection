import tensorflow as tf
from src.preprocess import load_dataset
from sklearn.model_selection import train_test_split

# Load dataset
X, y = load_dataset("dataset")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Use ResNet50 (High-End Model)
base_model = tf.keras.applications.ResNet50(
    weights="imagenet",
    include_top=False,
    input_shape=(128, 128, 3)
)

base_model.trainable = False  # Freeze pretrained layers

# Build model
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))

# Save high-end model
model.save("models/resnet_paralysis.keras")

print("✅ Transfer Learning Training Done!")
