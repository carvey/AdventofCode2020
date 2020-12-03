import sys

policy_fle = open(sys.argv[1])
policies = policy_fle.read().strip().split('\n')
policy_fle.close()


class PolCheck:

    def __init__(self, raw):
        self.raw = raw

        self.char = None
        self.min = None
        self.max = None
        self.password = None

        # these are for the second interpretation
        self.position1 = None
        self.position2 = None

        self.parse()

    def parse(self):
        raw_split = self.raw.split(' ') # ex: ['5-6', 'w:', 'wwwfkc']
        char_min, char_max = raw_split[0].split('-')

        self.min = int(char_min)
        self.max = int(char_max)

        # setting these to different names for clarity on interpretation 2
        # subtracting 1 to take into account 1 based indexing
        self.position1 = self.min - 1
        self.position2 = self.max - 1 

        self.char = raw_split[1].replace(':', '')

        self.password = raw_split[2]

        
    def valid_summation(self):
        """
        This validation checks the first interpretation where the number of occurrences of
        'char' have to fall within the specified range
        """
        count = self.password.count(self.char)
        if count in range(self.min, self.max+1):
            return True

        return False

    def valid_occurrence(self):
        """
        This validation checks the second interpretation where 'password' has to have 'char'
        at index 'position1' or 'position2' using 1 based indexing
        """
        chars = (self.password[self.position1], self.password[self.position2])
        if chars.count(self.char) == 1:
            return True

        return False

valid_pass_count_summation = 0 # for interpretation 1
valid_pass_count_occurrence = 0 # for interpretation 2

for pol in policies:
    polcheck = PolCheck(pol)

    if polcheck.valid_summation():
        valid_pass_count_summation += 1

    if polcheck.valid_occurrence():
        valid_pass_count_occurrence += 1
    

print("First interpretation: %s" % valid_pass_count_summation)
print("Second interpretation: %s" % valid_pass_count_occurrence)
