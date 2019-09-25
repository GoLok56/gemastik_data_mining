from nltk.tokenize import TweetTokenizer

class Tokenizer:
  def __init__(self):
    self.tokenizer = TweetTokenizer()

  def tokenize(self, text):
    return self.tokenizer.tokenize(text)
