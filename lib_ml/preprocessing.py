import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')

class Preprocessor:
    def __init__(self):
        # Initialize the Porter Stemmer
        self.ps = PorterStemmer()
        # Initialize the list of stopwords
        self.all_stopwords = stopwords.words('english')
        self.all_stopwords.remove('not')  # 'not' is not a stopword

    # this is what model training needs 
    def process(self, dataset):
        corpus = []
        for i in range(0, 900):
            corpus.append(self.process_item(dataset['Review'][i]))
        return corpus

    # this is what model service needs
    def process_item(self, item):
        review = re.sub('[^a-zA-Z]', ' ', item)
        review = review.lower()
        review = review.split()
        review = [self.ps.stem(word) for word in review if not word in set(self.all_stopwords)]
        review = ' '.join(review)
        return review