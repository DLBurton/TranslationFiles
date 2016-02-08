__author__ = 'darrenburton'


import errno
import os


class BaseParser(object):

    def __init__(self, input_folder=None, output_folder=None, verbose=False ):

        self.verbose = verbose

        self._input_folder = input_folder
        self._output_folder = output_folder

        if self._validate_parse_required():
            if self.verbose: print("Parsing and creating files for :" + self._output_folder)
            self._go_parse()

        else:
            if self.verbose: print("Not creating folder as no input files passed to : " + self._get_subclass_name())

    def _get_subclass_name(self):
        return self.__class__.__name__

    def _validate_parse_required(self):

        return True if self._output_folder else False

    def _go_parse(self):
        raise NotImplementedError

