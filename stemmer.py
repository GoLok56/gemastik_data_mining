from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class Stemmer:
  def __init__(self):
    self.stemmer = StemmerFactory().create_stemmer()

  def stem(self, text):
    return self.stemmer.stem(text)
