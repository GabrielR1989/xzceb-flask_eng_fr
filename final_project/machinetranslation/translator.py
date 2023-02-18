'''
This module contains: Provision Watson Translation Service
a function english_to_french which takes in the english_text as a string
argument, in translator.py
a function french_to_english which takes in the french_text as a string
argument, in translator.py
Name: Gabriel Ricardo Erazo
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    '''
    Function that translates English text to French
    Name: Gabriel Ricardo Erazo
    '''
    french_text = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    return french_text.get('translations')[0].get('translation')

def french_to_english(french_text):
    '''
    Function that translates French text to  English
    Name: Gabriel Ricardo Erazo
    '''
    english_text = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    return english_text.get('translations')[0].get('translation')
    