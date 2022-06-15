from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def english_to_french(text):
    """
    This function translates english to french
    """
    if text=="":
        return "null"
    
    url_lt='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/be85874b-7169-46e2-810e-ae031d4176cb'
    apikey_lt='NaUSQjavA7-xdWkAyuoYQbQHjq4fmwXjz2mTKCV22g5q'
    version_lt='2018-05-01'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    translation_response = language_translator.translate(text=text, model_id='en-fr').get_result()
    french_translation=translation_response['translations'][0]['translation']
    return french_translation

def english_to_german(text):
    
    """
    This function translates english to german
    """

    if text=="":
        return "null"
    
    url_lt='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/be85874b-7169-46e2-810e-ae031d4176cb'
    apikey_lt='NaUSQjavA7-xdWkAyuoYQbQHjq4fmwXjz2mTKCV22g5q'
    version_lt='2018-05-01'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    translation_response = language_translator.translate(text=text, model_id='en-de').get_result()
    german_translation=translation_response['translations'][0]['translation']
    return german_translation
