# IMPORT THE LAB1 MODULE TO TEST FUNCTIONS
import lab1

# TEST FUNCTION: FACTORIAL
# VALIDATES THE FACTORIAL FUNCTION WITH INPUT 5 AND 0
def test_factorial_logic():
    assert lab1.factorial(5) == 120
    assert lab1.factorial(0) == 1

# TEST FUNCTION: FIBONACCI
# VALIDATES THE FIBONACCI FUNCTION WITH INPUT 7 AND 0
def test_fibonacci_sequence():
    assert lab1.Fibonacci(7) == 13
    assert lab1.Fibonacci(0) == 0

# TEST FUNCTION: SUM TO GOAL
# CHECKS IF THE PRODUCT IS RETURNED WHEN TWO ELEMENTS SUM TO TARGET 
def test_combination_sum():
    assert lab1.sum_to_goal([1, 2, 3, 4], 5) == 6
    assert lab1.sum_to_goal([1, 2, 3], 10) == 0

# TEST FUNCTION: WINS ROCK SCISSORS PAPER
# TESTS ALL POSSIBLE GAME OUTCOMES
def test_rps_game_logic():
    assert lab1.wins_rock_scissors_paper("Rock", "Scissors") == True
    assert lab1.wins_rock_scissors_paper("Rock", "Rock") == False

# TEST FUNCTION: INCREMENTER CLASS
# CHECKS IF COUNTER INCREASES PROPERLY WITH STEP SIZE
def test_counter_increase():
    new_counter = lab1.Incrementer(2)
    new_counter.update()
    new_counter.update()
    assert new_counter.count() == 4

# TEST FUNCTION: DECREMENTER CLASS
# CHECKS IF COUNTER DECREASES PROPERLY WITH STEP SIZE
def test_counter_decrease():
    lower_counter = lab1.Decrementer(2)
    lower_counter.update()
    lower_counter.update()
    assert lower_counter.count() == -4
