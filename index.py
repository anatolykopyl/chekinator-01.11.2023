import requests
import nltk

# Check if the required NLTK libraries are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def tag_to_group(tag):
    tag_groups = {
        'NN': 'Nouns',
        'NNP': 'Nouns',
        'NNPS': 'Nouns',
        'NNS': 'Nouns',
        'JJ': 'Adjectives',
        'JJR': 'Adjectives',
        'JJS': 'Adjectives',
        'VB': 'Verbs',
        'VBP': 'Verbs',
        'VBD': 'Verbs',
        'VBG': 'Verbs',
        'VBN': 'Verbs',
        'VBZ': 'Verbs',
        'RB': 'Adverbs',
        'RBR': 'Adverbs',
        'RBS': 'Adverbs',
        'IN': 'Interjections',
        'PRP': 'Prepositions',
        'PRPS': 'Prepositions',
        'DT': 'Determiners'
    }
    return tag_groups.get(tag, tag)

def sort_dictionary(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict

def count_speech_parts(text):
    words = nltk.word_tokenize(text)

    tagged_words = nltk.pos_tag(words)
  
    speech_parts_count = {}
  
    for word, tag in tagged_words:
        speech_part = tag_to_group(tag)

        if speech_part in speech_parts_count:
            speech_parts_count[speech_part] += 1
        else:
            speech_parts_count[speech_part] = 1
  
    return speech_parts_count

url = 'https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt'
response = requests.get(url)

if response.status_code == 200:
    sorted_speech_parts = sort_dictionary(count_speech_parts(response.text))
    top_five = sorted_speech_parts[:5]
    print(top_five)
else:
    print('Error:', response.status_code)
