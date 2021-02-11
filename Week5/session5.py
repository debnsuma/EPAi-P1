from operator import itemgetter
import random
import math
from functools import reduce, partial
import string

suits = ['spades', 'clubs', 'hearts', 'diamonds']
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
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


def merge(list1: "This function", list2:"This Function mergers two given list")->"Merged list":
    "This Function when given 2 list return combined list"
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list

def card_deck1_regular(n: 'number of Decks' = 1) -> 'List of Cards':
    """
    This Program takes in number of deck and provides list of cards in it.
    """
    Card_deck = []
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    if n >= 1 and isinstance(n, int):
        for n in range(n):
            for b in suits:
                for a in vals:
                    Card_deck.append((a, b))
    else:
        print("Number of decks needs to be  +ve integer")
    return Card_deck

def card_deck2_special(n: 'number of Decks' = 1) -> 'List of Cards':
    "Single expression that including lambda, zip and map functions to select create 52 cards in a deck"
    if n>=1 and isinstance(n, int):
        card_deck2 = n*list(map(lambda x:(x[0], x[1]),zip(vals*4,suits*13)))
    else:
        print("Number of decks needs to be  +ve integer")
    return card_deck2

def determinevalue1(y: "Face Number of Card") -> "Program Number of Card":
    """ This function generates is the program number of cards"""
    val_number_dic = {'2': 12, '3': 13, '4': 14, '5': 15, '6': 16, '7': 17, '8': 18, '9': 19, '10': 20, 'jack': 21,'queen': 22, 'king': 23, 'ace': 24}
    z = val_number_dic.get(y)
    return z

def game_card_poker_winner(hand1: "List of Cards with Player 1",hand2: "List of Cards with Player 1") -> 'Returns the number of  player who won':
    """
    This Determines the winner of Card game based on given set of cards
    Its calls another function to calculate score of each hand and then compares.
    Note: The input need to be properly order to check Tie Case.
    """
    winner = 'Its a tie both players share the pot'
    check1 = all(item in deck for item in hand2)
    check2 = all(item in deck for item in hand2)
    if len(hand1) == len(hand2) and check1 is True and check2 is True:
        score1 = score_calculator(hand1)
        score2 = score_calculator(hand2)
        for a in range(len(hand1) + 1):
            if score1[a] > score2[a]:
                winner = 'Player 1'
                break
            elif score1[a] < score2[a]:
                winner = 'Player 2'
                break
    elif check1 is False and check2 is False:
        winner = 'Its a tie as Both Player should have legitimate cards'
    elif check1 is False:
        winner = 'Its a tie as Player1 should have legitimate cards'
    elif check2 is False:
        winner = 'Its a tie as Player2 should have legitimate cards'
    else:
        winner = 'Its a tie Both Players should have same amount of cards'
    return winner

def card_sorter_and_numbered(hand: 'unsorted hand with card number') -> 'Sorted card number with structured number':
    """ This Program sorts the cards based on suit and vals and returns with number in place of vals"""
    hand_vals = list(map(itemgetter(0), hand))
    hand_suit = list(map(itemgetter(1), hand))
    hand_vals1 = []
    for a in hand_vals:
        hand_vals1.append(determinevalue1(a))
    hand_r = merge(hand_vals1, hand_suit)
    hand_r = sorted(hand_r, key=lambda x: (x[1], -x[0]))
    return hand_r, hand_vals1, hand_suit

def checkconsecutive(l: 'Take in list  and checks if it consecutive number or not') -> 'True or False':
    return sorted(l) == list(range(min(l), max(l) + 1))

