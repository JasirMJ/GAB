import nltk
from nltk.stem import WordNetLemmatizer
print("Starting installation ...")
nltk.download('popular', quiet=True) # for downloading popular packages
print("Completed Installation of Popular")
nltk.download('punkt')
print("Completed Installation of Punkt")
nltk.download('wordnet')
print("Completed Installation of Wordnet")