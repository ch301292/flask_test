def keyword_from_file(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r',encoding='utf-8').readlines()]  
    return stopwords