def score_calculator(hand: 'input is list of cards') -> 'The score of given hand':
    "This Function Calculates the score of given hand for selecting the winner in Poker"
    Score = []
    cards_in_hand = len(hand)
    sorted_cards, hand_fval, hand_suit = card_sorter_and_numbered(hand)
    hand_suit_uni = list(set(hand_suit))
    hand_suit_uni_nu = len(hand_suit_uni)
    hand_fvals_uni = list(set(hand_fval))
    hand_fvals_uni_nu = len(hand_fvals_uni)
    #####for Straight flush
    hand_fval_sorted = sorted(hand_fval, reverse=True)
    ct1 = hand_fval.count(hand_fvals_uni[0])
    ct2 = hand_fval.count(hand_fvals_uni[1]) if hand_fvals_uni_nu >= 2 else 1
    ct3 = hand_fval.count(hand_fvals_uni[2]) if hand_fvals_uni_nu >= 3 else 1
    ct4 = hand_fval.count(hand_fvals_uni[3]) if hand_fvals_uni_nu >= 4 else 1
    ct = sorted((ct1, ct2, ct3, ct4), reverse=True)
    Royal_flush_sum_dict = {5: 110, 4: 90, 3: 69}
    Four_of_kind_dict = {5: 2, 4: 1}
    #####
    # "Royal Flush"
    if hand_suit_uni_nu == 1 and sum(hand_fval) == Royal_flush_sum_dict.get(cards_in_hand):
        score = hand_fval_sorted
        score.insert(0, 10000)
    # Straight flush
    elif hand_suit_uni_nu == 1 and checkconsecutive(hand_fval_sorted):
        score = hand_fval_sorted
        score.insert(0, 9000)
    # Four of a kind
    elif cards_in_hand >= 4 and hand_fvals_uni_nu == Four_of_kind_dict.get(cards_in_hand) and ct[0] == 4:
        score = hand_fval_sorted
        score.insert(0, 8000)
    # Full House
    elif cards_in_hand == 5 and hand_fvals_uni_nu == 2 and ct[0] == 3:
        score = hand_fval_sorted
        score.insert(0, 7000)
    # Flush
    elif hand_suit_uni_nu == 1:
        score = hand_fval_sorted
        score.insert(0, 6000)
    # Straight
    elif checkconsecutive(hand_fval_sorted):
        score = hand_fval_sorted
        score.insert(0, 5000)
    # Three of kind
    elif ct[0] == 3:
        score = hand_fval_sorted
        score.insert(0, 4000)
    # Two Pair
    elif cards_in_hand >= 4 and ct[0] == 2 and ct[1] == 2:
        score = hand_fval_sorted
        score.insert(0, 3000)
    # One Pair
    elif ct[0] == 2 and ct[1] == 1:
        score = hand_fval_sorted
        score.insert(0, 2000)
    # High Card
    else:
        score = hand_fval_sorted
        score.insert(0, 1000)
    return score


# 1. Fibonacci Check

def fibonacci(count: int) -> list:
    """
    This function takes a count an input and generated Fibonacci series element count equal to count

    # input:
        count   : int

    # Returns
        list

    # Funcationality:
        Calcualtes the sum of last two list elements and appends it to the list until the count is completed.
        by default it generates a list of size 2

    For eg: if count is 21 the list will generate fabonacci series of list length as 21

    """
    fib_list = [0, 1]
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), range(2, count)))
    return fib_list[:count]


def check_result(my_number: list) -> list:
    """
    This function is used to generate the list of random numbers or take the list from the user and check it against the Fibonacci
    list and display the output.

    # input:
        my_number   : list List to match against the Fibonacci list given by user

    # Returns
        list : returns the matched list

    # Functionality:
        It a random list of numbers in the range 1 to 10000 and then matches it with Fibanacci list
        returned from calling Fibonacci function. Then it prints the matched numbers

    """
    if not my_number:
        my_number = []
        # Generating a 100000 length long list
        for _ in range(0, 100000):
            my_number.append(random.randint(1, 10000))

    # generating fabonacci list upto max element less than 10000
    print(fibonacci(21))

    # Matches the generated list with the list of Fibonacci and filters the matched numbers
    result = list(filter(lambda x: x in my_number, fibonacci(21)))
    result.sort()
    return result


my_number = [1, 7, 8, 10]
mylist = check_result(my_number)
# 2. List Comprehension

## 2.1

def my_add(a: list, b: list) -> list:
    """
    This function takes two list, compares each element, if list 1 ahs even element and list
    2 has odd element then they are added else ignored

    # Input:
        a: List (Input List 1)
        b: List (Input List 2)

    # Returns:
        list: Once the addition is done, the result is stored in the list and returned.

    # Functionality:
        The two lists are zipped and each tuple is iterated, element 1 of the tuple is checked of
        eveness and element b of the tuple is checked for oddness, if the condition is satisfied
        then they are added and the result is stored in a list.
    """

    result = [x + y for x, y in zip(a, b) if x % 2 == 0 if y % 2 != 0]
    return result


## 2.2

