""" ECSTIA """

""" Sample Encoding 1 : +S356.23<9 -> +, S, 356.23, <, 9 """
""" Sample Decoding 1 : if (tech_ind[S].data < 356.234): BUY * 9 """

""" Sample Encoding 1 : -a1.3234>4 -> -, a, 1.3234, >, 4 """
""" Sample Decoding 1 : if (tech_ind[a].data > 1.3234): SELL * 4 """

""" if ( threshold <cond> tech_ind.val) """



import allele_helper as helper



""" Allele Characteristics """
ENCODING_SIZE = 10

""" Mutation Variables """
POS_MUT_PROB = 0.25
TECH_IND_MUT_PROB = 0.25
THRESHOLD_MUT_PROB = 0.25
CONDITION_MUT_PROB = 0.25
POWER_MUT_PROB = 0.25

class Allele(object):
    """
    Initialize & Verify The Allele
    """
    def __init__(self, encoding=None):
        if encoding is None:
            encoding = helper.generate_encoding()
        
        self.encoding = encoding

        # Hydrate The Allele (Initialize)
        if self.hydrate() is None:
            print("< ERR > : Failed to hydrate allele, invalid encoding! {}".format(encoding))
            self = None
            
        # Verify The Allele
        if self.verify() is False:
            print("< ERR > : Failed to verify allele, invalid encoding! {}".format(encoding))
            self = None

        return



    """
    Initializes Variables For Allele From Encoding
    """
    def hydrate(self):
        # Sanity Check
        if self.encoding is None:
            return None

        # Decode Position (buy:sell)
        self.pos = helper.decode_position( self.encoding[0:1] )
        # Decode Technical Indicator
        self.tech_ind = helper.decode_tech_ind( self.encoding[1:2] )
        # Decode Threshold (for technical indicator) 
        self.threshold = helper.decode_threshold( self.encoding[2:8] )
        # Decode Condition
        self.condition = helper.decode_condition( self.encoding[8:9] )
        # Decode Power (of decision)
        self.power = helper.decode_power( self.encoding[9:10] )

        return 1

    

    """
    Encodes & Returns The Current State Of The Allele
    """
    def dehydrate(self):
        # Encode Position (buy:sell)
        pos = helper.encode_position(self.pos)
        # Encode Technical Indicator
        tech_ind = helper.encode_tech_ind(self.tech_ind)
        # Encode Threshold (for technical indicator) 
        threshold = helper.encode_threshold(self.threshold)
        # Encode Condition
        condition = helper.encode_condition(self.condition)
        # Encode Power (of decision)
        power = helper.encode_power(self.power)

        # Check That All Passed Encoding
        if pos is None or tech_ind is None or threshold is None or condition is None or power is None:
            print("< ERR > : Failed to dehydrate allele, invalid allele state!")
            return None

        # Form Encoding
        encoding = pos + tech_ind + threshold + condition + power

        # Return Encoding
        return encoding
    


    """
    Verifies The Initialization Of An Allele
    """
    def verify(self):
        # Verify Encoding
        if len(self.encoding) is not ENCODING_SIZE:
            return None
        # Verify Position
        if self.pos is None:
            return False
        # Verify Technical Indicator
        if self.tech_ind is None:
            return False
        # Verify Threshold
        if self.threshold is None:
            return False
        # Verify Condition
        if self.condition is None:
            return False
        # Verify Power
        if self.power is None:
            return False

        # Passed Verification
        return True



    """
    Returns A Mutation Of The Current Encoding
    """
    def mutate( self, radiation=1.0 ):
        old_encoding = self.encoding

        # Mutate Position
        mut_pos = helper.mutate_position( old_encoding[0:1], POS_MUT_PROB * radiation)
        # Mutate Technical Indicator
        mut_tech_ind = helper.mutate_tech_indicator( old_encoding[1:2], TECH_IND_MUT_PROB * radiation)
        # Mutate Threshold
        mut_threshold = helper.mutate_threshold( old_encoding[2:8], THRESHOLD_MUT_PROB * radiation)
        # Mutate Condition
        mut_condition = helper.mutate_condition( old_encoding[8:9], CONDITION_MUT_PROB * radiation)
        # Mutate Power
        mut_power = helper.mutate_power( old_encoding[9:10], POWER_MUT_PROB * radiation)

        # Update Encoding
        new_encoding = mut_pos + mut_tech_ind + mut_threshold[0:6] + mut_condition + mut_power
        self.encoding = new_encoding

        # Hydrate The Allele (Initialize)
        if self.hydrate() is None:
            print("< ERR > : Failed to hydrate allele, invalid encoding! {}".format(encoding))
            self = None
            
        # Verify The Allele
        if self.verify() is False:
            print("< ERR > : Failed to verify allele, invalid encoding! {}".format(encoding))
            self = None

        # Return
        return
    


    """
    Returns A Reaction From The Allele
    """
    def react( self, input_data ):
        if (self.condition == '<'): # Less Than
            
            if ( input_data < self.threshold ): # Condition Met    
                return 1 + self.power
            
            return 0 # Condition Not Met
    
        elif (self.condition == '>'): # Greater Than

            if ( input_data > self.threshold ): # Condition Met
                return 1 + self.power
    
            return 0 # Condition Not Met
            
        # Allele Corrupted
        print("< ERR > : Error in allele reaction, invalid condition! {}".format(self.encoding))
        return None


    """
    Returns String Representation Of The Allele
    """
    def as_string( self ):
        position = "SELL"
        if self.pos == 1:
            position = "BUY"
        
        return "if ( {}(t) {} {} ) -> {} {} VOTES".format(self.tech_ind,
                                                    self.condition,
                                                    self.threshold,
                                                    self.power + 1,
                                                    position)



"""
Returns A Crossover(s) Of This Allele & The Passed Allele
"""
def crossover(allele_a, allele_b, n_offspring):
    # Generate N Offspring From Parent Crossover
    offspring = helper.crossover(allele_a, allele_b, n_offspring)

    # Return Offspring (Size Adjusted)
    return offspring[:n_offspring]


                  
