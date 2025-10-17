import nltk
import os

nltk.download('punkt_tab')

if not os.path.isdir("response_usages_16k"):
    os.mkdir("response_usages_16k")