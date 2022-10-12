# Function for creating a list of random number of dicts
def create_list_of_dicts():
    import string
    import random
    result = []
    for i in range(random.randint(2, 10)):
        dict_size = random.randint(1, 26)
        keys = random.sample(string.ascii_lowercase, dict_size)
        values = (random.randint(1, 100) for j in range(dict_size))
        one_dict = dict(zip(keys, values))
        result.append(one_dict)
    return result


# Function for creating one common dict
def union_dicts_to_one_dict(all_dicts):
    current_dict_number = 0
    cnt = 0
    result = {}
    dicts_keys = []
    for one_dict in all_dicts:
        for dict_key in one_dict:
            dicts_keys.append(dict_key)

    for one_dict in all_dicts:
        current_dict_number += 1

        for dict_key in one_dict:
            dict_value = one_dict.get(dict_key)
            cnt = 0

            for i in dicts_keys:
                if dict_key == i:
                    cnt += 1

            if cnt == 1:
                result[dict_key] = dict_value
            elif cnt > 1:
                dict_key_num = dict_key + '_' + str(current_dict_number)
                dict_value_num = dict_value

                result[dict_key_num] = dict_value_num

    return result


# Function for ordering the dictionary by key values (in alphabetic order)
def order_dict_by_keys(dictionary):
    result = dict(sorted(dictionary.items()))
    return result


# Function for choosing max value for every alphabet letter
def get_dict_of_letters_with_max_value(one_dict):
    result = {}
    cnt = 0
    all_letters_from_dict = []

    for dict_key in one_dict:
        alphabet_letter = str(dict_key)[0]
        if alphabet_letter not in all_letters_from_dict:
            all_letters_from_dict.append(alphabet_letter)

    for k in all_letters_from_dict:
        max_dict_value = 0
        max_dict_key = 0

        for dict_key in one_dict:
            if dict_key[0] == k:
                if one_dict[dict_key] > max_dict_value:
                    max_dict_key = dict_key
                    max_dict_value = one_dict[dict_key]
            elif dict_key == k:
                result[dict_key] = one_dict[dict_key]

        result[max_dict_key] = max_dict_value

    return result


# PLEASE, NOTE:
# For verifying results you may uncomment the lines below

# random_dicts = create_list_of_dicts()
# print(random_dicts)

# common_dict = union_dicts_to_one_dict(random_dicts)
# print(common_dict)

# ordered_dict = order_dict_by_keys(common_dict)
# print(ordered_dict)

# dict_without_duplicates = get_dict_of_letters_with_max_value(ordered_dict)
# print(dict_without_duplicates)
