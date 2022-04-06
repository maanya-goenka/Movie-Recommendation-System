from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import movieScraper

def tfidf_cosine():
    # creating the tf-idf vector
    tfidf = TfidfVectorizer(stop_words = "english")
    # recommendations are based on the movie genres
    #tfidfMatrix1 = tfidf.fit_transform(movieScraper.extractWeb()["Genre"])
    tfidfMatrix2 = tfidf.fit_transform(movieScraper.imdbExtraction()["Features"])
    #print(list(enumerate(tfidf.get_feature_names())))
    #tfidfMatrix1.shape
    tfidfMatrix2.shape
    #cosineSimilarityMatrix1 = linear_kernel(tfidfMatrix1, tfidfMatrix1)
    cosineSimilarityMatrix2 = linear_kernel(tfidfMatrix2, tfidfMatrix2)
    #return cosineSimilarityMatrix1
    return cosineSimilarityMatrix2