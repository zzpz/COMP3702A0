class State():


    def __init__(self,state_string):
        try:
            self.state = state_string
        except:
            self.state = "12345678_"


    state: str

    def __str__(self):
        return self.state

    def __repr__(self):
        return self.state

class Node:
    state: State
    action_states: {str : State}
    complete: bool

    def __init__(self,state):
        self.state = state
        self.action_states = None
        self.complete = False

    def __init__(self,state,action_states):
        self.state = state
        self.action_states = action_states
        self.complete = True


    def reachable_states(self):
        return self.action_states.values()

    def possible_actions(self):
        return self.action_states.keys()

    def __str__(self):
        return "state: " + str(self.state) + "    node: "+ str(self.action_states)

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
                return s.state

            if position == 'R':
                if s.state.find('_') < 3:
                    return s.state
                # bad
                else:
                    percepts = s.state
                    index = percepts.find('_')
                    swapindex = index-3
                    if(swapindex < 0):
                        return None
                    r = swap(percepts,index,swapindex)
                    return r
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
                return s.state
            if position == 'R':
                if s.state.find('_') > 7:
                    return s.state
            else:
                percepts = s.state
                index = percepts.find('_')
                swapindex = index+3
                if (swapindex > 8): #magic numbers
                    return None
                r = swap(percepts, index, swapindex)
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
                return s.state
            else:
                percepts = s.state
                index = percepts.find('_')
                swapindex = index - 1
                if (swapindex < 0):
                    return None
                r = swap(percepts, index, swapindex)
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

    def right(s, position):
        try:
            if position == 'R':
                return s.state
            else:
                percepts = s.state
                index = percepts.find('_')

                swapindex = index + 1
                if (swapindex > 8):
                    return None
                r = swap(percepts, index, swapindex)
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
        if r: reached_states.add(r)


    elif index<3:
        position = 'T'
        r= Transition.processor(callback,state,position)
        if r: reached_states.add(r)


    elif index>5:
        position = 'B'
        r= Transition.processor(callback,state,position)
        if r: reached_states.add(r)


    if(len(reached_states) != 1):
        return None
    else:
        return reached_states.pop()



def get_next_states_given_action(state):
    reached_states_by_action = dict([])

    actions = ['U','D','L','R']
    for action in actions:
        r = transition(state, action)
        reached_states_by_action[action] = r
    return reached_states_by_action
# program


def compare(state_1, state_2):
    # happy path
    try:
        valid_actions = []

        d = get_next_states_given_action(state_1)
        for(k,v) in d.items():
            if v is None:
                continue
            if v== state_2.state:
                valid_actions.append(k)

        return valid_actions

    except:
        return None