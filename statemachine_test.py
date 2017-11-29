from statemachine import StateMachine

def s_111_transitions(throws):
    throw = throws[0]
    throws = throws[1:]
    newState = "000"
    if throw == "3":
        newState = "111"
    elif throw == "4":
        newState = "1101"
    elif throw == "5":
        newState = "11001"

    return(newState, throws)

def s_1101_transitions(throws):
    throw = throws[0]
    throws = throws[1:]
    newState = "000"
    if throw == "2":
        newState = "111"
    
    return(newState, throws)
    

if __name__ == "__main__":
    m = StateMachine()
    m.add_state("111", s_111_transitions)
    m.add_state("1101", s_1101_transitions)
    m.set_start("111")
    m.run("42",2)
    m.run("423",3)
