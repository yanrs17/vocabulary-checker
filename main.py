import codecs

DECODING = 'utf-8'
ARTICLE_NAME = 'lin201'
LANGUAGE = 'en'
TOP_N = 10
# LEN_EACH_FREQ = 10
STRIPPED_LETTERS = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r1234567890"""

def get_word_to_freq(article, dictionary):
    
    file = codecs.open(article, 'r', DECODING)
    word_list = file.read().split()
    file.close()

    word_to_freq = {}
    for word in word_list:
        add_word_in_word_to_freq(word, word_to_freq)
    return word_to_freq

def add_word_in_word_to_freq(word, word_to_freq):
    word = word.lower().strip(STRIPPED_LETTERS)
    if word != '' and word not in vocab_list:
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

if __name__ == '__main__':
    article = 'article/{}_{}.txt'.format(ARTICLE_NAME, LANGUAGE)
    dictionary = 'dict/dict_{}.txt'.format(LANGUAGE)

    dict_read = codecs.open(dictionary, 'r', DECODING)
    vocab_list = dict_read.read().split()
    dict_read.close()

    word_to_freq = get_word_to_freq(article, dictionary)
    freq_to_word = get_freq_to_word(word_to_freq)
    show(freq_to_word)

    while True:
        dict_append = codecs.open('dict/dict_' + LANGUAGE + '.txt', 'a', 'utf-8')
        new_word = input('Input: ').strip()
        if new_word:
            dict_append.write(new_word)
            dict_append.write('\n')
        dict_append.close()
        print("=" * 100 + '\n')

        remove_word_in_freq_to_word(new_word, word_to_freq, freq_to_word)
        add_word_in_word_to_freq(new_word, word_to_freq)
        show(freq_to_word)