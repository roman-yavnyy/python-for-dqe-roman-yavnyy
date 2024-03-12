import random
import string
from collections import defaultdict
from random import *


# add function for dicts creation
def create_random_dicts():
    # create empty list
    list_of_dicts = []

    # randomize number of dicts
    for d in range(randint(2, 10)):
        # set size of dict
        size = randint(2, 10)
        # define key
        keys = sample(string.ascii_lowercase, size)
        # define value
        values = (randint(0, 100) for d in range(size))
        # create dict
        list_of_dicts = [{choice(string.ascii_lowercase): randrange(0, 99) for j in range(randrange(0, 25))}
                         for i in range(randrange(1, 9))]
    # return complete list
    return list_of_dicts


def combine_dicts(list_of_dicts):
    # create dict to store values and their dict occurrences for each key
    values_occurrences = defaultdict(list)

    # iterate through list of dicts,
    for idx, d in enumerate(list_of_dicts, start=1):
        # iterate through dict
        for key, value in d.items():
            # keep tracking values and their occurrences
            values_occurrences[key].append((value, idx))

    # create final dictionary
    final_dict = {}
    # iterate through dict with occurrences
    for key, values in values_occurrences.items():
        # find the value-occurrence pair with the highest value
        max_value, occurrence = max(values, key=lambda x: x[0])
        # rename the key based on the occurrence if the key appears in more than one dictionary
        new_key = f"{key}_{occurrence}" if len(values) > 1 else key
        # set value for key
        final_dict[new_key] = max_value
    return final_dict


# create list using function
dicts_list = create_random_dicts()
# print dict
print(dicts_list)
# display the final dictionary
combined_dict = combine_dicts(dicts_list)
print(combined_dict)
