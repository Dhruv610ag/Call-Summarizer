#Generating the new folders directory 
mkdir -p src
mkdir -p testing_audios
mkdir  -p modules


# creating the files
touch src/__init__.py
touch src/helper.py
touch src/prompt.py
touch .env
touch setup.py
touch app.py
touch modules/audio_extractor.py
touch modules/embeddings.py
touch modules/summarizer.py
touch modules/sentiment_analyser.py
touch requirements.txt

echo "Directory and files made succesfully"
