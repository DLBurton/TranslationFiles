__author__ = 'darrenburton'


"""
This is a script to pull all translation files that are passed to us and output the required translated files as required
by the server, ios and Android
"""


import os, fnmatch, sys
from utils import Translate_Files
import datetime
import argparse



def KiteArguments() :

    parser = argparse.ArgumentParser(description='Translate some files.')
    parser.add_argument('--verbose', dest='verbose', action='store_true', help='Print to screen')
    parser.set_defaults(verbose=False)

    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-f', '--file', dest='file', help='Add folder path', required=True)

    args = parser.parse_args()

    return args


if __name__ == "__main__":



    arguments = KiteArguments()

    now = datetime.datetime.now()

    kite_folder = Translate_Files('Kite_Translations_' + now.strftime('%d-%m-%Y_%H-%M-%S'), verbose=arguments.verbose, input_file=arguments.file)

    kite_folder.parse_files()
