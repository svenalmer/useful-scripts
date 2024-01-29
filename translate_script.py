import json
import re
import argparse
from deep_translator import GoogleTranslator
from deep_translator import MyMemoryTranslator

from tqdm import tqdm

"""
This script is used to translate inputs from input.json to all languages in the languages list and populate the localization files in your xcode project.
"""

LOCALIZE_PATH = "localization"

parser = argparse.ArgumentParser(description='Translate given input and populate swift localization files')
parser.add_argument('-r', '--replace', help='replace existing translations', action='store_true')

#List of language codes
languages = ['de', 'fr', 'el', 'hr', 'ro', 'sk', 'tr', 'am', 'iw', 'en', 'ar', 'ru', 'es', 'it'] #google translate
# languages = ['de-DE', 'fr-FR', 'el-GR', 'hr-HR', 'ro-RO', 'sk-SK', 'tr-TR', 'am-ET', 'he-IL', 'en-US', 'ar-SA', 'ru-RU', 'es-ES', 'it-IT'] # my memory translator

def sort_dict(d):
    new = {key:d[key] for key in sorted(d.keys())}
    return new

def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        json_content = file.read()
        cleaned_json = re.sub(r',\s*}', '}', json_content)
        data = json.loads(cleaned_json)
    return data

def write_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(sort_dict(data), file, ensure_ascii=False, indent=4)

replace_translations = vars(parser.parse_args())['replace']

input_data = read_json('input.json')
input_keys = input_data.keys()

if len(input_data) == 0:
    exit(0)

translator = GoogleTranslator(source='en', target='de')
# translator = MyMemoryTranslator(source='en-US', target='de-DE')

for lang in tqdm(languages):

    # GOOGLE TRANSLATE
    dest_filename = LOCALIZE_PATH + '/lang-' + (lang if lang!='iw' else 'he') + '.json'
    translator.target = lang

    # MYMEMORY TRANSLATE
    # dest_filename = 'localization/lang-' + lang.split('-')[0] + '.json'
    # translator.target = lang

    dest_data = read_json(dest_filename)
    dest_keys = dest_data.keys()

    for key in input_keys:
        translated = translator.translate(input_data[key])
        if replace_translations or key not in dest_keys:
            dest_data[key] = translated

    write_json(dest_filename, dest_data)

write_json('input.json', {})
