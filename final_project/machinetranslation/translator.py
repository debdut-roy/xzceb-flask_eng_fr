import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-12-23',
    authenticator=authenticator
)
language_translator.set_service_url(url)
# language_translator.set_disable_ssl_verification(True)

def englishToFrench(englishText):
    """
    This function translates English to French
    """
    french_translation = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    frenchText = french_translation.get('translations')[0].get('translation')
    return frenchText

def frenchToEnglish(frenchText):
    """
    This function translates French to English
    """
    english_translation = language_translator.translate(text=frenchText, model_id='en-fr').get_result()
    englishText = english_translation.get('translations')[0].get('translation')
    return englishText

print(englishToFrench('Hello'))