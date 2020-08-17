class A0:
    pass


##Happy path


def transition(state, action):
    reachable_states = []
    # always assuming valid state
    ##validate_state or catch error

    ##always assuming valid action
    ##validate_action or catch error

    # u

    # d

    # l

    # r

    reachable_states.extend(('up','down','left','right'))

    return reachable_states


class State:
    state = '12345678_'



# program
state = State().state
action = 'action'

transitions = transition(state,action)

for reachable_state in transitions :
    if reachable_state == 'up':
        print('up')
    if reachable_state == 'down':
        print('down')
    if reachable_state == 'left':
        print('left')
    if reachable_state == 'right':
        print('right')

