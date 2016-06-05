import codecs

def clean_up(s):
    return s.lower().strip("""!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r""")



if __name__ == '__main__':
    file = codecs.open('VC.txt', 'r', 'utf-8')
    dic = file.read().split()
    count = {}
    for i in range(len(dic)):
        dic[i] = clean_up(dic[i])
        if dic[i] not in count:
            count[dic[i]] = 0
        count[dic[i]] += 1
    
    k = 0
    max = 1000000000000000000
    lst = []
    while k < 100 and max != 0:
        j = 0
        for word in count:
            #max_word = ''
            if count[word] > j and count[word] <= max and word not in lst:
                j = count[word]
                max_word = word
                lst.append(max_word)

        if max != 0:
            print(k + 1, max_word ,j)           
        k += 1
        max = j     
    #print(count) 