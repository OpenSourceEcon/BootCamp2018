class ContentFilter:
    def __init__(self, filename): 
        exists = False
        while not exists:
            try:
                with open(filename, 'r') as readfile:
                    exists = True
                    self.filename = filename
                    self.content = readfile.read()
                    self.numlines = len(readfile.readlines())
            except:
                filename = input("Please enter a valid file name: ")
        self.numchars = len(self.content)
        self.numalphas = sum(c.isalpha() for c in self.content)
        self.numdigits = sum(c.isdigit() for c in self.content)
        self.numspaces = sum(c.isspace() for c in self.content)

    def uniform(self, writefile, mode='w', case='upper'):
        valid = ['w', 'x', 'a']
        if mode not in valid:
            raise ValueError("This is not a valid mode. Change to 'x', 'w' or 'a'")
        if case == 'upper':
            writethis = self.content.upper()
        elif case == 'lower':
            writethis = self.content.lower()
        else:
            raise ValueError("This is not a valid case.  Use upper or lower")
        with open(writefile, mode) as outfile:
            outfile.write(writethis + '\n')

    def reverse(self, writefile, mode='w', unit='line'):
        valid = {'w', 'x', 'a'}
        valid.add(mode)
        if len(valid) != 3:
            raise ValueError("This is not a valid mode. Change to 'x', 'w' or 'a'")
        if unit == 'line':
            wordlist = self.content.split('\n')
            newwordlist = wordlist[::-1]
            writethis = "\n".join(newwordlist)
        elif unit == 'word':
            wordlist = self.content.split('\n')
            newwordlist = wordlist
            for i in range(len(wordlist)):
                newwordlist[i] = wordlist[i][::-1]
            writethis = "\n".join(newwordlist)
        else:
            raise ValueError("This is not a valid unit.  Use line or word")
        with open(writefile, mode) as outfile:
            outfile.write(writethis + '\n')

    def transpose(self, writefile, mode='w'):
        valid = {'w', 'x', 'a'}
        valid.add(mode)
        if len(valid) != 3:
            raise ValueError("This is not a valid mode. Change to 'x', 'w' or 'a'")
        lines = self.content.split('\n')
        matrix = []
        for i in range(len(lines)):
            matrix.append(lines[i].split(' '))
        matrix = [*zip(*matrix)]
        for j in range(len(matrix)):
            matrix[j] = " ".join(matrix[j])
        writethis = "\n".join(matrix)
        with open(writefile, mode) as outfile:
            outfile.write(writethis + '\n')

    def __str__(self):
        string = str("Source File:\t\t\t" + str(self.filename) +
        "\nTotal characters:\t\t" + str(self.numchars) + "\nAlphabetic characters:\t\t" +
        str(self.numalphas) + "\nNumerical characters:\t\t" + str(self.numdigits) +
        "\nWhitespace characters:\t\t" + str(self.numspaces) +
        "\nNumber of lines:\t\t" + str(self.numlines))
        return string