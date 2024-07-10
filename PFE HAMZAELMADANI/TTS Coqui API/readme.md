# Text-to-Speech Application
"""
This is a Flask application that uses the Coqui TTS (Text-to-Speech) API to convert text into speech.

The application has two routes:

1. `/addtext` (POST): This route accepts JSON data with a 'text' field. It replaces any abbreviations or incorrect words in the text with their correct forms, as specified in a dictionary loaded from 'dictionnaire.json'. It then uses the Coqui TTS API to convert the corrected text into speech, and saves the resulting audio file. The URL of the audio file is returned in the response.

2. `/static/<path:path>` (GET): This route serves static files from the 'static' directory.

The application uses the 'COQUI_TOS_AGREED' environment variable to indicate that the Coqui TTS terms of service have been agreed to.

The application can be run in debug mode by setting the 'FLASK_DEBUG' environment variable to 'True'.
"""

## material Requirements

Pour utiliser Coqui TTS sur un CPU, voici les exigences minimales :

Processeur (CPU): Un processeur multi-cœur moderne (Intel Core i5/i7(9th ou 10th gen) ou AMD équivalent).
RAM: Au moins 8 Go de RAM. Pour les modèles plus grands ou plus complexes, 16 Go de RAM ou plus peuvent être nécessaires.
Stockage: Un SSD pour des temps de chargement plus rapides et une meilleure performance générale. La taille de stockage dépendra du nombre de modèles et des données que vous utilisez, mais au moins 20 Go d'espace libre est recommandé.
Exigences minimales GPU
L'utilisation d'un GPU améliore considérablement les performances de la synthèse vocale, surtout pour les modèles plus grands et complexes. Voici les exigences minimales recommandées pour utiliser Coqui TTS avec un GPU :
Carte Graphique (GPU): Une carte graphique NVIDIA avec au moins 4 Go de VRAM. Par exemple, NVIDIA GTX 1060 Ti ou supérieure. Pour des performances optimales, des cartes comme la NVIDIA GTX 1660, RTX 2060 ou supérieures sont recommandées.
Drivers CUDA: CUDA Toolkit 10.1 ou supérieur et les drivers NVIDIA correspondants.
RAM: 16 Go de RAM pour s'assurer que le système peut gérer la charge de travail combinée du GPU et du CPU.
Stockage: Un SSD pour des temps de chargement plus rapides et une meilleure performance générale.
Exemple de Configuration Optimale
Pour des performances optimales, notamment pour des applications en temps réel ou pour des modèles de grande taille, voici une 

configuration recommandée :
Processeur (CPU): Intel Core i7/i9 ou AMD Ryzen 7/9.
Carte Graphique (GPU): NVIDIA RTX 3060 ou supérieure avec au moins 8 Go de VRAM.
RAM: 32 Go de RAM.
Stockage: SSD NVMe avec au moins 512 Go d'espace libre.

## Requirement needed 

pip installed 
python 3.11 or higher

### Installation
First, clone the repository

#### running the program Manually
secondly, switch to dev branch :

thirdly, you can install the requirement manually 

lastly, you run the app.py send the text in a json file in (http://localhost:5000/addtext)

```bash
1/ git clone http://34.245.246.163/si-digital-internes/tts-coqui.git

2/ git checkout dev

3/ pip install --no-cache-dir -r requirements.txt

4/ python app.py 

5/ streamlit run streamlit.py

```
#### running it using Docker Compose

1/build the app (the requirements will be installed automaticly) 
```bash
docker compose up --build -d
```

2/if the app doesnt start do the second command

```bash
docker compose up
```








