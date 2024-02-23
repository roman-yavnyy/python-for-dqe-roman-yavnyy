# import lib with needed functions
import random

# create list of 100 random numbers from 0 to 1000
# using sample method that returns a list of 100 elements in range between 0 and 1000
random_list = random.sample(range(0, 1000), 100)

# sort list from min to max (without using sort())
# go through each element of list
for i in range(len(random_list)):
    # add another loop for comparison 2 neighboring elements
    for j in range(len(random_list) - i - 1):
        # compare elements
        if random_list[j] > random_list[j + 1]:
            # swap elements is they are not in order
            # add temp variable for storing element with higher value that will be swapped
            temp = random_list[j]
            # rewrite higher value with lower neighbor
            random_list[j] = random_list[j + 1]
            # write higher value from temp to next element
            random_list[j + 1] = temp

# print result
print(f"sorted list: {random_list}")

# calculate average for even and odd numbers
# add list with only even numbers
even_list = []
# add list with only odd numbers
odd_list = []
# add even numbers to the list
# loop through whole list
for i in random_list:
    # if remainder after division by 2 is zero - then even
    if i % 2 == 0:
        # add element to even list
        even_list.append(i)
    # in other case
    else:
        # add element to odd list
        odd_list.append(i)

# calculate even average. sum of elements divided by number of elements
even_average = sum(even_list) / len(even_list)
# same for odd numbers
odd_average = sum(odd_list) / len(odd_list)

# print even average
print(f"average for even numbers: {even_average}")
# print odd average
print(f"average for odd numbers: {odd_average}")
