NLP Assignment Dimensionless

speech2text.py - uses Google Speech Recognition API to detect my voice file. (I used my own file because your file was not accessible). Google Speech Recognition API is the easiest because it does not require an API key.

nlu_model.py - NLU model trained with a dataset given in the folder using Rasa.

Execute the foll. in cmd before running the nlu_model.py file (admin permissions required)
pip install rasa_nlu
python -m rasa_nlu.server

pip install rasa_nlu[spacy]                             //For using spacy as backend
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en

Now the project should train the model and then it can accurately understand the intents and entities and classify them accordingly.


