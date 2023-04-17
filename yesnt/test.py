import re
import string

def tokenize(line):

    clear_data = []

    tokenizer = re.compile(r'\w+')

    punctuations = [':/', ':)', '...', ':D', '<3', ':-)', ':(', ':-(', '—', '》', '>:(','?','.','!','-',',']
    for symbol in string.punctuation:
        punctuations.append(symbol)

    line = line.lower()

    # remove old style retweet text "RT"
    line = re.sub(r'^RT[\s]+', '', line)
    # remove hyperlinks
    line = re.sub(r'https?://[^\s\n\r]+', '', line)
    # remove hashtags
    # only removing the hash # sign from the word
    line = re.sub(r'#', '', line)

    #tokenizing sentences
    line_tokens = tokenizer.findall(line)
    

    
    for word in line_tokens:
        if (word == '' or word == ' '):
            pass
        else:
            clear_data.append(word)

    return " ".join(clear_data)


test_text = 'hə,   ola biler esLinde'
print(tokenize(test_text))