from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
import spacy

train_data = load_data('rasa_dataset.json')
#trainer = Trainer(config.load("config_spacy.yaml"))
Trainer.train(train_data)

model_directory = Trainer.persist('/models/')

nlp = spacy.load('en')
docx = nlp(u"I am looking for an Italian Restaurant where I can eat")
for word in docx.ents:
    print("value",word.text,"entity",word.label_,"start",word.start_char,"end",word.end_char)

