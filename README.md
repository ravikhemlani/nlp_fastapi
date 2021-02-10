# NLP Web Service API
A simple web service that performs the following API services: 
- entity extraction on text body of URLs
- storing of results into a database
- retrieve entities from database
- retrieve texts from a provided entity

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

## Setup Instructions
- py -m venv venv
- venv\Scripts\activate.bat
- python -m pip install --upgrade pip setuptools wheel
- pip install -r requirements.txt
- python -m spacy download en_core_web_sm
