from statemachine import StateMachine
import random
import itertools

def valid_transitions(state, max_throw, multiplex_mode):
#multiplex mode 0 = no multiplexes
#multiplex mode n = max throws n 
#multiplex mode -1 = no in air collisions, 2 always valid

    state_list = list(state)

    num_throws = state_list.pop(0)

    while len(state_list) < max_throw:
        state_list.append(0)

    valid_throws = []
    
    if multiplex_mode == 0:
        for i in range(1,max_throw+1):
            if state_list[i-1] == 0:
                valid_throws.append(i)           
    elif multiplex_mode == -1:
        for i in range(1,max_throw+1):
            if state_list[i-1] == 0 or i == 2:
                valid_throws.append(i)                
    else:
        for i in range(1,max_throw+1):
            if int(state_list[i-1]) < multiplex_mode:
                valid_throws.append(i)            

    if num_throws == "0":
        return [0]
    elif num_throws == "1":
        return valid_throws
    else: 
        return itertools.combinations(valid_throws,num_throws)


if __name__ == "__main__":
    l = valid_transitions("11112",7,2)
    for i in l:
        print(i)
    
