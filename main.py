import codecs
FILE_NAME = 'article/Le Petit Prince (fr).txt'
DICT_NAME = 'dict/dict_fr.txt'
LENGTH = 20

def show():

    file = codecs.open(FILE_NAME, 'r', 'utf-8')
    words = file.read().split()

    dict_read = codecs.open(DICT_NAME, 'r', 'utf-8')
    vocab = dict_read.read().split()

    ＃ Might want to distinguish "s" and "ed"
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
        words[i] = words[i].lower().strip("""!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r1234567890""")
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
        if len(word) > 10:
            word = word[0:9]
        print(frequency, word)

        length -= 1

if __name__ == '__main__':
    show()
    while True:
        dict_append = codecs.open(DICT_NAME, 'a', 'utf-8')
        dict_append.write(input('Input: '))
        dict_append.write('\n')
        dict_append.close()
        print("\n" * 100)
        show()
