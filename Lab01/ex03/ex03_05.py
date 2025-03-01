def WordCount(words):
    word_count = {}
    for word in words:
        word = word.lstrip().rstrip()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

sentence = input("Nhập một câu: ")
words = sentence.split(',')
print(WordCount(words))