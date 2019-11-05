"""
This file supplies the generate, decode, verify, and mutate functions
    for each specific trait of an allele.
"""
import random

BUY = "+"
SELL = "-"

LESS_THAN = "<"
GREATER_THAN = ">"

tech_ind_dict = {
    '0' : "1", # 1
    '1' : "2", # 2
    '2' : "3", # 3 
    '3' : "4", #4
    '4' : "5", #5
    '5' : "6", #6
    '6' : "7", #7
    '7' : "8", #8
    '8' : "9", #9
    '9' : "10", #10
    'a' : "11", #11
    'b' : "12", #12
    'c' : "13", #13
    'd' : "14", #14
    'e' : "15", #15
    'f' : "16", #16
    'g' : "17", #17
    'h' : "18", #18 
    'i' : "19", #19
    'j' : "20", #20
    'k' : "21", #21
    'l' : "22", #22
    'm' : "23", #23
    'n' : "24", #24
    'o' : "25", #25
    'p' : "26", #26
    'q' : "27", #27
    'r' : "28", #28
    's' : "29", #29
    't' : "30", #30
    'u' : "31", #31
    'v' : "32", #32
    'w' : "33", #33
    'x' : "34", #34
    'y' : "35", #35
    'z' : "36", #36
    'A' : "37", #37
    'B' : "38", #38
    'C' : "39", #39
    'D' : "40", #40
    'E' : "41", #41
    'F' : "42", #42
    'G' : "43", #43
    'H' : "44", #44
    'I' : "45", #45
    'J' : "46", #46
    'K' : "47", #47
    'L' : "48", #48
    'M' : "49", #49
    'N' : "50", #50
    'O' : "51", #51
    'P' : "52", #52
    'Q' : "53", #53
    'R' : "54", #54
    'S' : "55", #55
    'T' : "56", #56
    'U' : "57", #57
    'V' : "58", #58
    'W' : "59", #59
    'X' : "60", #60
    'Y' : "61", #61
    'Z' : "62", #62
    '!' : "63", #63
    '@' : "64", #64
    '#' : "65", #65
    '$' : "66", #66
    '%' : "67", #67
}



"""                       """
""" Random Initialization """
"""                       """
def generate_encoding(pos=None, tech_ind=None, thresh=None, cond=None, power=None):
    # Generate Position, if necessary
    if pos is None:
        n_pos = random.randint(0,1)
        if n_pos == 0:
            pos = BUY
        else:
            pos = SELL
        
    # Generate Technical Indicator, if necessary
    if tech_ind is None:
        keys = tech_ind_dict.keys()
        tech_ind = random.choice( list(keys) )
        
    # Generate Threshold, if necessary
    if thresh is None:
        n_thresh = random.uniform(0, 999.99)
        thresh = str( n_thresh )

    # Generate Condition, if necessary
    if cond is None:
        n_cond = random.randint(0,1)
        if n_cond == 0:
            cond = LESS_THAN
        else:
            cond = GREATER_THAN
            
    # Generate Power, if necessary
    if power is None:
        power = str( random.randint(0,9) )

    # Generate Encoding
    encoding = pos + tech_ind + thresh[:6] + cond + power

    # Return Generated Encoding
    return encoding



"""          """
""" Decoding """
"""          """
def decode_position( character ):
    # Check if character is a valid postion
    if character == BUY:
        return int(1)
    elif character == SELL:
        return int(-1)

    # Otherwise, return NoneType
    print("< ERR > : Error decoding allele : Position.")
    return None

def decode_tech_ind( character ):
    # Check if character is in technical indicator dictionary
    if character in tech_ind_dict:
        # Return key-value pair
        return tech_ind_dict[ character ]

    # Otherwise, return NoneType
    print("< ERR > : Error decoding allele : Technical Indicator.")
    return None

def decode_threshold( numb_string ):
    # Check if numb_string is a valid float
    try:
        float( numb_string )
    except ValueError:
        # Otherwise, return NoneType
        print("< ERR > : Error decoding allele : Threshold.")
        return None

    # Return 'numb_string' as float
    return float( numb_string )

def decode_condition( character ):
    # Check if character is a valid condition
    if character == LESS_THAN:
        return LESS_THAN
    elif character == GREATER_THAN:
        return GREATER_THAN

    # Otherwise, return NoneType
    print("< ERR > : Error decoding allele : Condition.")
    return None

def decode_power( digit_char ):
    # Check if digit_char is a valid int
    try:
        int( digit_char )
    except ValueError:
        # Otherwise, return NoneType
        print("< ERR > : Error decoding allele : Power.")
        return None

    # Return 'numb_string' as float
    return int( digit_char )



"""          """
""" Encoding """
"""          """
def encode_position( pos ): # DONE
    # Check if position is valid
    if pos == 1:
        return BUY
    elif pos == -1:
        return SELL

    # Otherwise, return NoneType
    print("< ERR > : Error encoding allele : Position.")
    return None

