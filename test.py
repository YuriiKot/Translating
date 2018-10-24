

from google.cloud import translate
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./Translation-f071deb87e85.json"



# Instantiates a client
translate_client = translate.Client()

# The text to translate
# text = u'Ich möchte es haben, weil mein Onkel es zum Geburtstag hatte.'
text = u'Der dritte Punkt ist vielleicht, dass wir wirklich froh sein können, in einer Demokratie zu leben, denn sicherlich machen Russland und China genau das Gleiche, aber keiner spricht darüber, weil das niemand machen kann.'
# The target language
source = 'de'
target = 'uk'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    source_language  = source,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))
# /Users/admin/Downloads/Translation-f071deb87e85.json
