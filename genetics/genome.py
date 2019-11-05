""" Full Genotype Individuals """

""" Sample Genome Encoding : BuyLimit,SellLimit,Allele,Allele,Allele,...,Allele """



import genome_helper as helper



""" Genome Characteristics """
ALLELES_PER_GENOME = 23

""" Mutation Variables """
LIMIT_MUT_PROB = 0.25

class Genome(object):
    """
    Initialize & Verify The Genome
    """
    def __init__(self, encoding=None):
        if encoding is None:
            encoding = helper.generate_encoding()
        
        self.encoding = encoding
        self.alleles = []
        
        # Hydrate The Genome (Initialize)
        if self.hydrate() is None:
            print("< ERR > : Failed to hydrate genome, invalid encoding!\n{}".format(encoding))
            self = None

        # Verify The Genome 
        if self.verify() is False:
            print("< ERR > : Failed to verify genome, invalid encoding!\n{}".format(encoding))
            self = None

        return


    """
    Initializes Variables For Genome From Encoding
    """
    def hydrate(self):
        # Sanity Check
        if self.encoding is None:
            return None

        # Unwrap Encoding
        items = self.encoding.split(',')

        # Decode Buy & Sell Limits
        self.buy_limit = decode_limit( items[0] )
        self.sell_limit = decode_limit( items[1] )
        
        # Decode Alleles
        genes = items[2:]
        for gene in genes:
            allele = Allele( gene )
            self.alleles.append( allele )

        return 1
            

    """
    Encodes & Returns The Current State Of The Genome
    """
    def dehydrate( self ):
        items = []
        # Encode & Append Buy Limit
        buy_limit = helper.encode_limit( self.buy_limit )
        # Encode & Append Sell Limit
        sell_limit = helper.encode_limit( self.sell_limit )
        # Encode & Append Alleles
        alleles = []
        for allele in self.alleles:
            dna = allele.dehydrate()
            if dna is None:
                print("< ERR > : Failed to dehydrate genome, invalid allele state!")
                return None
            alleles.append( dna )
            
        # Check That All Passed Encoding
        if buy_limit is None or sell_limit is None or len(alleles) != ALLELES_PER_GENOME:
            print("< ERR > : Failed to dehydrate genome, invalid allele state!")
            return None

        # Form Encoding
        items.append( buy_limit )
        items.append( sell_limit )
        items += alleles
        encoding = ",".join(items)

        # Return Encoding
        return encoding

    """
    Verify The Initialization Of A Genome
    """
    def verify( self ):
        # Verify Buy Limit
        if self.buy_limit is None:
            return False
        # Verify Sell Limit
        if self.sell_limit is None:
            return False
        # Verify Alleles
        if len(self.alleles) != ALLELES_PER_GENOME:
            return False
        else:
            for allele in self.alleles:
                # Verify Each Allele
                if allele is None:
                    return False

        # Passed Verification
        return True
    
    """
    Returns A Mutation Of The Current Encoding
    """
    def mutate( self, radiation=1.0 ):
        old_encoding = self.encoding

        # Mutate Buy Limit
        mut_buy_limit = self.buy_limit
        if random.uniform(0, 1) < LIMIT_MUT_PROB:
            mut_buy_limit += random.randint(-1, 1)
        
        # Mutate Sell Limit
        mut_sell_limit = self.sell_limit
        if random.uniform(0, 1) < LIMIT_MUT_PROB:
            mut_sell_limit += random.randint(-1, 1)

        # Fix potential buy/sell limit overlap
        while mut_buy_limit < mut_sell_limit:
            # normalize extreme limit
            if mut_buy_limit < 0:
                mut_buy_limit += 1
            elif mut_sell_limit > 0:
                mut_sell_limit -= 1
                
        # Mutate Alleles
        mut_alleles = []
        for allele in self.alleles:
            mut_allele = allele.mutate()
            mut_alleles.append( mut_allele )

        # Update Encoding
        new_encoding = []
        new_encoding.append( mut_buy_limit )
        new_encoding.append( mut_sell_limit )
        new_encoding.extend( mut_alleles )
        new_encoding = ",".join(new_encoding)
        #self.encoding = new_encoding

        # Return Encoding
        return new_encoding


    
    """
    Returns A Reaction From The Genome
    """
    def react( self, row_dict ):
        # Initialize pressure
        pressure = 0

        # Summate Pressure
        for allele in self.alleles:
            value = row_dict[ allele.tech_ind ]
            # Verify data
            if value is None:
                # Data corrupted
                print("< ERR > : Error in genome reaction, data corrupted!",
                      " Could not find key {}.".format(allele.tech_id))
                return None
            
            pressure += allele.react( value )
            
        # Return Decision
        if pressure > self.buy_limit and not (pressure < self.sell_limit):
            return "BUY"
        elif pressure < self.sell_limit and not (pressure > self.buy_limit):
            return "SELL"
        elif pressure >= self.buy_limit and pressure <= self.sell_limit:
            return "HOLD"

        # Genome Corrupted
        print("< ERR > : Error in genome reaction!")
        return None



    """
    Returns String Representation Of The Genome
    """
    def as_string( self ):
        print("Genome As String")


"""
Returns N Crossovers Between Two Genomes
"""
def crossover(genome_a, genome_b, cross_rate): #n_offspring):
        return helper.crossover(genome_a,genome_b,cross_rate)
        
