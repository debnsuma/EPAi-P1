# Session 5 assignment of EPAi2.0

This is the README for the EPAi2.0 Assignment. 

Name: Suman Debnath 

- Default Values
- Docstrings & Annotation
- Lambda Function
- Functional introspection
- Callable
- Maps,filter & zip
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Based on above Session we are tasked with develop  code to check special kind of poker with tow give hand
The object achieved in  this assignment as follow
- Function to create deck of cards using regular function
- Function to create deck of cards using map,zip and lambda function
- Function find winner of special poker game based on given set of cards\
Where the rank is as follows the given value in front is arbitrary just for convenience\
Royal Flush     =10000 (for set of 3,4 & 5 cards)\
Straight Flush  = 9000 (for set of 3,4 & 5cards)\
Four of kind    = 8000 (for set of 4 & 5 cards)\
Full House      = 7000 (for set of 5 cards)\
Flush           = 6000 (for set of 3,4&5 cards)\
Straight        = 5000 (for set of 3,4&5 cards)\
Three of kind   = 4000 (for set of 3,4&5 cards)\
Two pair        = 3000 (for set of 3,4&5 cards)\  
One pair        = 2000 (for set of 3,4&5 cards)\
High card       = 1000 (for set of 3,4&5 cards)\
- to create 35(min 20+) test cases to check our code.
- Last but not least create this readme file explaning the different functions
 
## Functions Used
  
`card_deck1_regular()` : This function takes in number of deck required and returns cards in deck

`card_deck2_special()` : This function takes in number of deck required and returns cards in deck this function is created with lambda map and zip function. 

`game_card_poker_winner()`: 
- This Determines the winner of Card game based on given set of cards
  Its calls another function to calculate score of each hand and then compares.
  Note: The input need to be properly order to check Tie Case.
- This function when given 2 set of cards returns the Winner as given below   
- Player 1 if player 1 has a better hand
- Player 2 if player 2 has a better hand
- 'Its a tie both players share the pot' - if both have similar hands

`score_calculator()`: This Function Calculates the score of given hand for selecting the winner in Poker"

## Function Used for `test`

`test_function_poker_game()`: This test checks the game_card_winner is selected properly for user given input
   
`test_function_check_regular_created_deck()` : This test checks the created deck  using regular for loop is matching  manualy created deck

`test_function_check_special_map_zip_lamda_created_deck()`: This test checks the created deck  using regular for map,zip and lamda function is matching  manualy created deck

## The below list of Function check if it is returning right class of win for given hand 
Royal Flush     =10000\
Straight Flush  = 9000\
Four of kind    = 8000\
Full House      = 7000\
Flush           = 6000\
Straight        = 5000\
Three of kind   = 4000\
Two pair        = 3000\  
One pair        = 2000\
High card       = 1000\


def test_function_score_cal_check1():
    assert score_calculator(p_royal_flush_5)[0]==10000, 'score Should be 10000'

def test_function_score_cal_check2():
    assert score_calculator(p_royal_flush_4)[0]==10000, 'score Should be 10000'

def test_function_score_cal_check3():
    assert score_calculator(p_royal_flush_3)[0]==10000, 'score Should be 10000'

def test_function_score_cal_check4():
    assert score_calculator(p_straight_flush_5)[0]==9000, 'score Should be 9000'

def test_function_score_cal_check5():
    assert score_calculator(p_straight_flush_4)[0]==9000, 'score Should be 9000'

def test_function_score_cal_check6():
    assert score_calculator(p_straight_flush_3)[0]==9000, 'score Should be 9000'

def test_function_score_cal_check7():
    assert score_calculator(p_four_of_kind_5)[0]==8000, 'score Should be 8000'

def test_function_score_cal_check8():
    assert score_calculator(p_four_of_kind_4)[0]==8000, 'score Should be 8000'

def test_function_score_cal_check9():
    assert score_calculator(p_full_house_5)[0]==7000, 'score Should be 7000'

def test_function_score_cal_check10():
    assert score_calculator(p_poker_flush_5)[0]==6000, 'score Should be 6000'

def test_function_score_cal_check11():
    assert score_calculator(p_poker_flush_4)[0]==6000, 'score Should be 6000'

def test_function_score_cal_check12():
    assert score_calculator(p_poker_flush_3)[0]==6000, 'score Should be 6000'

def test_function_score_cal_check13():
    assert score_calculator(p_straight_5)[0]==5000, 'score Should be 5000'

def test_function_score_cal_check14():
    assert score_calculator(p_straight_4)[0]==5000, 'score Should be 5000'

