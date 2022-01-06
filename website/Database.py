import csv
import nltk
from nltk.util import pr

nltk.download('omw-1.4')

import firebase_admin

nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

from firebase_admin import credentials

from firebase_admin import db

cred = credentials.Certificate("website/key.json")

lemmatizer = WordNetLemmatizer()

url_key = open("website/api_key.txt").read()
firebase_admin.initialize_app(cred, {
    'databaseURL': url_key
})


# Client code will call this function when the dictionary of financial of terms and
# their respective definitions will need to be populated.
def read_data():
    term_list = []
    def_list = []

    ref = db.reference("/")

    snapshot = ref.get()
    for key, val in snapshot.items():
        term_list.append(lemmatizer.lemmatize(str(val.get('term')).lower()) + " : " + str(val.get('definition')))
        # def_list.append(str(val.get('definition')))

    # term_def_dict = {
    #     'terms': term_list,
    #     'definitions': def_list
    # }

    return term_list


# Client code will be able to add their own term(s) and definition(s) using this function
def add_term_def(term, definition):
    # url_key = open("website/api_key.txt").read()
    # firebase_admin.initialize_app(cred, {
    #     'databaseURL': url_key
    # })
    ref = db.reference("/")
    if term and definition:
        data_to_send = {
            'term': term,
            'definition': definition
        }

        ref.push(data_to_send)

