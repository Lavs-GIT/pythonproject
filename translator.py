def english_to_french()

from ibm_watson import LanguageTranslatorV3
url_lt='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/be85874b-7169-46e2-810e-ae031d4176cb'
apikey_lt='NaUSQjavA7-xdWkAyuoYQbQHjq4fmwXjz2mTKCV22g5q'
version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

from pandas import json_normalize
json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

French_translation=language_translator.translate(text=translation_eng , model_id='en-fr').get_result()
French_translation['translations'][0]['translation']

def english_to_german()

German_translation=language_translator.translate(text=translation_eng , model_id='en-de').get_result()
German_translation['translations'][0]['translation']
