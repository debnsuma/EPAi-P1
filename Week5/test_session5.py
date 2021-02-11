import inspect
import os
import re

import session5
from session5 import game_card_poker_winner
from session5 import score_calculator
from session5 import card_deck1_regular
from session5 import card_deck2_special

import os
import pytest
import random



##type of Card Suits
suits = ['spades', 'clubs', 'hearts', 'diamonds']
##Face value of cards
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
######Deck for Comparision
deck = [('2', 'clubs'), ('3', 'clubs'), ('4', 'clubs'), ('5', 'clubs'), ('6', 'clubs'), ('7', 'clubs'),
        ('8', 'clubs'), ('9', 'clubs'), ('10', 'clubs'), ('jack', 'clubs'), ('queen', 'clubs'), ('king', 'clubs'),
        ('ace', 'clubs'), ('2', 'diamonds'), ('3', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'),
        ('6', 'diamonds'), ('7', 'diamonds'), ('8', 'diamonds'), ('9', 'diamonds'), ('10', 'diamonds'),
        ('jack', 'diamonds'), ('queen', 'diamonds'), ('king', 'diamonds'), ('ace', 'diamonds'), ('2', 'hearts'),
        ('3', 'hearts'), ('4', 'hearts'), ('5', 'hearts'), ('6', 'hearts'), ('7', 'hearts'), ('8', 'hearts'),
        ('9', 'hearts'), ('10', 'hearts'), ('jack', 'hearts'), ('queen', 'hearts'), ('king', 'hearts'),
        ('ace', 'hearts'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('5', 'spades'), ('6', 'spades'),
        ('7', 'spades'), ('8', 'spades'), ('9', 'spades'), ('10', 'spades'), ('jack', 'spades'),
        ('queen', 'spades'), ('king', 'spades'), ('ace', 'spades')]
## Hands for Testing
p_royal_flush_5 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
p_royal_flush_4 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
p_royal_flush_3 = [('ace', 'spades'), ('king', 'spades'), ('queen', 'spades')]
p_straight_flush_5 = [('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades'), ('9', 'spades')]
p_straight_flush_4 = [('king', 'spades'), ('queen', 'spades'), ('jack', 'spades'), ('10', 'spades')]
p_straight_flush_3 = [('king', 'spades'), ('queen', 'spades'), ('jack', 'spades')]
p_four_of_kind_5 = [('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds'), ('9', 'spades')]
p_four_of_kind_4 = [('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds')]
p_full_house_5 = [('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('jack', 'diamonds'), ('jack', 'spades')]
p_poker_flush_5 = [('king', 'hearts'), ('8', 'hearts'), ('6', 'hearts'), ('4', 'hearts'), ('2', 'hearts')]
p_poker_flush_4 = [('king', 'hearts'), ('8', 'hearts'), ('6', 'hearts'), ('4', 'hearts')]
p_poker_flush_3 = [('king', 'hearts'), ('8', 'hearts'), ('6', 'hearts')]
p_straight_5 = [('8', 'hearts'), ('7', 'spades'), ('6', 'diamonds'), ('5', 'clubs'), ('4', 'hearts')]
p_straight_4 = [('8', 'hearts'), ('7', 'spades'), ('6', 'diamonds'), ('5', 'clubs')]
p_straight_3 = [('8', 'hearts'), ('7', 'spades'), ('6', 'diamonds')]
p_three_of_kind_5 = [('queen', 'spades'), ('queen', 'hearts'), ('queen', 'clubs'), ('7', 'hearts'), ('2', 'club')]
p_three_of_kind_4 = [('queen', 'spades'), ('queen', 'hearts'), ('queen', 'clubs'), ('7', 'hearts')]
p_three_of_kind_3 = [('queen', 'spades'), ('queen', 'hearts'), ('queen', 'clubs')]
p_two_Pair_5 = [('jack', 'spades'), ('jack', 'diamonds'), ('9', 'clubs'), ('9', 'diamonds'), ('5', 'spades')]
p_two_Pair_4 = [('jack', 'spades'), ('jack', 'diamonds'), ('9', 'clubs'), ('9', 'diamonds')]
p_one_Pair_5 = [('king', 'hearts'), ('king', 'clubs'), ('9', 'clubs'), ('8', 'clubs'), ('4', 'hearts')]
p_one_Pair_4 = [('king', 'hearts'), ('king', 'clubs'), ('9', 'clubs'), ('8', 'clubs')]
p_one_Pair_3 = [('king', 'hearts'), ('king', 'clubs'), ('9', 'clubs')]
p_high_card_5 = [('ace', 'hearts'), ('queen', 'clubs'), ('6', 'hearts'), ('4', 'spades'), ('2', 'diamonds')]
p_high_card_4 = [('ace', 'hearts'), ('queen', 'clubs'), ('6', 'hearts'), ('4', 'spades')]
p_high_card_3 = [('ace', 'hearts'), ('queen', 'clubs'), ('6', 'hearts')]


README_CONTENT_CHECK_FOR = [
    'game_card_poker_winner',
    'score_calculator',
    'card_deck1_regular',
    'card_deck2_special',
    'Fibonacci',
    'vowels',
    'list',
    'lambda',
    'zip',
    'tuple',
    'detox',
    'reduce',
    'sigmoid',
    'Cipher',
    'number plate',
    'ReLU'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"



def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_poker_game():
    assert game_card_poker_winner(p_royal_flush_5,p_straight_flush_5) =='Player 1', "Test01-High Hand Cannot lose to straigh flush"
    assert game_card_poker_winner(p_poker_flush_4,p_four_of_kind_4) == 'Player 2', "Test02-Four_of_kind Cannot lose to flush"
    assert game_card_poker_winner(p_poker_flush_5,p_high_card_5) == 'Player 1', "Test03-Flush Cannot lose to high card"
    assert game_card_poker_winner(p_three_of_kind_4,p_three_of_kind_4) == 'Its a tie both players share the pot', "Test04-Same set of cards must be tie"
    assert game_card_poker_winner(p_straight_flush_3,p_high_card_3) == 'Player 1', "Test05-Straigh Flush cannot lose to high card"
    assert game_card_poker_winner(p_three_of_kind_5,p_two_Pair_5) == 'Player 1', "Test06-Three of Kind cannot lose to Two Pair"
    assert game_card_poker_winner(p_high_card_5,p_full_house_5) == 'Player 2', "Test07-Full house cannot lose to High Card"
    assert game_card_poker_winner(p_two_Pair_4,p_four_of_kind_4 ) == 'Player 2', "Test08-Four of kind cannot lose to Two Pair"
    assert game_card_poker_winner(p_three_of_kind_4, p_high_card_4) == 'Player 1', "Test09-Three of kind cannot lose to High card"
    assert game_card_poker_winner(p_two_Pair_4 , p_royal_flush_4) == 'Player 2', "Test10-Royal cannot lose to two pair"
    assert game_card_poker_winner(p_two_Pair_4, p_royal_flush_4) == 'Player 2', "Test11-Royal cannot lose to two pair"
    assert game_card_poker_winner(p_two_Pair_5, p_one_Pair_5) == 'Player 1', "Test12-Two pair cannot lose to one pair"
    assert game_card_poker_winner(p_poker_flush_5, p_straight_flush_5) == 'Player 2', "Test13-Straight flush cannot lose to flush"
    assert game_card_poker_winner(p_royal_flush_3 ,p_straight_3) == 'Player 1', "Test14-Royal flush cannot lose to straigh"
    assert game_card_poker_winner(p_three_of_kind_4, p_four_of_kind_4) == 'Player 2', "Test15-Four of Kind cannot lose to Three of Kind"
    assert game_card_poker_winner(p_one_Pair_3,p_high_card_3) == 'Player 1', "Test16-One Pair cannot lose to High Card"
    assert game_card_poker_winner(p_one_Pair_4,p_two_Pair_4) == 'Player 2', "Test17-Two Pair cannot lose to One Pair"
    assert game_card_poker_winner(p_straight_flush_5,p_one_Pair_5) == 'Player 1', "Test18-Straigh flush cannot lose to One Pair"
    assert game_card_poker_winner(p_high_card_3,p_poker_flush_3) == 'Player 2', "Test19-Flush cannot lose to High card"
    assert game_card_poker_winner(p_four_of_kind_4, p_straight_4) == 'Player 1', "Test20- straight cannot lose to Four of Kind"


def test_function_check_regular_created_deck():
    card_deck_check=card_deck1_regular()
    assert all(item in deck for item in card_deck_check) and len(card_deck_check)==len(deck), "Manual deck and regular deck should be same"

def test_function_check_special_map_zip_lamda_created_deck():
    card_deck_check=card_deck2_special()
    print(card_deck_check)
    assert all(item in deck for item in card_deck_check) and len(card_deck_check)==len(deck), "Manual deck and Special deck should be same"

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


# Test for Assignment 2

def test_add():
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 6, 8, 10]
    assert session5.my_add(a, b) == [], 'you just had to check odd and even and perform addition, and you FAILED..!!'
    b = [1, 3, 5, 7, 9]
    a = [2, 4, 6, 8, 10]
    assert session5.my_add(a, b) == [3, 7, 11, 15,
                                     19], 'you just had to check odd and even and perform addition, and you FAILED..!!'


def test_string():
    mystring = "tsai"
    assert session5.my_alphabet(mystring) == "ts", 'You ust need to remove a,e,i, o, u, You are awesome, you can do it.'


def test_my_relu():
    mylist = [-1, -2, -3, -4, -5, 5, 4, 3, 1, 0, 9, -10, -17, 5, 2]
    assert session5.my_relu(mylist) == [0, 0, 0, 0, 0, 5, 4, 3, 1, 0, 9, 0, 0, 5, 2], "Remove all the negativity"


def test_sigmoid():
    x = 0
    assert session5.sigmoid(x) == 0.5, 'it is simple sigmoid, check google for equation'
    x = 4
    assert session5.sigmoid(x) == 0.9820137900379085, 'it is simple sigmoid, check google for equation'
    x = -4
    assert session5.sigmoid(x) == 0.01798620996209156, 'it is simple sigmoid, check google for equation'


def test_mysigmoid():
    mylist = [0, 4, -4]
    assert session5.mysigmoid(mylist) == [0.5, 0.9820137900379085,
                                          0.01798620996209156], 'do the same thing that you did above, but it is a list this time'


def test_mycipher():
    mystring = "zyxwvutsai"
    assert session5.mycipher(
        mystring) == "edcbazyxfn", "Alphabetical ciphers are very simple,you messed it up but you can do it"


def test_detox():
    mypara = "ola Amigo"
    with pytest.raises(ValueError, match=r".* length .*"):
        session5.detox(mypara), "That is not a paragraph"

    mypara = '''
            reverting for no reason i spent quite some time improving an article that 
            was in a poor state now two people have undone all my work with a click 
            of a button you did not have the courtesy to explain why you reverted it 
            but you still had the fucking cheek to accuse me of leaving an inaccurate 
            edit summary noone is that stupid so you were plainly just out to provoke me 
            well fucking well done consider me fucking provoked i guess you did not even bother 
            to look at the changes before you put all that shit back selfarrest refers to various maneuvers 
            employed in mountaineering it does not refer to that it is that you want to say paris refers to the capital 
            city of france or nile refers to a river that flows into the mediterranean sliding down a snow or ice covered slope 
            arrests stops the slide you think readers are too stupid to understand what arrests means in this 
            context himself or herself you think the single word themselves is some how better expressed in three words andor 
            ice axe you never bothered to read wpslash these potentially lifesaving techniques must be practiced 
            frequently in order to maintain proficiency this website is called wikipedia not wikimanual but you never bothered 
            to read wpnot did you that is just the first five i made many more i left the article looking considerably 
            better and more encyclopaedic but then you came along and fucked it all back up again do you feel 
            proud still waiting for you to justify your risible claim of or also stop stalking and harassing
            '''
    assert session5.detox(
        mypara) == True, "One should not ignore bad words, they should teach people not to say it as it may hurt someone"

    mypara = '''
            reverting for no reason i spent quite some time improving an article that 
            was in a poor state now two people have undone all my work with a click 
            of a button you did not have the courtesy to explain why you reverted it 
            but you still had the cheek to accuse me of leaving an inaccurate 
            edit summary noone is that stupid so you were plainly just out to provoke me 
            well well done consider me provoked i guess you did not even bother 
            to look at the changes before you put all that back selfarrest refers to various maneuvers 
            employed in mountaineering it does not refer to that it is that you want to say paris refers to the capital 
            city of france or nile refers to a river that flows into the mediterranean sliding down a snow or ice covered slope 
            arrests stops the slide you think readers are too stupid to understand what arrests means in this 
            context himself or herself you think the single word themselves is some how better expressed in three words andor 
            ice axe you never bothered to read wpslash these potentially lifesaving techniques must be practiced 
            frequently in order to maintain proficiency this website is called wikipedia not wikimanual but you never bothered 
            to read wpnot did you that is just the first five i made many more i left the article looking considerably 
            better and more encyclopaedic but then you came along and it all back up again do you feel 
            proud still waiting for you to justify your risible claim of or also stop stalking and harassing
            '''
    assert session5.detox(mypara) == False, "One should not classify something good as bad"


def test_myadd():
    mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert session5.myadd(mynumbers) == 2 + 4 + 6 + 8 + 10, 'just check if they are even then add them. Simple.'


def test_mymaxchar():
    mystring = "SHUBHAM AGNIHOTRI"
    assert session5.mymaxchar(mystring) == 'U', 'Need to find the max character, it is not working as expected'
    mystring = "shubham agnihotri"
    assert session5.mymaxchar(mystring) == 'u', 'Need to find the max character, it is not working as expected'


def test_my_atrangi_addition():
    mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert session5.my_atrangi_addition(mynumbers) == 3 + 6 + 9, 'just select evert 3rd element and add it. Simple.'


def test_get_numberplate():
    mynumbers = [random.randint(1000, 10000) for x in range(25)]
    mynumberplates = session5.get_numberplate(mynumbers)
    for i in range(len(mynumberplates)):
        assert mynumberplates[i][-4:] == str(mynumbers[i]), 'Custom Number plates not getting assigned'


def test_ny_number_plate():
    state_code = "KA"
    numberplate = 1224
    assert session5.my_number_plate(state_code, numberplate)[
           :2] == state_code, 'Number plate is not getting generated properly'
    assert session5.my_number_plate(state_code, numberplate)[-4:] == str(
        numberplate), 'Number plate is not getting generated properly'


def test_custom_numberplate():
    state_code = "KA"
    assert session5.custom_numberplate(session5.my_number_plate, state_code)()[
           :2] == state_code, 'Number plate is not getting generated properly'


def test_fibonacci_doc():
    assert bool(session5.fibonacci.__doc__), 'No DocString for fibonacci'


def test_check_result_docs():
    assert bool(session5.check_result.__doc__), 'No DocString for check_result'


def test_my_add_docs():
    assert bool(session5.my_add.__doc__), 'No DocString for my_add'


def test_my_alphabet_docs():
    assert bool(session5.my_alphabet.__doc__), 'No DocString for my_alphabet'


def test_my_relu_docs():
    assert bool(session5.my_relu.__doc__), 'No DocString for my_relu'


def test_sigmoid_docs():
    assert bool(session5.sigmoid.__doc__), 'No DocString for sigmoid'


def test_mysigmoid_docs():
    assert bool(session5.mysigmoid.__doc__), 'No DocString for mysigmoid'


def test_mycipher_docs():
    assert bool(session5.mycipher.__doc__), 'No DocString for mycipher'


def test_detox_docs():
    assert bool(session5.detox.__doc__), 'No DocString for detox'


def test_myadd_docs():
    assert bool(session5.myadd.__doc__), 'No DocString for myadd'


def test_mymaxchar_docs():
    assert bool(session5.mymaxchar.__doc__), 'No DocString for mymaxchar'


def test_my_atrangi_addition_docs():
    assert bool(session5.my_atrangi_addition.__doc__), 'No DocString for my_atrangi_addition'


def test_mynumberplate_docs():
    assert bool(session5.mynumberplate.__doc__), 'No DocString for mynumberplate'


def test_get_numberplate_docs():
    assert bool(session5.get_numberplate.__doc__), 'No DocString for get_numberplate'


def test_my_number_plate_docs():
    assert bool(session5.my_number_plate.__doc__), 'No DocString for my_number_plate'


def test_custom_numberplate_docs():
    assert bool(session5.custom_numberplate.__doc__), 'No DocString for custom_numberplate'


def test_fibonacci_annot():
    assert bool(session5.fibonacci.__annotations__), 'No Annotation for fibonacci'


def test_check_result_annot():
    assert bool(session5.check_result.__annotations__), 'No Annotation for check_result'


def test_my_add_annot():
    assert bool(session5.my_add.__annotations__), 'No Annotation for my_add'


def test_my_alphabet_annot():
    assert bool(session5.my_alphabet.__annotations__), 'No Annotation for my_alphabet'


def test_my_relu_annot():
    assert bool(session5.my_relu.__annotations__), 'No Annotation for my_relu'


def test_sigmoid_annot():
    assert bool(session5.sigmoid.__annotations__), 'No Annotation for sigmoid'


def test_mysigmoid_annot():
    assert bool(session5.mysigmoid.__annotations__), 'No Annotation for mysigmoid'


def test_mycipher_annot():
    assert bool(session5.mycipher.__annotations__), 'No Annotation for mycipher'


def test_detox_annot():
    assert bool(session5.detox.__annotations__), 'No Annotation for detox'


def test_myadd_annot():
    assert bool(session5.myadd.__annotations__), 'No Annotation for myadd'


def test_mymaxchar_annot():
    assert bool(session5.mymaxchar.__annotations__), 'No Annotation for mymaxchar'


def test_my_atrangi_addition_annot():
    assert bool(session5.my_atrangi_addition.__annotations__), 'No Annotation for my_atrangi_addition'


def test_mynumberplate_annot():
    assert bool(session5.mynumberplate.__annotations__), 'No Annotation for mynumberplate'


def test_get_numberplate_annot():
    assert bool(session5.get_numberplate.__annotations__), 'No Annotation for get_numberplate'


def test_my_number_plate_annot():
    assert bool(session5.my_number_plate.__annotations__), 'No Annotation for my_number_plate'


def test_custom_numberplate_annot():
    assert bool(session5.custom_numberplate.__annotations__), 'No Annotation for custom_numberplate'