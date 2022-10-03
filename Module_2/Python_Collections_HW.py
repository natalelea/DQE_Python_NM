# Function from the following library is necessary for generating random letters
import string
# Function from the following library is necessary for generating random numbers
import random

# Create empty list to store the further results
all_dicts = []

# Populating list with random number of dictionaries
for i in range(random.randint(2, 10)):
    # Getting random dictionary size
    size = random.randint(1, 26)
    # Getting random letters as keys
    keys = random.sample(string.ascii_lowercase, size)
    # Getting random numbers as values
    values = (random.randint(1, 100) for j in range(size))
    # Creating dicts and adding them to general list
    oneDict = dict(zip(keys, values))
    all_dicts.append(oneDict)

# Create empty or equal to 0 variables to store the further results
result = dict()
dict_number = 0
cnt = 0
ls = []

# Creating list of all dicts' keys
for one_dict in all_dicts:
    for dict_value in one_dict:
        ls.append(dict_value)

# Loop for each dict from the list
for one_dict in all_dicts:
    # Incrementing number of current dict
    dict_number += 1

    # Loop for each key from the dict
    for dict_key in one_dict:

        # Getting value for the separate key
        dict_value = one_dict.get(dict_key)

        # Counting if this key repeats more than once in all the dicts
        cnt = 0
        for i in ls:
            if dict_key == i:
                cnt += 1

        # Adding current key without "_<number>" if it is unique
        if cnt == 1:
            result[dict_key] = dict_value
        # Creating current dict value and key with "_<number>"
        elif cnt > 1:
            dict_key_num = dict_key + '_' + str(dict_number)
            dict_value_num = dict_value

            # Adding new element to the result dict (anyway)
            result[dict_key_num] = dict_value_num

            # Loop for verifying values of the same key from the start of result list untill current element
            for k in range(1, dict_number):
                dict_key_seq = dict_key + '_' + str(k)

                # Checking if key with such a number already exist (if no -> go to next number)
                if dict_key_seq in result:
                    dict_value_seq = result[dict_key_seq]

                    # Comparison of values for same dict keys and different values
                    # Removing the pairs that have not maximum value
                    if dict_value_seq < dict_value_num:
                        result.pop(dict_key_seq)
                    elif dict_value_seq >= dict_value_num:
                        result.pop(dict_key_num)

# Printing the results
print(result)
