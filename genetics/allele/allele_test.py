import allele as ale
import random

def random_allele():
    allele = ale.Allele( None )
    return allele

def build_allele( encoding ):
    allele = ale.Allele( encoding )
    return allele

def bad_allele():
    allele = ale.Allele( "00000ABCDE" )
    return allele

def deep_test():
    GEN = 0
    MAX_GEN = 1000
    
    POP_SIZE = 100
    POPULATION = []

    # Initialize Population
    while len(POPULATION) < POP_SIZE:
        POPULATION.append(random_allele()) # TEST : Random Generation, Hydration, Verification

    # Simulate Evolution
    while GEN <= MAX_GEN:
        # Select 'Best' Individuals
        survivors = []
        while len(survivors) < POP_SIZE/2:
            parent = random.choice(POPULATION)
            parent_dna = parent.dehydrate() # TEST : Dehydration
            if parent_dna != parent.encoding:
                print("ERROR DEHYDRATION, ENCODING DID NOT MATCH ORIGINAL. {} != {}".format(parent.encoding, parent_dna))

            survivors.append(parent_dna)

        # Re-Initialize Parents & Mutate
        parents = []
        for survivor in survivors:
            parent = build_allele(survivor) # TEST : Given Generation, Hydration, Verification
            parents.append( parent )

        # Create Offspring
        offspring = []
        while len(offspring) < POP_SIZE:
            parent_1 = random.choice(parents)
            parent_2 = random.choice(parents)
            
            children = ale.crossover(parent_1, parent_2, 2) # Test Crossover

            if len(children) != 2:
                print("ERROR CROSSOVER, CHILDREN DID NOT MATCH 2 != {}".format(len(children)))

            for child in children:
                new_allele = build_allele( child )
                new_allele.mutate()
                offspring.append( new_allele )

        # Replace Population
        POPULATION = offspring.copy()

        print( GEN )
        GEN += 1

    for ind in POPULATION:
        print(ind.as_string())

deep_test()









    
