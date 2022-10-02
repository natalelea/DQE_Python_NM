# Copying the given text to a variable
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

# Please, uncomment the line below to verify the input (if necessary)
# print(input_text)

# 1.Making teat to lower case except the first letter.
# 2.Fixing "iz"
# 3.Splitting the whole text to separate words
c = input_text.capitalize().replace(' iz ', ' is ').split(' ')

# Creating empty or equal to 0 variables to store the further results
sent = ''
cnt = 0

# Creating a loop for every separate word of the splitted text
for i in range(0, len(c)):
    # Searching for first word of every sentence and turning its first letter to uppercase
    if c[i] not in ['', ' ', '\n'] and cnt == 1:
        c[i] = c[i].capitalize()
        cnt = 0
    # Searching for last word of every sentence and adding it to the variable
    if c[i].endswith(':\n') or c[i].endswith('.') or c[i].endswith('\n'):
        sent += c[i]
        cnt = 1

# Formatting the result sentence of all the last words
sent = sent.replace('\n', '').replace('.', ' ').replace(':', ' ').replace('  ', ' ').strip() + '.'

# Union of the previously formatted text and adding an extra sentence
output = ' '.join(c) + ' ' + sent

# Counting whitespaces in the input text
space_count = input_text.count(' ') + input_text.count('\n') + input_text.count('\t')

# Printing the results
print(f'{output} \n\n The number of whitespace characters in this text is {space_count}.')
