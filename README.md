# Convolutional Neural Network Project (Hockey vs Tennis)
Prosjektet ble utviklet for å lære å anvende maskinlæring utover undervisningen på studiet. Prosjektet ga en dypere forståelse av hvordan man jobber med bildeklassifisering, datasett, dataforbehandling og Convolutional Neural Networks (CNN) ved hjelp av Python og TensorFlow/Keras. I tillegg til å være et spennende prosjekt, var det gøy å koble idretter jeg driver med, og har drevet med gjennom hele livet, med programmering for å se hvordan kunstig intelligens kan skille bilder med høy nøyaktighet.

# Funksjonalitet
Ved kjøring av main.py skjer følgende:
- Laster inn 1300+ forskjellige hockeybilder og tennisbilder fra mapper organisert i train/ og test/
- Utfører bildebehandling og dataforstørrelse (augmentation) med ImageDataGenerator
- Trener et Convolutional Neural Network (CNN) for å skille bildene.
- Starter en webapplikasjon for at en bruker selv skal kunne opplaste et bilde og skille mellom tennis og ishockey.
- Oppnåelse av over 95% nøyaktighet på testsettet.

# Hvordan kjøre
0. Video og prosjektrapport ligger som:
   Interaksjonsvideo Hockey-vs-Tennis.mov
   Prosjektrapport ML2 Assignment.pdf

2. 
cd HOCKEY-VS-TENNIS-CNN

python -m venv .venv

source .venv/bin/activate     # (Mac/Linux)

.venv\Scripts\activate      # (Windows)

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

**app/main/** - Inneholder main som definerer FastAPI for prediksjon. Den trente modellen lastes inn og tar imot bildeinput. 

**data/** – Inneholder mapper for train/ og test/ med hockeybilder og tennisbilder. Ca 80% i train og 20% i test.

**models/** - Lagrer trent modell model.h5 og etikettene labels.json som brukes til prediksjonen.

**images/** – Lagrede grafer fra treningsutførelse.

**webapp/cnnweb/src/** - Java Spring-frontend som lar brukeren laste opp bilder via webgrensesnittet. Inneholder kontrolleren PredictController.java og kjørbar applikasjons CnnWebApplication.java.

**main.py** – Hovedfilen som håndterer lasting av data, modelltrening og evaluering.

**requirements.txt** – Liste over nødvendige Python-avhengigheter (TensorFlow, Matplotlib m.m.)

# Resultater
Etter 15 epoker oppnådde modellen 95% nøyaktighet på testsettet:
<img width="640" height="480" alt="training_accuracy" src="https://github.com/user-attachments/assets/8cad1678-fded-4f46-98c2-9e35ac4f007e" />
