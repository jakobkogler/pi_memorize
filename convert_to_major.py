"""Converts a number into words using a major system."""
import argparse


class ConverterMajorSystem():
    """Class for converting a number to words using the major system."""

    def __init__(self, path):
        """Initialize class and copy path to major system."""
        super(ConverterMajorSystem, self).__init__()
        self.major_list = self.__read_major_list(path)

    @staticmethod
    def __read_major_list(path):
        """Read the csv-file of a major list and return the parsed list as dict."""
        major_list = dict()
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                number, word = line.split(';')
                major_list[number] = word
        return major_list

    def convert(self, numbers):
        """Convert numbers to words."""
        number_groups = [numbers[idx:idx+3] for idx in range(0, len(numbers), 3)]
        template = 'Index {index:4}, Digits {digits}: {words}'
        output = [template.format(index=idx*3+1, digits=group,
                                  words=self.major_list[group])
                  for idx, group in enumerate(number_groups)]
        return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts a number into words using a major system')
    parser.add_argument('major_list', help='file containing a major list in csv-format')
    parser.add_argument('--group', type=int, default=5, help='group words into sentences (default: 5)')

    args = parser.parse_args()
    converter = ConverterMajorSystem(args.major_list)

    numbers = input()
    for idx, line in enumerate(converter.convert(numbers)):
        print(line)
        if (idx + 1) % args.group == 0:
            print()