def encode_tech_ind( tech_ind ): # DONE
    # Loop through 'tech_ind_dict'
    for ti in tech_ind_dict:
        # Check for match
        if tech_ind_dict[ti] == tech_ind:
            return ti

    # Otherwise, return NoneType
    print("< ERR > : Error encoding allele : Technical Indicator.")
    return None


def encode_threshold( threshold ): # DONE
    # Check if threshold is a valid float
    try:
        float( threshold )
    except ValueError:
        # Otherwise, return NoneType
        print("< ERR > : Error encoding allele : Threshold.")
        return None

    # Fit Threshold into 6 digits
    thresh_str = str(threshold )[0:6]
    while len(thresh_str) < 6:
        if "." in thresh_str:
            thresh_str += "0"
        else:
            thresh_str = "0" + thresh_str

    # Return threshold as string
    return thresh_str

def encode_condition( condition ): # DONE
    # Check if codnition is a valid character
    if condition == LESS_THAN:
        return LESS_THAN
    elif condition == GREATER_THAN:
        return GREATER_THAN

    # Otherwise, return NoneType
    print("< ERR > : Error encoding allele : Condition.")
    return None

def encode_power( power ): # DONE
    # Check if power is valid
    try:
        int( power )
        if 0 <= power and power <= 9:
            # Return string representation of power
            return str(power)
    except ValueError:
        # Otherwise, return NoneType
        print("< ERR > : Error encoding allele : Power.")
        return None
    
    # Otherwise, return NoneType
    print("< ERR > : Error encoding allele : Power.")
    return str(power)




"""          """
""" Mutation """
"""          """
def should_mutate( mutate_prob ):
    # Determine if mutate should occur
    result = random.random()
    if result < mutate_prob:
        return True

    return False

def mutate_position( character, mutate_prob):
    # Check if mutation should occur
    if not should_mutate( mutate_prob ):
        # No mutation
        return character

    # Mutate position
    if character == BUY:
        return SELL
    elif character == SELL:
        return BUY

    # Otherwise, return NoneType
    print("< ERR > : Failed to mutate position, invalid encoding! {}".format(character))
    return None

def mutate_tech_indicator( character, mutate_prob ):
    # Check if mutation should occur
    if not should_mutate( mutate_prob ):
        # No mutation
        return character

    # Mutate technical indicator
    keys = tech_ind_dict.keys()
    tech_ind = random.choice( list(keys) )

    # Return mutated value
    return tech_ind

def mutate_threshold( numb_string, mutate_prob ):
    # Check if mutation should occur
    if not should_mutate( mutate_prob ):
        # No mutation
        return numb_string

    # Verify 'numb_string' is a float
    try:
        float( numb_string )
    except ValueError:
        # Otherwise, return NoneType
        print("< ERR > : Failed to mutate threshold, invalid encoding! {}".format(numb_string))
        return None

    # Mutate threshold
    threshold = float( numb_string )
    mutate_size = threshold * 0.10
    mutation = random.uniform(-mutate_size, mutate_size)
    threshold += mutation
    
    # Return mutated value
    return str( threshold )

def mutate_condition( character, mutate_prob ):
    # Check if mutation should occur
    if not should_mutate( mutate_prob ):
        # No mutation
        return character
    
    # Mutate condition
    if character == LESS_THAN:
        return GREATER_THAN
    elif character == GREATER_THAN:
        return LESS_THAN

    # Otherwise, return NoneType
    print("< ERR > : Failed to mutate condition, invalid encoding! {}".format(character))
    return None

def mutate_power( digit_char, mutate_prob ):
    # Check if mutation should occer
    if not should_mutate( mutate_prob ):
        # No mutation
        return digit_char

    # Verify 'digit_char' is a number
    try:
        int( digit_char )
    except ValueError:
        # Otherwise, return NoneType
        print("< ERR > : Failed to mutate power, invalid encoding! {}".format(digit_char))
        return None
    
    # Mutate Power
    power = int( digit_char )
    mutation = random.randint(-1, 1)
    power += mutation
    if power < 0:
        power = 0
    if power > 9:
        power = 9
        
    # Return mutated value
    return str( power )



"""           """
""" Crossover """
"""           """
def crossover(allele_1, allele_2, n_offspring):
    # Obtain Encodings From Alleles
    mate_1 = allele_1.encoding
    mate_2 = allele_2.encoding
    mates = [mate_1, mate_2]

    offspring = []

    for i in range(n_offspring):
        # Form A New Child Encoding
        pos = random.choice(mates)[0:1]
        tech_ind = random.choice(mates)[1:2]
        threshold = random.choice(mates)[2:8]
        condition = random.choice(mates)[8:9]
        power = random.choice(mates)[9:10]

        child = pos + tech_ind + threshold + condition + power
        offspring.append(child)

    # Return Children
    return offspring
    





    
    
        
