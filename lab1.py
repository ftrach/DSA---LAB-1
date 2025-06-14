# FUNCTION: WINS_ROCK_SCISSORS_PAPER 
# PARAMETERS: TWO STRINGS (PLAYER AND OPPONENT CHOICES)
# RETURNS: TRUE IF PLAYER WINS, FALSE OTHERWISE
def wins_rock_scissors_paper(user_choice_input, opponent_choice_input):
    user_choice_input = user_choice_input.lower()
    opponent_choice_input = opponent_choice_input.lower()
    if user_choice_input == opponent_choice_input:
        return False
    return (user_choice_input == "rock" and opponent_choice_input == "scissors") or \
           (user_choice_input == "scissors" and opponent_choice_input == "paper") or \
           (user_choice_input == "paper" and opponent_choice_input == "rock")

# FUNCTION: FACTORIAL
# PARAMETERS: ONE INTEGER
# RETURNS: FACTORIAL VALUE OF THE INPUT
def factorial(input_number):
    if input_number == 0:
        return 1
    result_accumulator = 1
    for multiplier in range(1, input_number + 1):
        result_accumulator *= multiplier
    return result_accumulator

# FUNCTION: FIBONACCI
# PARAMETERS: ONE INTEGER
# RETURNS: N-TH FIBONACCI VALUE
def Fibonacci(index_position):
    if index_position == 0:
        return 0
    elif index_position == 1:
        return 1
    previous_number, current_number = 0, 1
    for counter in range(2, index_position + 1):
        previous_number, current_number = current_number, previous_number + current_number
    return current_number

# FUNCTION: SUM_TO_GOAL
# PARAMETERS: LIST OF NUMBERS AND A GOAL VALUE
# RETURNS: PRODUCT OF TWO ELEMENTS WHOSE SUM MATCHES GOAL
def sum_to_goal(number_pool, target_value):
    checked_values = set()
    for candidate in number_pool:
        needed_pair = target_value - candidate
        if needed_pair in checked_values:
            return candidate * needed_pair
        checked_values.add(candidate)
    return 0

# CLASS: INCREMENTER
# TRACKS A VALUE AND INCREASES IT BY A STEP SIZE
class Incrementer:
    def __init__(self, delta_step=1):
        self.delta_step = delta_step
        self.current_count = 0

    # METHOD: COUNT
    # RETURNS THE CURRENT COUNTER VALUE
    def count(self):
        return self.current_count

    # METHOD: UPDATE
    # INCREASES THE COUNTER VALUE BY STEP SIZE
    def update(self):
        self.current_count += self.delta_step

# CLASS: DECREMENTER
# INHERITS INCREMENTER BUT DECREASES THE COUNTER INSTEAD
class Decrementer(Incrementer):
    # METHOD: UPDATE
    # DECREASES THE COUNTER VALUE BY STEP SIZE
    def update(self):
        self.current_count -= self.delta_step
