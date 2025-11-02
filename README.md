# Convolutional Neural Network Project (Hockey vs Tennis)
Prosjektet ble utviklet for å lære å anvende maskinlæring utover undervisningen på studiet. Prosjektet ga en dypere forståelse av hvordan man jobber med bildeklassifisering, datasett, dataforbehandling og Convolutional Neural Networks (CNN) ved hjelp av Python og TensorFlow/Keras. I tillegg til å være et spennende prosjekt, var det gøy å koble idretter jeg driver med, og har drevet med gjennom hele livet, med programmering for å se hvordan kunstig intelligens kan skille bilder med høy nøyaktighet.

# Funksjonalitet
Ved kjøring av main.py skjer følgende:
- Laster inn 1300+ forskjellige hockeybilder og tennisbilder fra mapper organisert i train/ og test/
- Utfører bildebehandling og dataforstørrelse (augmentation) med ImageDataGenerator
- Trener et Convolutional Neural Network (CNN) for å skille bildene.
- Visualiserer graf med matplotlib.
- Oppnåelse av over 95% nøyaktighet på testsettet.

# Hvordan kjøre

1.
cd HOCKEY-VS-TENNIS-CNN

python -m venv .venv

source .venv/bin/activate     # (Mac/Linux)

# .venv\Scripts\activate      # (Windows)

pip install -r requirements.txt

2.
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000

3.
cd webapp/cnnweb
mvn spring-boot:run

4.
Webappen starter på http://localhost:8080

# Bruk
1. Åpne nettleseren på http://localhost:8080

2. Last opp et bilde av enten ishockey eller tennis

3. Trykk på Klassifiser

# Mappestruktur

HOCKEY-VS-TENNIS-CNN/
├── app/                     # FastAPI-app som kjører prediksjonen
│   └── main.py
├── data/                    # Treningsdata og testdata
├── models/                  # Lagret modell
│   ├── model.h5
│   └── labels.json
├── images/                  # Treningskurver og visualiseringer
│   └── training_accuracy.png
├── webapp/cnnweb/           # Spring Boot-prosjektet
│   ├── src/
│   │   |- main/java/com/example/controller/PredictController.java
│   │   └── main/resources/
│   │       ├── templates/
│   │       │   └── upload.html
│   │       └── application.properties
│   └── pom.xml
├── requirements.txt         # Python-avhengigheter
├── README.md
└── LICENSE

**app/main/** -

**data/** – Inneholder mapper for train/ og test/ med hockeybilder og tennisbilder. Ca 80% i train og 20% i test.

**models/** - 

**images/** – Lagrede grafer fra treningsutførelse.

**webapp/cnnweb/src/** - 

**main.py** – Hovedfilen som håndterer lasting av data, modelltrening og evaluering.

**requirements.txt** – Liste over nødvendige Python-avhengigheter (TensorFlow, Matplotlib m.m.)

# Resultater
Etter 15 epoker oppnådde modellen 95% nøyaktighet på testsettet:
<img width="640" height="480" alt="training_accuracy" src="https://github.com/user-attachments/assets/8cad1678-fded-4f46-98c2-9e35ac4f007e" />
