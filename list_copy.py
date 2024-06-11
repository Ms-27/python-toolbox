import copy

# do a shallow copy of a list:
#  new list but , elements remain the same objetcs
new_list = list[:]

# do a deepcopy of a list:
# new list with new elements
new_list = copy.deepcopy(list)
