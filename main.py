import codecs

DECODING = 'utf-8'
ARTICLE_NAME = 'Le_Petit_Prince'
LANGUAGE = 'fr'
LENGTH = 20
LENGTH_OF_EACH_FREQ = 10
STRIPPED_LETTERS = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r1234567890"""

def show():

    file = codecs.open('article/' + ARTICLE_NAME + '_' + LANGUAGE + '.txt', 'r', DECODING)
    words = file.read().split()

    dict_read = codecs.open('dict/dict_' + LANGUAGE + '.txt', 'r', DECODING)
    vocab = dict_read.read().split()

    # Might want to distinguish "s" and "ed"
    # vocab_new = vocab[:]
    # suffixes = ['s', 'ed']
    # for suffix in suffixes:
    #     vocab_with_suffix = vocab_new[:]
    #     for i in range(len(vocab_with_suffix)):
    #         vocab_with_suffix[i] += suffix
    #     vocab.extend(vocab_with_suffix)
    #
    # print(vocab)


    word_to_freq = {}
    for i in range(len(words)):
        words[i] = words[i].lower().strip(STRIPPED_LETTERS)
        if words[i] != '' and words[i] not in vocab:
            if words[i] not in word_to_freq:
                word_to_freq[words[i]] = 0
            word_to_freq[words[i]] += 1

    freq_to_word = {}
    for word in word_to_freq:
        if word_to_freq[word] not in freq_to_word:
            freq_to_word[word_to_freq[word]] = []
        freq_to_word[word_to_freq[word]].append(word)

    freq = []
    for frequency in freq_to_word:
        freq.append(frequency)
    freq.sort()

    file.close()
    dict_read.close()

    frequency = freq.pop()
    print(frequency, freq_to_word[frequency])
    length = LENGTH - 1
    while length != 0 and len(freq) != 0:
        frequency = freq.pop()
        word = freq_to_word[frequency]
        if len(word) > LENGTH_OF_EACH_FREQ:
            word = word[0:LENGTH_OF_EACH_FREQ-1]
        print(frequency, word)

        length -= 1

if __name__ == '__main__':
    show()
    while True:
        dict_append = codecs.open('dict/dict_' + LANGUAGE + '.txt', 'a', 'utf-8')
        added = input('Input: ')
        added = added.strip()
        if (added):
            dict_append.write(added)
            dict_append.write('\n')
        dict_append.close()
        print("\n" * 100)
        show()
