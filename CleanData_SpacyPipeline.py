import spacy


def clean_text_nlp(X, is_lemma=True, remove_stop=True, is_alphabetic=True):
    """
    X : list of string such as ["sentence_1", "sentences_2", ... , "sentence_n"]

    Return : list of list of words 
    [
        ["word_1", "word_2", ... , "word_n"], (sentence 1 cleaned)
        ["word_1", "word_2", ... , "word_n"],
        .
        .
        .
        ["word_1", "word_2", ... , "word_n"] (sentence n cleaned)
    ]

    """
    nlp = spacy.load("en_core_web_sm")
    # (is_lemma = True, remove_stop = True, is_alpha = False) = (1,1,0)
    is_lemma = True
    remove_stop = False
    is_alphabetic = True
    hyperparam_tuple = (is_lemma, remove_stop, is_alphabetic)
    new_X = []
    while(True):
        if((0,0,0)==hyperparam_tuple): # everything initialize with False
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                doc = [token.text.lower() for token in doc if(not(token.is_left_punct) and not(token.is_right_punct) and not(token.is_punct) and not(token.is_bracket))]
                new_X.append(doc)
            break
        elif((1,0,0)==hyperparam_tuple): # lemma_
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                doc = [token.lemma_.lower() for token in doc if(not(token.is_left_punct) and not(token.is_right_punct) and not(token.is_punct) and not(token.is_bracket))]
                new_X.append(doc)
            break
        elif((0,1,0)==hyperparam_tuple): # remove stop_words
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                doc = [token.text.lower() for token in doc if (not(token.is_stop) and not(token.is_left_punct) and not(token.is_right_punct) and not(token.is_punct) and not(token.is_bracket))]
                new_X.append(doc)
            break
        elif((0,0,1)==hyperparam_tuple): # only alphabetic
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                doc = [token.text.lower() for token in doc if (token.is_alpha and not(token.is_left_punct))]
                new_X.append(doc)
            break
        elif((1,1,0)==hyperparam_tuple): #lemma and remove stop_words
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                doc = [token.lemma_.lower() for token in doc if (not(token.is_stop) and not(token.is_left_punct) and not(token.is_right_punct) and not(token.is_punct) and not(token.is_bracket))]
                new_X.append(doc)
            break
        elif((0,1,1)==hyperparam_tuple): #remove stop_words and only alphabetic
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                doc = [token.text.lower() for token in doc if (token.is_alpha and not(token.is_stop))]
                new_X.append(doc)
            break
        elif((1,0,1)==hyperparam_tuple): #lemma and only alphabetic
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                doc = [token.lemma_.lower() for token in doc if(token.is_alpha and not(token.is_left_punct))]
                new_X.append(doc)
            break
        elif((1,1,1)==hyperparam_tuple): #lemma and only alphabetic and remove stop_words
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                doc = [token.lemma_.lower() for token in doc if(token.is_alpha and not(token.is_stop))]
                new_X.append(doc)
            break
        break
    
    return new_X
