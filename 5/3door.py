import numpy as np
from collections import Counter
car_list=np.random.randint(0, 3, size=1000)

def select_a_door():
    return np.random.randint(0, 3)

def open_a_door(car_pos,select_pos):
    list=[0,1,2]
    if car_pos==select_pos:
        list.remove(car_pos)
    else:
        list.remove(car_pos)
        list.remove(select_pos)
    return np.random.choice(list)

if __name__ == '__main__':

    no_change_success_record=list()
    change_success_record=list()
    select=list()
    for i in range(len(car_list)):
        select_door = select_a_door()
        open_door = open_a_door(car_list[i], select_door)
        no_change_success_record.append(select_door==car_list[i])
        list = [0, 1, 2]
        list.remove(select_door)
        list.remove(open_door)
        select_door=np.random.choice(list)
        change_success_record.append(select_door==car_list[i])
    print(Counter(no_change_success_record))
    print(Counter(change_success_record))





