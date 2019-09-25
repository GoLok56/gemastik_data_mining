import re

class Preprocess:
  def __init__(self, text, tokenizer, stemmer, stop_words=None, slang_words=None, base_words=None):
    self.text = text
    self.stop_words = stop_words
    self.tokenizer = tokenizer
    self.stemmer = stemmer
    self.slang_words = slang_words
    self.base_words = base_words
    self.preprocess()

  def preprocess(self):
    self.case_fold()
    self.clean()
    self.slang_word_correction()
    self.stem()
    self.tokenize()
    self.remove_stop_words()
    self.base_words_check()

  def case_fold(self):
    self.text = self.text.lower()

  def clean(self):
    self.text = re.sub(r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', '', self.text)  # URLs
    self.text = re.sub(r'(?:\#+[\w_]+[\w\'_\-]*[\w_]+)', '', self.text)  # Hashtag
    self.text = re.sub(r'(?:@[\w_]+)', '', self.text)  # Mention
    self.text = re.sub(r'[^\x00-\x7F]+', '', self.text)  # Unicode
    self.text = re.sub(r'rt', '', self.text)  # Retweet
    self.text = re.sub(r'(?:[:=;][oO\-]?[D\)\]\(\]/\\OpP])', '', self.text)  # Emoticon
    self.text = re.sub(r'(?:(?:\d+,?)+(?:\.?\d+)?)', '', self.text)  # Special Char
    self.text = re.sub(r'[\n\t\r]+', '', self.text) # Remove linebreak, tab, return

  def slang_word_correction(self):
    if self.slang_words:
        pattern = re.compile(r'\b(' + '|'.join(self.slang_words.keys()) + r')\b')
        self.text = pattern.sub(lambda x: self.slang_words[x.group()], self.text)

  def stem(self):
    self.text = self.stemmer.stem(self.text)    

  def tokenize(self):
    self.tokens = self.tokenizer.tokenize(self.text)

  def remove_stop_words(self):
    if self.stop_words:
        self.tokens = [word for word in self.tokens if word not in self.stop_words]
        self.text = ' '.join(self.tokens)
    
  def base_words_check(self):
    if self.base_words:
        self.tokens = [word for word in self.tokens if word in self.base_words]
        self.text = ' '.join(self.tokens)