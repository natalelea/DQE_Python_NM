# Function for fixing "iz"
def grammar_replace(text):
    result = text.replace(' iz ', ' is ')
    return result


# Function for normalizing letter case in the text
def capitalizing(text):
    c = text.capitalize().split(' ')
    cnt = 0
    for i in range(0, len(c)):
        if c[i] not in ['', ' ', '\n'] and cnt == 1:
            c[i] = c[i].capitalize()
            cnt = 0
        if c[i].endswith(':\n') or c[i].endswith('.') or c[i].endswith('\n'):
            cnt = 1
    return ' '.join(c)


# Function for creating sentence from the last words
def sentence_creation(text):
    text = grammar_replace(text)
    c = text.capitalize().split(' ')
    sent = ''
    cnt = 0
    for i in range(0, len(c)):
        if c[i].endswith(':\n') or c[i].endswith('.') or c[i].endswith('\n'):
            sent += c[i]
            cnt = 1
    sent = sent.replace('\n', '').replace('.', ' ').replace(':', ' ').replace('  ', ' ').strip() + '.'
    return sent


# Function for executing fixing "iz", normalizing letter case and adding the new sentence to the end of text
def text_union(text):
    corrected_grammar = grammar_replace(text)
    formatted_text = capitalizing(corrected_grammar)
    sentence = sentence_creation(text)
    result = formatted_text + ' ' + sentence
    return result


# Function for counting spaces in the text
def space_count(text):
    result = text.count(' ') + text.count('\n') + text.count('\t')
    return f'The number of whitespace characters in this text is {result}.'


input_text = 'homEwork:\n  ' \
             'tHis iz your homeWork, copy these Text to variable.\n\n  ' \
             '' \
             'You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE ' \
             'senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.' \
             '' \
             '\n\n  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.\n\n  ' \
             '' \
             'last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ' \
             'ALL whitespaces. I got 87.'


# PLEASE, NOTE:
# For verifying results you may uncomment the lines below

# corrected_text = grammar_replace(input_text)
# print(corrected_text)

# capitalized_text = capitalizing(input_text)
# print(capitalized_text)

# test_sentence = sentence_creation(input_text)
# print(test_sentence)

# formatted_output = text_union(input_text)
# print(formatted_output)

# total_spaces = space_count(input_text)
# print(total_spaces)