def test_function_score_cal_check15():
    assert score_calculator(p_straight_3)[0]==5000, 'score Should be 5000'

def test_function_score_cal_check16():
    assert score_calculator(p_three_of_kind_5)[0]==4000, 'score Should be 4000'

def test_function_score_cal_check17():
    assert score_calculator(p_three_of_kind_4)[0]==4000, 'score Should be 4000'

def test_function_score_cal_check18():
    assert score_calculator(p_three_of_kind_3)[0]==4000, 'score Should be 4000'

def test_function_score_cal_check19():
    assert score_calculator(p_two_Pair_5)[0]==3000, 'score Should be 3000'

def test_function_score_cal_check20():
    assert score_calculator(p_two_Pair_4)[0]==3000, 'score Should be 3000'

def test_function_score_cal_check21():
    assert score_calculator(p_one_Pair_5)[0]==2000, 'score Should be 2000'

def test_function_score_cal_check22():
    assert score_calculator(p_one_Pair_4)[0]==2000, 'score Should be 2000'

def test_function_score_cal_check23():
    assert score_calculator(p_one_Pair_3)[0]==2000, 'score Should be 2000'

def test_function_score_cal_check24():
    assert score_calculator(p_high_card_5)[0]==1000, 'score Should be 1000'

def test_function_score_cal_check25():
    assert score_calculator(p_high_card_4)[0]==1000, 'score Should be 1000'

def test_function_score_cal_check26():
    assert score_calculator(p_high_card_3)[0]==1000, 'score Should be 1000'


For Problem 2
==============

Here we have various small tasks as mentioned above, so lets take them one at a time

### Tasks

#### **Task 1**

In this task we are asked to check whether a number falls in the fabonacci series or not using **list**, **filters** and **lambda functions**. Here we create a function Fibonacci which returns the fabonacci series, Then randomly a list of numbers is generated and matched against the fabonacci list and the matched list is displayed.

#### **Task 2**

All the sub tasks here has to be done using list comprehension. 
   * A We need to take two list and check each elements, if element of list a is even where as element of list b is odd, we will add them else we will ignore them
     * User sends two list
     * The list is zipped and iterated
     * First tuple element is checked for evenness and second tuple element is checked for oddness
     * if the condition is matched those elements are added
   * We have to remove vowels from the string
     * iterate through string
     * check if element falls in the vowel category
   * Make a Relu Function
     * Iterate over the list of numbers
     * if Negative convert to zero, 
     * else leave as it is
   * Make a sigmoid function
     * Create a sigmoid function that takes integer as an input and returns its sigmoid form
     * iterate through the list that user provided and pass each element to sigmoid function
     * Store each element to a new list and return the list
   * Make an Alphabet Cipher
     * check order of each character
     * if order + 5 is greater than order of z which is 122, 
       * then substract 26 from the order of character +5 
     * else add 5 to the order of character
     * join the list to make string
     * return string

#### **Task 3**

In this function the user inputs the paragraph of length 200, if the paragragh word count is less than 200, it raises an error. There is predefined list of bad words [link](https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt ), it is fetched and converted to list. Then the list is check with each word in the para, of any word is found it is alerted.

#### **Task 4**

Here we need to perform tasks using reduce function

*   Add Only even numbers in the list
    *   filter is applied over the list to fetch the even numbers
    *   all the numbers are added using reduce function and lambda function performing the addition
*   To find the biggest character
    *   Here Max function is used
    *   Initial value is " " as this is the first ascii printable character
    *   the input string as passed as argument and max character is returned
*   Add Every 3 number in the list
    *   filter list to get every 3rd element i.e. at index 2,5,8,..
    *   use lambda function to perform addition over that list
    *   return the sum

#### **Task 5**:

In this task we had to create function using list comprehension to generate license plates. Here the format is KADDAADDDD where A is for Alphabet uppercase and D is for digit. random value is generated for DD and DDDD in the range 10 to 99 and 1000 to 9999 respectively. AA is also generated randomly using Ascii.uppercase characters.
Then the list is returned

#### **Task 6**:

* In this task we can switch between KA/DL as the statecode , here the user can give a list of numbers which they want in their number plate
* In task 2 of this we need to create a function which allows custom number plate and statecode and we need to create a partial function that calls this function providing a default number plate where as custom statecode.
  

### Test Cases

Here we have written a lot of testcases to check each functionality thoroughtly as out code shouldnt be breaking. Each function has it own test case and they are also checked for doc string and annotations

