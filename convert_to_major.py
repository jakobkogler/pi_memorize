"""Converts a number into words using a major system."""
import argparse


class ConverterMajorSystem():
    """class for converting a number to words using the major system."""

    def __init__(self, path):
        """Initialize class and copy path to major system."""
        super(ConverterMajorSystem, self).__init__()
        self.major_list = self.read_major_list(path)

    def read_major_list(self, path):
        """Read the csv-file of a major list and return the parsed list as dict."""
        try:
            major_list = dict()
            with open(path, 'r') as file:
                for line in file:
                    number, word = line.split(';')
                    major_list[number] = word
            return major_list
        except (IOError, OSError):
            print('Some errors occured while reading the major-list file.')
            print('Check, if the path to the file is correct and if the file is in the correct format.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts a number into words using a major system')
    parser.add_argument('major_list', help='file containing a major list in csv-format')

    args = parser.parse_args()
    converter = ConverterMajorSystem(args.major_list)
