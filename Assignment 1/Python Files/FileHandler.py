class FileHandler(object):
    def __init__(self, file):
        self.file = file

    def get_file(self):
        with open(self.file) as txt_file:
            half_split = []
            for line in txt_file:
                half_split.append((line.replace("\n", "")).split(','))
            #print(half_split)
            return half_split

    def write_file(self, input_content):
        open_file = open(self.file, "w")
        open_file.write(input_content)
        open_file.close()
        return input_content

file = FileHandler('written_file.csv')
file.get_file()#

"""[['Oxygen', 'Hydrogen', 'Carbon_Dioxide'], ['4500', '2500', '1053'], ['words name', 'Number Names', 'None']]"""
