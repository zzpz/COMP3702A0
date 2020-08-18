from a0 import *
import argparse

def main():
    go = True

    while(go):
        ##get inputs

        parser = argparse.ArgumentParser(description='Calculate valid actions')
        parser.add_argument("state1", help="12345678_")
        parser.add_argument("state2", help="1234567_8")

        args = parser.parse_args()
        state = State(args.state1)
        state_2 = State(args.state2)

        ##calculate
        valid_moves = compare(state,state_2)


        ##print outputs
        if len(valid_moves) <1:
            print("IMPOSSIBLE")
        else:
            print(','.join([(x) for x in valid_moves]))


        #end
        go = False





if __name__ == '__main__':
    main()
