# Function for fixing "iz"
def replace_iz_with_is(text):
    result = text.capitalize().replace(' iz ', ' is ')
    return result


# Function for normalizing letter case in the text
def capitalize_first_letter(text):
    processed_text = text.capitalize().split(' ')
    cnt = 0
    for i in range(0, len(processed_text)):
        if processed_text[i] not in ['', ' ', '\n'] and cnt == 1:
            processed_text[i] = processed_text[i].capitalize()
            cnt = 0
        if processed_text[i].endswith(':\n') or processed_text[i].endswith('.') or processed_text[i].endswith('\n'):
            cnt = 1
    return ' '.join(processed_text)


# Function for creating sentence from the last words
def get_last_word_of_sentences(text):
    text = replace_iz_with_is(text)
    processed_text = text.capitalize().split(' ')
    result = ''
    for i in range(0, len(processed_text)):
        if processed_text[i].endswith(':\n') or processed_text[i].endswith('.') or processed_text[i].endswith('\n'):
            result += processed_text[i]
    result = result.replace('\n', '').replace('.', ' ').replace(':', ' ').replace('  ', ' ').strip() + '.'
    return result


# Function for executing fixing "iz", normalizing letter case and adding the new sentence to the end of text
def normalize_text(text):
    grammarly_correct_text = replace_iz_with_is(text)
    formatted_text = capitalize_first_letter(grammarly_correct_text)
    joint_sentence = get_last_word_of_sentences(text)
    result = formatted_text + ' ' + joint_sentence
    return result


# Function for counting spaces in the text
def count_spaces_in_text(text):
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

# corrected_text = replace_iz_with_is(input_text)
# print(corrected_text)

# capitalized_text = capitalize_first_letter(input_text)
# print(capitalized_text)

# test_sentence = get_last_word_of_sentences(input_text)
# print(test_sentence)

# formatted_output = normalize_text(input_text)
# print(formatted_output)

# total_spaces = count_spaces_in_text(input_text)
# print(total_spaces)
