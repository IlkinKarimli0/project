import nltk                                
import re                                  # library for regular expression operations
import string                              # for string operations

from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.tokenize import TweetTokenizer   # module for tokenizing strings

#nltk.download('stopwords')



def tokenize(line):

    clear_data = []

    # az_stopwords = stopwords.words('azerbaijani')
    # az_stopwords.remove('a')

    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)

    punctuations = [':/', ':)', '...', ':D', '<3', ':-)', ':(', ':-(', '—', '》', '>:(','?','.','!','-',',']
    for symbol in string.punctuation:
        punctuations.append(symbol)



    
    # remove old style retweet text "RT"
    line = re.sub(r'^RT[\s]+', '', line)
    # remove hyperlinks
    line = re.sub(r'https?://[^\s\n\r]+', '', line)
    # remove hashtags
    # only removing the hash # sign from the word
    line = re.sub(r'#', '', line)

    #tokenizing sentences
    line_tokens = tokenizer.tokenize(line)
    

    
    for word in line_tokens:
        if (word == '' or word == ' '):
            pass
        else:
            clear_data.append(word)

    return " ".join(clear_data)


# test_text = 'hə'
# print(tokenize(test_text))
