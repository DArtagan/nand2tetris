class instruction:
    binary = ''

    def __str__(self):
        return self.binary

    def parse(self, line):
        line = line.strip()
        line = line.replace('<',';')
        line = line.replace('>',';')
        output = line.split(';')
        return str(output[2])


class a_instruction(instruction):
    def __init__(self, constant):
        self.binary = '@' + self.parse(constant)


class c_instruction(instruction):
    def __init__(self, comp, dest, jump):
        try:
            temp_bin = bin(int(self.parse(comp),16))[2:].zfill(8)
            temp_bin = str(temp_bin)[1:]
            print(temp_bin)
            self.comp = self.comp_dict[temp_bin]
        except:
            self.comp = self.parse(comp)
            self.comp = self.comp[2:]
            self.comp = 'X' + self.comp
        self.dest = self.dest_dict[self.parse(dest)]
        self.jump = self.jump_dict[self.parse(jump)]

        if self.dest != 'null':
            self.binary += self.dest + '='
        if self.comp != 'null':
            self.binary += self.comp
        if self.jump != 'null':
            self.binary += ';' + self.jump

    dest_dict = {'000': 'null',
            '001': 'M',
            '010': 'D',
            '011': 'MD',
            '100': 'A',
            '101': 'AM',
            '110': 'AD',
            '111': 'AMD',}

    jump_dict = {'000': 'null',
            '001': 'JGT',
            '010': 'JEQ',
            '011': 'JGE',
            '100': 'JLT',
            '101': 'JNE',
            '110': 'JLE',
            '111': 'JMP',}

    comp_dict = {'0101010': '0',
                 '0111111': '1',
                 '0111010': '-1',
                 '0001100': 'D',
                 '0110000': 'A',
                 '0001101': '!D',
                 '0110011': '!A',
                 '0001111': '-D',
                 '0110011': '-A',
                 '0011111': 'D+1',
                 '0110111': 'A+1',
                 '0001110': 'D-1',
                 '0110010': 'A-1',
                 '0000010': 'D+A',
                 '0010011': 'D-A',
                 '0000111': 'A-D',
                 '0000000': 'D&A',
                 '0010101': 'D|A',
                 '1110000': 'M',
                 '1110001': '!M',
                 '1110011': '-M',
                 '1110111': 'M+1',
                 '1110010': 'M-1',
                 '1000010': 'D+M',
                 '1010011': 'D-M',
                 '1000111': 'M-D',
                 '1000000': 'D&M',
                 '1010101': 'D|M',}
 
