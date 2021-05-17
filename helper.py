def is_isbn_or_key(word):
    '''
    :param word:
    :return: isbin判断
    '''
    # isbin13  13个0-9数字
    # isbin10  10个0-9数字，包含'-'
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
