import sense_hat, random, time

"""

  Rock Paper Scissors
  
  Play Rock Paper Scissors with your Raspberry Pi.  Select rock, paper or
  scissors with the joystick. The Pi picks randomly.  
  
  Keeps track of your score- try best out of 5!
  
  Note: Requires sense_hat version 2.2.0 or later
  
"""

sense = sense_hat.SenseHat()

game_state = { 
          "comp_pick" : None,
          "user_pick" : None,
          "picks" : ("rock", "paper", "scissors"),
          "choice_index" : 0,
          "comp_score" : 0,
          "user_score" : 0
        }

start_over_state = game_state.copy()

Y = (255, 255, 0)
G = (0, 255, 0)
B = (0, 0, 255)
X = (0, 0, 0)

####
# Game Images
####

big_rock = [
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, Y, Y, Y, X, X, X,
    X, Y, Y, Y, Y, Y, X, X,
    X, Y, Y, Y, X, Y, Y, X,
    X, Y, Y, Y, Y, Y, Y, X,
    X, X, Y, Y, Y, Y, X, X,
    X, X, X, X, X, X, X, X
]


big_paper = [
    X, X, X, X, X, X, X, X,
    X, X, X, G, G, G, X, X,
    X, X, G, X, G, G, X, X,
    X, G, X, X, G, G, X, X,
    X, G, G, G, G, G, X, X,
    X, G, G, G, G, G, X, X,
    X, G, G, G, G, G, X, X,
    X, X, X, X, X, X, X, X
]


big_scissors = [
    X, X, X, X, X, X, X, X,
    X, B, X, X, X, X, B, X,
    X, X, B, X, X, B, X, X,
    X, X, X, B, B, X, X, X,
    X, X, X, B, B, X, X, X,
    X, B, B, X, X, B, B, X,
    X, B, B, X, X, B, B, X,
    X, X, X, X, X, X, X, X
]


user_rock = [
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, Y, Y, X,
    X, X, X, X, Y, Y, Y, Y,
    X, X, X, X, Y, Y, Y, Y
]

user_paper = [
    X, X, X, X, X, X, G, G,
    X, X, X, X, X, G, X, G,
    X, X, X, X, X, G, G, G,
    X, X, X, X, X, G, G, G
]

user_scissors = [
    X, X, X, X, B, X, X, B,
    X, X, X, X, X, B, B, X,
    X, X, X, X, X, B, B, X, 
    X, X, X, X, B, X, X, B
]

comp_rock = [
    X, X, X, X, X, X, X, X,
    X, Y, Y, X, X, X, X, X,
    Y, Y, Y, Y, X, X, X, X,
    Y, Y, Y, Y, X, X, X, X
]

comp_paper = [
    X, G, G, X, X, X, X, X,
    G, X, G, X, X, X, X, X,
    G, G, G, X, X, X, X, X,
    G, G, G, X, X, X, X, X
]

comp_scissors = [
    B, X, X, B, X, X, X, X,
    X, B, B, X, X, X, X, X,
    B, B, B, B, X, X, X, X,
    B, X, X, B, X, X, X, X
]
     
small_nothing = [
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X
]

####
# Game Functions
####

def get_user_pick(state):
    """
    Takes game state and returns string of user's pick.
    """
    picks = state["picks"]
    return picks[state["choice_index"] % len(picks)]

def show_picks(state):

    user = get_user_pick(state)
    comp = state["comp_pick"]
    
    # show user pick, then comp pick
    if user == "rock":
        user_screen =  user_rock
    elif user == "paper":
        user_screen = user_paper
    elif user == "scissors":
        user_screen = user_scissors
    if comp == "rock":
        comp_screen = comp_rock
    elif comp == "paper":
        comp_screen = comp_paper
    elif comp == "scissors":
        comp_screen = comp_scissors
    
    # Display user choice
    screen1 = small_nothing + user_screen
    sense.set_pixels(screen1)
    
    time.sleep(.5)
    
    # Display comp choice too
    screen2 = comp_screen + user_screen
    sense.set_pixels(screen2)
    
    time.sleep(1)
    
    # Make alternate screen based on result
    if user_wins(game_state):
        P = (0, 150, 0)
    elif user_wins(game_state) == None:
        P = (100, 100, 100)
    else:
        P = (150, 0, 0)
    screen3 = [P if i == X else i for i in screen2]
    
    # Flash Screen
    for i in range(15):
        sense.set_pixels(screen2)
        time.sleep(.02)
        sense.set_pixels(screen3)
        time.sleep(.02)
    
def display_score(state):
    user_score = state["user_score"]
    comp_score = state["comp_score"]
    sense.show_message("You: {0} Pi: {1}".format(user_score, comp_score))
    display(state)

def user_wins(state):
    """
    Returns True if the user wins, False if user loses, and None if tie
    """
    comp = state["comp_pick"]
    user = state["user_pick"]
    
    if comp == user:
        return None
    elif comp == "rock":
        return user == "paper"
    elif comp == "paper":

        return user == "scissors"
    elif comp == "scissors":
        return user == "rock"
    

def score(state):
    if user_wins(state) == True:
        state["user_score"] += 1
    elif user_wins(state) == False:
        state["comp_score"] += 1
    
    # Show picks and display the score
    show_picks(state)
    display_score(state)
    
    # Reset
    state["comp_pick"] = None
    state["user_pick"] = None
    state["choice_index"] = 0
    
    display(state)

def display(state):
    """
    Displays the shape of the current choice index.    
    """
    user_pick = get_user_pick(state)

    if user_pick == "rock":
        sense.set_pixels(big_rock)
    elif user_pick == "paper":
        sense.set_pixels(big_paper)
    elif user_pick == "scissors":
        sense.set_pixels(big_scissors)

####
# Intro on Program Start
####

sense.clear()

for image in [big_rock, big_paper, big_scissors]:
    sense.set_pixels(image)
    time.sleep(.5)
    
sense.show_message("<")
sense.set_rotation(180)
sense.show_message("<")
sense.set_rotation(0)

# Start at the rock
sense.set_pixels(big_rock)

####
# Main Loop
####

while True:
    events = sense.stick.get_events()
    if events:
      for event in events:
        if event.action != 'pressed':
            #this is a hold or keyup; move on
            continue
        if event.direction == 'left':
            game_state["choice_index"] += 1
            display(game_state)
        elif event.direction == 'right':
            game_state["choice_index"] -= 1
            display(game_state)
        elif event.direction == 'middle':
            # Comp picks randomly
            game_state["comp_pick"] = random.choice(game_state["picks"])
            # User picks selected option
            game_state["user_pick"] = get_user_pick(game_state)
            score(game_state)