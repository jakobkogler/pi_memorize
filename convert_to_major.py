"""Converts a number into words using a major system."""

import argparse

parser = argparse.ArgumentParser(description='Converts a number into words using a major system')
parser.add_argument('major-list', help='file containing a major list in csv-format')

args = parser.parse_args()
