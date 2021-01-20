from readability import Document
from requests import get
import bs4
import en_core_web_sm


# Instantiate global vars
nlp = en_core_web_sm.load()


# Function to grab text from the article body
def get_text(url):
    response = get(url)
    doc = Document(response.text)
    title = doc.title()
    summary = doc.summary()
    body = bs4.BeautifulSoup(summary, features="lxml").get_text()
    return f"{title} : {body}"


# Function to derive Named Entity Recognition (ner) with counts
def get_entities(text):
    doc = nlp(text)
    labels = [x.label_ for x in doc.ents]
    return labels


def get_entity_text(text, entity):
    doc = nlp(text)
    texts = [x.text for x in doc.ents if x.label_ == entity]
    return texts



