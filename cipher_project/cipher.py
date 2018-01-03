class Cipher():

    """Grid will hold the coordinants for the Alphabet for
    use in the Bifid Cipher only. Also the bifid_cipher_dict has
    the coordinates as keys and the letters and characters of the alphabet as
    values.
    Cipher takes in a messsge parameter as a string.
    """

    GRID = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
        (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),
        (0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2),
        (0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(8,3),
        (0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4),
        (0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5),
        (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6),
        (0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7),
        (0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8),]

    ALPHABET = [('A'),('B'),('C'),('D'),('E'),('F'),('G'), ('H'),('I')
            ,('J'),('K'),('L'),('M'),('N'),('O'),('P'),('Q'),('R')
            ,('S'),('T'),('U'),('V'),('W'),('X'),('Y'),('Z'),('0')
            ,('1'),('2'),('3'),('4'),('5'),('6'),('7'),('8'),('9')
            ,('a'),('b'),('c'),('d'),('e'),('f'),('g'),('h'),('i')
            ,('j'),('k'),('l'),('m'),('n'),('o'),('p'),('q'),('r')
            ,('s'),('t'),('u'),('v'),('w'),('x'),('y'),('z'),(' ')
            ,('.'),(','),(';'),(':'),('?'),('!'),('"'),("'"),('-')
            ,('('),(')'),('['),(']'),('{'),('}'),('$'),('='),('%')
           ]


    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return str(self.message)
