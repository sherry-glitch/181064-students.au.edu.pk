import operator


def count(article):
    words = article.split()
    word_count = len(words)
    dist_word = {}
    for word in words:
        if word in dist_word:
            dist_word[word] += 1
        else:
            dist_word[word] = 1
    var_dict = sorted(dist_word.items(), key=operator.itemgetter(1), reverse=True)
    return var_dict, word_count
