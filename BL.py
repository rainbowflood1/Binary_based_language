class BL:
    seq_pos = 0
    seq = []
    def __init__(self, bit=8):
        self.bit = bit
    bit = 8
    operators = {
        ("0"*(bit-len("1"))+"1"): None
    }

    def binaryTodecimal(n):
        decimal = 0
        power = 1
        while n>0:
            rem = n%10
            n = n//10
            decimal += rem*power
            power = power*2
            
        return bin(decimal)

    def string_to_bin(self, str):
        self.seq = str.split(" ")
    def read_bin(self):
        for self.seq_pos in range(0, len(self.seq)):
            print(self.seq_pos)
            print(self.seq[self.seq_pos])