def my_alphabet(mystring: str) -> str:
    """
    This function takes in string as inmput and checks if it contains any vowel
    it removed all the vowels from the string and returns it

    # Input:
        mystring: str (Input string over which vowel check operation will be performed.)

    # Returns:
        str: string with no vowels

    # Functionality:
        This function iterates over the elements of the string and checks if each element
        is in vowel list or not. if not then it adds to a list.
        the list later is then converted to string using join function.
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = "".join([x for x in mystring if x not in vowels])
    return result


## 2.3

def my_relu(mylist: list) -> list:
    """
    This function takes in list as an input and converts all the negative value of the
    list to positive and keeps positive values intact.

    # Input:
        mylist: list(It is a list of integers given by the user)

    # Returns:
        list: returns the corrected list

    # Functionality:
        Each element of the input list is checked for positive,
        if it is negative then it is replaced with 0.
    """
    result = [x if x >= 0 else 0 for x in mylist]
    return result


## 2.4

def sigmoid(x: int) -> float:
    """
        This function squeezes value to 0 to 1.

        # Input:
            x: int, it is the number whose sigmoid has to be calculated

        # Returns:
            float: This function returns the sigmoid value of the number

        # Functionality:
            This function takes a number and performs a
            sigmoid operation over it and returns the result
    """
    return 1 / (1 + math.exp(-x))


def mysigmoid(mylist: list) -> list:
    """
    This function converted each element of the input list to its sigmoid form

    # Input:
        mylist: list, This is the input list where sigmoid operation is performed

    # Returns:
        list: It returns the transformed list

    # Functionality:
        The input list is iterated and each element is passed as a parameter to sigmoid function
        the result is stored in another list and returned

    """
    result = [sigmoid(x) for x in mylist]
    return result


## 2.5

def mycipher(mystring: str) -> str:
    """
    This function performs an alphabatical cipher

    # Input:
        mystring: str, String over which cipher has to be done

    # Returns:
        str: Encrypted String

    # Funcationality:
        We need to shift each character by 5, if it is on the bottleneck, it starts again from a.
        here only lowercase alphabets are used. so we check if the order of input character is
        + 5 greater than ord of z, then we substract 26 out of it resuling in -21 (5-26) else
        we add it directly.
    """
    result = "".join([chr(ord(x) - 21) if (ord(x) + 5) > ord('z') else chr(ord(x) + 5) for x in mystring])
    return result


# 3 Detox

def detox(mypara: str) -> bool:
    """
    This function is used to check if bad words are present in a paragraph or not and flag them

    # Input:
        mypara: str, Input paragraph given by the user

    # Returns:
        bool: It returns True if any bad word found else returns false

    # Functionality:
        The paragraph is split into words and then each word is compared with the bad word list and
        is being flagged, if any true flag is seen, the para is marked as toxic.
    """

    if len(mypara.split()) < 200:
        raise ValueError("Paragraph length should be minimum 200")
    lines = ['4r5e', '5h1t', '5hit', 'a55', 'anal', 'anus', 'ar5e', 'arrse', 'arse', 'ass', 'ass-fucker', 'asses',
             'assfucker', 'assfukka', 'asshole', 'assholes', 'asswhole', 'a_s_s', 'b!tch', 'b00bs', 'b17ch', 'b1tch',
             'ballbag', 'balls', 'ballsack', 'bastard', 'beastial', 'beastiality', 'bellend', 'bestial', 'bestiality',
             'bi+ch', 'biatch', 'bitch', 'bitcher', 'bitchers', 'bitches', 'bitchin', 'bitching', 'bloody', 'blow job',
             'blowjob', 'blowjobs', 'boiolas', 'bollock', 'bollok', 'boner', 'boob', 'boobs', 'booobs', 'boooobs',
             'booooobs', 'booooooobs', 'breasts', 'buceta', 'bugger', 'bum', 'bunny fucker', 'butt', 'butthole',
             'buttmunch', 'buttplug', 'c0ck', 'c0cksucker', 'carpet muncher', 'cawk', 'chink', 'cipa', 'cl1t', 'clit',
             'clitoris', 'clits', 'cnut', 'cock', 'cock-sucker', 'cockface', 'cockhead', 'cockmunch', 'cockmuncher',
             'cocks', 'cocksuck ', 'cocksucked ', 'cocksucker', 'cocksucking', 'cocksucks ', 'cocksuka', 'cocksukka',
             'cok', 'cokmuncher', 'coksucka', 'coon', 'cox', 'crap', 'cum', 'cummer', 'cumming', 'cums', 'cumshot',
             'cunilingus', 'cunillingus', 'cunnilingus', 'cunt', 'cuntlick ', 'cuntlicker ', 'cuntlicking ', 'cunts',
             'cyalis', 'cyberfuc', 'cyberfuck ', 'cyberfucked ', 'cyberfucker', 'cyberfuckers', 'cyberfucking ', 'd1ck',
             'damn', 'dick', 'dickhead', 'dildo', 'dildos', 'dink', 'dinks', 'dirsa', 'dlck', 'dog-fucker', 'doggin',
             'dogging', 'donkeyribber', 'doosh', 'duche', 'dyke', 'ejaculate', 'ejaculated', 'ejaculates ',
             'ejaculating ', 'ejaculatings', 'ejaculation', 'ejakulate', 'f u c k', 'f u c k e r', 'f4nny', 'fag',
             'fagging', 'faggitt', 'faggot', 'faggs', 'fagot', 'fagots', 'fags', 'fanny', 'fannyflaps', 'fannyfucker',
             'fanyy', 'fatass', 'fcuk', 'fcuker', 'fcuking', 'feck', 'fecker', 'felching', 'fellate', 'fellatio',
             'fingerfuck ', 'fingerfucked ', 'fingerfucker ', 'fingerfuckers', 'fingerfucking ', 'fingerfucks ',
             'fistfuck', 'fistfucked ', 'fistfucker ', 'fistfuckers ', 'fistfucking ', 'fistfuckings ', 'fistfucks ',
             'flange', 'fook', 'fooker', 'fuck', 'fucka', 'fucked', 'fucker', 'fuckers', 'fuckhead', 'fuckheads',
             'fuckin', 'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme ', 'fucks', 'fuckwhit', 'fuckwit',
             'fudge packer', 'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkin', 'fuks', 'fukwhit', 'fukwit', 'fux',
             'fux0r', 'f_u_c_k', 'gangbang', 'gangbanged ', 'gangbangs ', 'gaylord', 'gaysex', 'goatse', 'God',
             'god-dam', 'god-damned', 'goddamn', 'goddamned', 'hardcoresex ', 'hell', 'heshe', 'hoar', 'hoare', 'hoer',
             'homo', 'hore', 'horniest', 'horny', 'hotsex', 'jack-off ', 'jackoff', 'jap', 'jerk-off ', 'jism', 'jiz ',
             'jizm ', 'jizz', 'kawk', 'knob', 'knobead', 'knobed', 'knobend', 'knobhead', 'knobjocky', 'knobjokey',
             'kock', 'kondum', 'kondums', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 'l3i+ch', 'l3itch', 'labia',
             'lmfao', 'lust', 'lusting', 'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'masochist',
             'master-bate', 'masterb8', 'masterbat*', 'masterbat3', 'masterbate', 'masterbation', 'masterbations',
             'masturbate', 'mo-fo', 'mof0', 'mofo', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz',
             'mothafucked ', 'mothafucker', 'mothafuckers', 'mothafuckin', 'mothafucking ', 'mothafuckings',
             'mothafucks', 'mother fucker', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckers',
             'motherfuckin', 'motherfucking', 'motherfuckings', 'motherfuckka', 'motherfucks', 'muff', 'mutha',
             'muthafecker', 'muthafuckker', 'muther', 'mutherfucker', 'n1gga', 'n1gger', 'nazi', 'nigg3r', 'nigg4h',
             'nigga', 'niggah', 'niggas', 'niggaz', 'nigger', 'niggers ', 'nob', 'nob jokey', 'nobhead', 'nobjocky',
             'nobjokey', 'numbnuts', 'nutsack', 'orgasim ', 'orgasims ', 'orgasm', 'orgasms ', 'p0rn', 'pawn', 'pecker',
             'penis', 'penisfucker', 'phonesex', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks',
             'phuq', 'pigfucker', 'pimpis', 'piss', 'pissed', 'pisser', 'pissers', 'pisses ', 'pissflaps', 'pissin ',
             'pissing', 'pissoff ', 'poop', 'porn', 'porno', 'pornography', 'pornos', 'prick', 'pricks ', 'pron',
             'pube', 'pusse', 'pussi', 'pussies', 'pussy', 'pussys ', 'rectum', 'retard', 'rimjaw', 'rimming', 's hit',
             's.o.b.', 'sadist', 'schlong', 'screwing', 'scroat', 'scrote', 'scrotum', 'semen', 'sex', 'sh!+', 'sh!t',
             'sh1t', 'shag', 'shagger', 'shaggin', 'shagging', 'shemale', 'shi+', 'shit', 'shitdick', 'shite', 'shited',
             'shitey', 'shitfuck', 'shitfull', 'shithead', 'shiting', 'shitings', 'shits', 'shitted', 'shitter',
             'shitters ', 'shitting', 'shittings', 'shitty ', 'skank', 'slut', 'sluts', 'smegma', 'smut', 'snatch',
             'son-of-a-bitch', 'spac', 'spunk', 's_h_i_t', 't1tt1e5', 't1tties', 'teets', 'teez', 'testical',
             'testicle', 'tit', 'titfuck', 'tits', 'titt', 'tittie5', 'tittiefucker', 'titties', 'tittyfuck',
             'tittywank', 'titwank', 'tosser', 'turd', 'tw4t', 'twat', 'twathead', 'twatty', 'twunt', 'twunter',
             'v14gra', 'v1gra', 'vagina', 'viagra', 'vulva', 'w00se', 'wang', 'wank', 'wanker', 'wanky', 'whoar',
             'whore', 'willies', 'willy', 'xrated', 'xxx']
    result = any([False if x not in lines else True for x in mypara.split()])
    return result


# 4 Reduce Functions

## 4.1

def myadd(mynumbers: list) -> int:
    """
    This function adds only even numbers to list

    # Input:
        mynumbers: list, This is a list of numbers provided by theuser

    # Returns:
        int: It returns the calculated sum of the integers

    # Functionality:
        This function takes in list, filters out all the even number using filter and lambda
        and then passes that list to reduce function to add all the elements of it, then the result
        is returned back.

    """
    result = reduce(lambda x, y: x + y, filter(lambda x: (x % 2 == 0), mynumbers))
    return result


## 4.2

def mymaxchar(mystring: str) -> chr:
    """
    This function finds the max character from the string.

    # Input:
        mystring: list, String provided by theuser

    # Returns:
        chr: Biggest printable character in the string

    # Functionality:
        This function takes in string, and checks each element if the string with other
        to fundout which is the biggest one.
    """

    result = reduce(max, mystring, " ")
    return result


## 4.3

def my_atrangi_addition(mynumbers: list) -> int:
    """
    This function add every 3rd number in the list i.e. at index 2,5,8,...

    # Input:
        mynumber: list, This is a list of numbers provided by theuser

    # Returns:
        int: It returns the calculated sum of the integers

    # Functionality:
        This function takes in list, filters out the list containing all third elements
        and then it is added

    """
    result = reduce(lambda x, y: x + y, mynumbers[2::3])
    return result


# 5

def mynumberplate() -> list:
    """
    This function is used to generate random number plates

    # Input:
        None

    # Returns:
        list: This function returns list of all the generated number plates.

    # Functionality
        The format of number plate has to be KADDAADDDD, D is digit and A is alphabet
        DD has to be in the range 10 to 99 where as DDDD has to be in the range 1000 to 9999
        AA has to be uppercase ascii character, A loop is run 25 times and these values are randomly picked and assigned

    """
    result = ["KA" + str(random.randint(10, 100)) + random.choice(string.ascii_uppercase) + random.choice(
        string.ascii_uppercase) + str(random.randint(1000, 10000)) for _ in range(15)]
    return result


# 6

## 6.1
def get_numberplate(numberplate: list) -> list:
    """
    This function is used to generate random number plates with user choice numbers

    # Input:
        None

    # Returns:
        list: This function returns list of all the generated number plates.

    # Functionality
        The format of number plate has to be KADDAADDDD/DLDDAADDDD, D is digit and A is alphabet
        DD has to be in the range 10 to 99 where as DDDD has to be in the range 1000 to 9999, chosen by the user
        AA has to be uppercase ascii character, A loop is run 25 times and these values are randomly picked and assigned

    """
    result = [random.choice(["KA", "DL"]) + str(random.randint(10, 100)) + random.choice(
        string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(numberplate[_]) for _ in range(15)]
    return result


## 6.2

def my_number_plate(state_code: str, numberplate: int) -> str:
    """
    This function is used to generate custom number plates

    # Input:
        state_code: str
        numberplate:int

    # Returns:
        list: This function returns list of all the generated number plates.

    # Functionality
        The format of number plate has to be KADDAADDDD/DLDDAADDDD, D is digit and A is alphabet
        DD has to be in the range 10 to 99 where as DDDD has to be in the range 1000 to 9999, chosen by the user
        AA has to be uppercase ascii character, A loop is run 25 times and these values are randomly picked and assigned
    """
    return state_code + str(random.randint(10, 100)) + random.choice(string.ascii_uppercase) + random.choice(
        string.ascii_uppercase) + str(numberplate)


def custom_numberplate(fn, statecode: str) -> str:
    """
    This function is used to create custom statewise numberplates

    # Input:
        fn: Funtion (It will be called inside the partial function)
        statecode: str

    # Returns:
        str: It return the numberplate in the string

    # Functionality:
        This function call partial function which takes function as the input and its variable as the
        parameter. statecode is something given by the user.

    """
    f = partial(fn, state_code=(statecode), numberplate=9999)
    return f


