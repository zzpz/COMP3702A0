class A0:
    pass

class State():



    state: str

    def __init__(self,state_string):
        try:
            self.state = state_string
        except:
            self.state = "12345678_"

    def __str__(self):
        return self.state


def swap(s, i, j):
        lst = list(s)
        lst[i], lst[j] = lst[j], lst[i]
        return ''.join(lst)


class Transition():
    ## setup callback functions


    def up(s, position):
        # u
        # if top row
        try:
            if position == 'T':
                return s
            else:
                percepts = s.state
                index = percepts.find('_')
                swapindex = index-3
                if(swapindex < 0):
                    return None
                r = swap(percepts,index,swapindex)
                return r



        except:
            return None
        # stay same
        # else swap at 3 left
        # 3 left



    def down(s, position):
        try:
            if position == 'B':
                return s
            else:
                percepts = s.state
                index = percepts.find('_')
                r = swap(percepts, index, index + 3)
                return r
        except:
            return None
        # d
        # 3 right
        # if bot row
        # stay same
        # else swap at 3 right

    def left(s, position):
        try:
            if position == 'L':
                return s
            else:
                percepts = s.state
                index = percepts.find('_')
                r = swap(percepts, index, index - 1)
                return r
        except:
            return None

        # l
        # if left column
        # same
        # else
        # move one space left
        # 'validate'
        # return the state that was reached
        pass

    def right(s, position):
        try:
            if position == 'R':
                return s
            else:
                percepts = s.state
                index = percepts.find('_')
                r = swap(percepts, index, index + 1)
                return r
        except:
            return None

    def processor(callback, state, position):
        return callback(state, position)

    switcher = {
        'U': up,
        'D': down,
        'L': left,
        'R': right
    }



##Happy path
def transition(state, action):
    """

    Given a State and an action apply transition function via a callback

    :param state: the current state as a 'State' class
    :param action:
    :return: the state that is a result of taking the action
    """

    # always assuming valid state str
    ##validate_state or catch error

    ##always assuming valid action
    ##validate_action or catch error

    #parsing the string
    reached_states = set()
    index = state.state.find('_')
    callback = Transition.switcher.get(action)

    if index%3==0:
        position = 'L'
        r = Transition.processor(callback,state,position)
        if r: reached_states.add(r)

    if index%3==2:
        position = 'R'
        r = Transition.processor(callback,state,position)
        reached_states.add(r)


    if index<3:
        position = 'T'
        r= Transition.processor(callback,state,position)
        reached_states.add(r)


    if index>5:
        position = 'B'
        r= Transition.processor(callback,state,position)
        reached_states.add(r)


    if(len(reached_states) != 1):
        return None
    else:
        return reached_states.pop()









# program

def main():
    state = State("_12345678")
    action = 'U'
    r = transition(state,action)
    print(r)

if __name__ == '__main__':
    main()



#
# for reachable_state in transitions :
#     if reachable_state == 'up':
#         print('up')
#     if reachable_state == 'down':
#         print('down')
#     if reachable_state == 'left':
#         print('left')
#     if reachable_state == 'right':
#         print('right')
#
