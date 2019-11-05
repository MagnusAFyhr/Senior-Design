"""
This file supplies the generate, decode, verify, and mutate functions
    for a genome.
"""

import allele.allele_helper as allele_helper
import random

ALLELES_PER_GENOME = 23

"""                       """
""" Random Initialization """
"""                       """
def generate_encoding(buy_limit=None, sell_limit=None, alleles=[]):
    # Generate Allele Encodings, if necessary
    if len(alleles) == 0:
        # populate alleles
        while len(alleles) < ALLELES_PER_GENOME:
            allele = allele_helper.generate_encoding()
            alleles.append(allele)

    # Calculate Max Buy & Sell Power
    for allele in alleles:
        # get position (buy/sell)
        pos = allele_helper.decode_position( allele[0:1] )
        if pos == "+":
            # buy allele
            power = allele_helper.decode_power( allele[9:10] )
            BUY_POWER_SUM += power
        elif pos == "-":
            # sell allele
            power = allele_helper.decode_power( allele[9:10] )
            SELL_POWER_SUM += power
        else:
            # error

    
    # Generate Buy Limit, if necessary
    if buy_limit is None:
        # generate random number from (0, BUY_POWER_SUM)
        buy_limit = random.randint(0, BUY_POWER_SUM)
        
    # Generate Sell Limit, if necessary
    if sell_limit is None:
        # generate random number from (0, SELL_POWER_SUM)
        sell_limit = random.randint(0, SELL_POWER_SUM)

    # Generate Encoding
    items = []
    items.append(buy_limit)
    items.append(sell_limit)
    for allele in alleles:
        items.append(allele)
    encoding = ",".join(items)

    # Return Generated Encoding
    return encoding



"""          """
""" Decoding """
"""          """
def decode_limit( numb_string ):
    # Check if numb_string is a valid int
    try:
        int( numb_string )
    except ValueError:
        # Otherwise, return NoneType
        print("< ERR > : Error decoding genome : Limit.")
        return None
    
    # Return 'numb_string' as int
    return int( numb_string )

"""          """
""" Encoding """
"""          """
def encode_limit( limit ):
    # Check if limit is a valid float
    try:
        float( limit )
    except ValueError:
        # Otherwise, return NoneType
        print("< ERR > : Error encoding genome : Limit.")
        return None

    # Return 'limit' as string
    return str(limit)



"""          """
""" Mutation """
"""          """
def should_mutate( mutate_prob ):
    # Determine if mutate should occur
    result = random.random()
    if result < mutate_prob:
        return True

    return False

def mutate_limit():
    return 0

def mutate_alleles( alleles ):
    mut_alleles = []
    for allele in a
    return 0



"""           """
""" Crossover """
"""           """
# def crossover(genomes, n_offspring):
def crossover(genome_1, genome_2, cross_rate):
    # Initialize Mate Pool
    mates = [genome_1, genome_2]

    # Initialize Allele Pool
    #allele_pool = []
    #for mate in mates:
    #    alleles = mate.encoding.split(",")[2:0]
    #    for allele in alleles:
    #        allele_pool.append( allele )

    # Produce New Allele Sets
    cross_amt = int((1-cross_rate) * ALLELES_PER_GENOME) % ALLELES_PER_GENOME
    alleles_1 = genome_1.encoding.split(",")[2:]
    alleles_2 = genome_2.encoding.split(",")[2:]
    new_alleles_1 = alleles_1[:cross_amt] + alleles_2[cross_amt:]
    new_alleles_2 = alleles_2[:cross_amt] + alleles_1[cross_amt:]

    # Produce Offspring
    buy_limits = [genome_1.buy_limit, genome_2.buy_limit]
    sell_limits = [genome_1.sell_limit, genome_2.sell_limit]
    alleles = [new_alleles_1, new_alleles_2]

    offspring_1 = ",".join([buy_limits.pop(random.randint(0,1)) +
                            sell_limits.pop(random.randint(0,1))] +
                           alleles.pop(random.randint(0,1)))

    offspring_2 = ",".join([buy_limits.pop() +
                            sell_limits.pop()] +
                           alleles.pop())
    
    # Return Offspring
    return [offspring_1, offspring_2]






