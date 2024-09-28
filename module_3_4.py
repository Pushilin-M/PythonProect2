
def single_root_words(root_word, *other_words):
    same_words = []
    r_words = [a.lower() for a in other_words]
    for j in range(len(r_words)):
        if root_word.lower() in r_words[j]:
            same_words.append(other_words[j])
    for i in range(len(r_words)):
        if r_words[i] in root_word.lower():
            same_words.append(other_words[i])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
