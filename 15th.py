import numpy as np
from tensorflow.keras import datasets, layers, models
# 1) LOAD DATA (images: 28x28 grayscale, labels: 0–9)
(X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()
# 2) PREP DATA (add channel dim, scale 0–1)
X_train = (X_train / 255.0).astype("float32")[..., np.newaxis] # (60000,28,28,1)
X_test = (X_test / 255.0).astype("float32")[..., np.newaxis]
num_classes = 10
# 3) BUILD MODEL (small 2D CNN)
model = models.Sequential([
 layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
 layers.MaxPooling2D(2,2),
 layers.Conv2D(64, (3,3), activation='relu'),
 layers.MaxPooling2D(2,2),
 layers.Flatten(),
 layers.Dense(64, activation='relu'),
 layers.Dense(num_classes, activation='softmax') # 10 classes
])
# 4) COMPILE (loss + optimizer + metric)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
metrics=['accuracy'])
# 5) TRAIN (a few epochs to keep it quick)
model.fit(X_train, y_train, epochs=3, batch_size=128, verbose=1)
# 6) EVALUATE
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print(f"Test accuracy (2D CNN): {acc:.3f}")
# 7) PREDICT (one image)
probs = model.predict(X_test[:1], verbose=0)[0]
print("Predicted class:", np.argmax(probs), "| Probabilities:", np.round(probs, 3))