# define your methods here.
# ex1() - ex10()
from pprint import *
def ex1():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},]   
    def sort_people(people_lst, field, asc_or_dsc):
        people_lst.sort(key=lambda p: p[field], reverse=True if asc_or_dsc == "desc" else False)
    sort_people(people_list, "weight","desc")
    pprint(people_list)
