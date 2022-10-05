# Function for creating a list of random number of dicts
def dict_list_creation():
    import string
    import random
    result = []
    for i in range(random.randint(2, 10)):
        size = random.randint(1, 26)
        keys = random.sample(string.ascii_lowercase, size)
        values = (random.randint(1, 100) for j in range(size))
        one_dict = dict(zip(keys, values))
        result.append(one_dict)
    return result


# Function for creating one common dict
def dicts_union():
    dict_number = 0
    cnt = 0
    lst = []
    result = {}
    all_dicts = dict_list_creation()

    for one_dict in all_dicts:
        for dict_value in one_dict:
            lst.append(dict_value)

    for one_dict in all_dicts:
        dict_number += 1

        for dict_key in one_dict:
            dict_value = one_dict.get(dict_key)
            cnt = 0

            for i in lst:
                if dict_key == i:
                    cnt += 1
            if cnt == 1:
                result[dict_key] = dict_value
            elif cnt > 1:
                dict_key_num = dict_key + '_' + str(dict_number)
                dict_value_num = dict_value

                result[dict_key_num] = dict_value_num

                for k in range(1, dict_number):
                    dict_key_seq = dict_key + '_' + str(k)

                    if dict_key_seq in result:
                        dict_value_seq = result[dict_key_seq]

                        if dict_value_seq < dict_value_num:
                            result.pop(dict_key_seq)
                        elif dict_value_seq >= dict_value_num:
                            result.pop(dict_key_num)
    return result


# Function for ordering the dictionary by key values (in alphabetic order)
def dict_ordering(dictionary):
    result = dict(sorted(dictionary.items()))
    return result


# PLEASE, NOTE:
# For verifying results you may uncomment the lines below

# random_dicts = dict_list_creation()
# print(random_dicts)

# common_dict = dicts_union()
# print(common_dict)

# common_dict = dicts_union()
# ordered_common_dict = dict_ordering(common_dict)
# print(common_dict)
# print(ordered_common_dict)
