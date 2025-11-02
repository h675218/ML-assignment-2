import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import matplotlib.pyplot as plt

img_size = (128, 128)  # setter en standardstørrelse som jeg vil ha alle bildene i
batch = 32             # antall bilder jeg ønsker i hver batch, 32 istedenfor å sende inn ett og ett bilde
epochs = 15            # antall runder vi ønsker å trene, epoker

# train_gen og test_gen er nesten helt like, men train_get har også augmentation for å lage variasjon i treningsbildene
train_gen = ImageDataGenerator(
    rescale=1./255, #får pikselverdier til å være [0,1]
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True
)

# faktiske testdata skal ikke trenes på, derfor kun endring av pikselverdier til [0,1]
test_gen = ImageDataGenerator(rescale=1./255)

train_ds = train_gen.flow_from_directory('data/train', target_size=img_size, batch_size=batch, class_mode='categorical'
)

test_ds = test_gen.flow_from_directory('data/test', target_size=img_size,batch_size=batch, class_mode='categorical'
)

print("Klassene:", train_ds.class_indices)

#CNN kode begynner her - sequential -> pipeline
model = Sequential([
    #convolution + pooling 1
    Conv2D(32, (3,3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D(2,2),

    #convolution + pooling 2
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    #klassifisering
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.3),      #forhindrer at modellen kun husker treningsbildene
    Dense(2, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

history = model.fit(
    train_ds,
    validation_data=test_ds,
    epochs=epochs #antall ganger vi går gjennom datasettet
)

#plotting for visuals med matplotlib
plt.plot(history.history['accuracy'], label='Train')
plt.plot(history.history['val_accuracy'], label='Test')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('images/training_accuracy.png')
#plt.show()

# --- Save model + labels ---
import os, json
os.makedirs("models", exist_ok=True)
model.save("models/model.h5")
labels = [None]*len(train_ds.class_indices)
for name, idx in train_ds.class_indices.items():
    labels[idx]=name
with open("models/labels.json","w") as f: json.dump(labels,f)
print("Saved models/model.h5 and models/labels.json")

plt.show()
