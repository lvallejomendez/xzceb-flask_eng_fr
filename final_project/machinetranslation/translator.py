"""Language Translator with IBM Watson"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    This function translates english to french
    """
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']

    return french_text


def french_to_english(french_text):
    """
    This function translates french to english
    """
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']

    return english_text
