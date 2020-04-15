# todo:
# 1. remove punctuation from joke and response_without_stopwords
# 2. rename doc, token, lexicon variables
# 3. add sentiment analysis

import copy, math, nltk
from collections import Counter
from nltk.tokenize import TreebankWordTokenizer
from collections import OrderedDict
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
# nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')


def cosine_sim(query_vec, joke_tf_tdf_vec):
    """
    Since our vectors are dictionaries, lets convert them to lists for easier mathing.
    """
    query_vec = [val for val in query_vec.values()]
    joke_tf_tdf_vec = [val for val in joke_tf_tdf_vec.values()]

    dot_prod = 0
    for i, v in enumerate(query_vec):
        dot_prod += v * joke_tf_tdf_vec[i]

    mag_1 = math.sqrt(sum([x ** 2 for x in query_vec]))
    mag_2 = math.sqrt(sum([x ** 2 for x in joke_tf_tdf_vec]))

    if (mag_1 * mag_2) > 0:
        return dot_prod / (mag_1 * mag_2)
    else:
        return 0


def remove_stopwords(doc):
    stop_words.extend([',', '.', '--', '-', '!', '?', ':', ';', '``', "''", '(', ')', '[', ']'])
    doc_words = TreebankWordTokenizer().tokenize(doc)
    doc_without_stopwords = [word for word in doc_words if word not in stop_words]
    return ' '.join(doc_without_stopwords)


def joke_response_analyzer(joke, response):
    joke2 = 'Did you hear about the scientist who was lab partners with a pot of boiling water? He had a very esteemed colleague.'
    joke3 = 'What do you call a fly without wings? A walk.'
    joke4 = 'When my wife told me to stop impersonating a flamingo, I had to put my foot down.'
    joke5 = 'What do you call someone with no nose? Nobody knows.'
    joke6 = 'What time did the man go to the dentist? Tooth hurt-y.'
    joke7 = 'Why can’t you hear a pterodactyl go to the bathroom? The p is silent.'
    joke8 = 'How many optometrists does it take to change a light bulb? 1 or 2? 1... or 2?'

    joke_without_stopwords = remove_stopwords(joke.lower())
    response_without_stopwords = remove_stopwords(response.lower())
    second_joke_without_stopwords = remove_stopwords(joke2.lower())
    third_joke_without_stopwords = remove_stopwords(joke3.lower())
    fourth_joke_without_stopwords = remove_stopwords(joke4.lower())
    fifth_joke_without_stopwords = remove_stopwords(joke5.lower())
    sixth_joke_without_stopwords = remove_stopwords(joke6.lower())
    seventh_joke_without_stopwords = remove_stopwords(joke7.lower())
    eighth_joke_without_stopwords = remove_stopwords(joke8.lower())

    documents = [joke_without_stopwords, second_joke_without_stopwords, third_joke_without_stopwords,
                 fourth_joke_without_stopwords, fifth_joke_without_stopwords, sixth_joke_without_stopwords,
                 seventh_joke_without_stopwords, eighth_joke_without_stopwords]

    tokenizer = TreebankWordTokenizer()
    token1 = tokenizer.tokenize(joke_without_stopwords)
    token2 = tokenizer.tokenize(second_joke_without_stopwords)
    token3 = tokenizer.tokenize(third_joke_without_stopwords)
    token4 = tokenizer.tokenize(fourth_joke_without_stopwords)
    token5 = tokenizer.tokenize(fifth_joke_without_stopwords)
    token6 = tokenizer.tokenize(sixth_joke_without_stopwords)
    token7 = tokenizer.tokenize(seventh_joke_without_stopwords)
    token8 = tokenizer.tokenize(eighth_joke_without_stopwords)
    tokens = token1 + token2 + token3 + token4 + token5 + token6 + token7 + token8
    lexicon = set(tokens)
    vector_template = OrderedDict((token, 0) for token in lexicon)

    document_tfidf_vectors = []

    for doc in documents:

        vec = copy.copy(
            vector_template)  # So we are dealing with new objects, not multiple references to the same object

        tokens = tokenizer.tokenize(doc.lower())
        token_counts = Counter(tokens)
        print(token_counts)
        lexicon = set(tokens)

        for key, value in token_counts.items():
            docs_containing_key = 0
            for _doc in documents:
                if key in _doc:
                    docs_containing_key += 1
            term_frequency = value / len(lexicon)
            if docs_containing_key:
                inverse_document_frequency = len(documents) / docs_containing_key
            else:
                inverse_document_frequency = 0
            vec[key] = term_frequency * inverse_document_frequency
        document_tfidf_vectors.append(vec)

    query = response_without_stopwords.lower()
    query_vec = copy.copy(
        vector_template)  # So we are dealing with new objects, not multiple references to the same object

    query_tokens = tokenizer.tokenize(query.lower())
    query_token_counts = Counter(query_tokens)

    for query_word, value in query_token_counts.items():
        docs_containing_key = 0
        for _doc in documents:
            if query_word in _doc.lower():
                docs_containing_key += 1
        if docs_containing_key == 0:
            continue
        term_frequency = value / len(query_tokens)
        inverse_document_frequency = len(documents) / docs_containing_key
        query_vec[query_word] = term_frequency * inverse_document_frequency
    relevance = cosine_sim(query_vec, document_tfidf_vectors[0])
    return relevance
