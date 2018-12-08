import codecs
import string

DECODING = 'utf-8'
STRIPPED_LETTERS = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r1234567890"""
PATH_ARTICLE = 'article/{}_{}.txt'
PATH_DICT = 'dict/dict_{}.txt'

def get_word_to_freq(article, dictionary):
    
    file = codecs.open(article, 'r', DECODING)
    word_list = file.read().split()
    file.close()

    word_to_freq = {}
    for word in word_list:
        add_word_in_word_to_freq(word, word_to_freq)
    return word_to_freq

def process_word(word):
    # English version
    word = word.strip(STRIPPED_LETTERS)
    if len(word) > 0 and word[0] not in string.ascii_lowercase:
        return None
    if len(word) > 4 and word[:4] == 'http':
        return None
    while '’' in word:
        word = word.replace('’', "'")
    while '¡' in word:
        word = word.replace('¡', 'ff')
    if len(word) > 2 and word[-2:] == "'s":
        word = word[:-2]
    return word

def add_word_in_word_to_freq(word, word_to_freq):
    
    word = process_word(word)
    if word and word not in vocab_list:
        if word not in word_to_freq:
            word_to_freq[word] = 0
        word_to_freq[word] += 1

def get_freq_to_word(word_to_freq):
    freq_to_word = {}
    for word in word_to_freq:
        if word_to_freq[word] not in freq_to_word:
            freq_to_word[word_to_freq[word]] = []
        freq_to_word[word_to_freq[word]].append(word)
    return freq_to_word

def remove_word_in_freq_to_word(word, word_to_freq, freq_to_word):
    cur_word = word_to_freq[word]
    if cur_word in freq_to_word:
        freq_to_word[cur_word].remove(word)
        if len(freq_to_word[cur_word]) == 0:
            del freq_to_word[cur_word]

def show(freq_to_word):
    freq_list = list(freq_to_word.keys())
    freq_list.sort()
    list_len = len(freq_list)

    for freq in freq_list[list_len-TOP_N: list_len]:
        print(freq, freq_to_word[freq])

def get_new_word(dictionary):
    dict_append = codecs.open(dictionary, 'a', 'utf-8')
    new_word = input('Input: ').strip()
    if new_word:
        dict_append.write(new_word)
        dict_append.write('\n')
        print("=" * 100 + '\n')
    dict_append.close()
    return new_word

if __name__ == '__main__':

    ARTICLE_NAME = 'ast101'
    LANGUAGE = 'en'
    TOP_N = 20

    article = PATH_ARTICLE.format(ARTICLE_NAME, LANGUAGE)
    dictionary = PATH_DICT.format(LANGUAGE)

    dict_read = codecs.open(dictionary, 'r', DECODING)
    vocab_list = dict_read.read().split()
    dict_read.close()

    word_to_freq = get_word_to_freq(article, dictionary)
    freq_to_word = get_freq_to_word(word_to_freq)
    show(freq_to_word)

    while True:
        new_word = get_new_word(dictionary)
        if new_word:
            remove_word_in_freq_to_word(new_word, word_to_freq, freq_to_word)
            add_word_in_word_to_freq(new_word, word_to_freq)
            show(freq_to_word)