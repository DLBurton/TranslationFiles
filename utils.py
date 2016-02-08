__author__ = 'darrenburton'


import errno
import os
from parsers.android import AndroidParser
from parsers.ios import AppleParser
from parsers.server import ServerParser

class Translate_Files(object):

    def __init__(self, folder_name, verbose=False, input_file=None):

        self.verbose = verbose
        self._folder_name = folder_name
        self.input_file = input_file
        self.android_path = None
        self.apple_path = None
        self.server_path = None

        self._create_directory()

    def _create_directory(self):

        if not self._dir_exists(self.input_file):
            raise Exception('Input folder does not exist')

        if self.verbose: print("Creating Folder : " + self._folder_name)

        directories = {'Server': 'server_path', 'Android':  'android_path', 'Apple': 'apple_path'}

        self._mkdir_p(self._folder_name)

        for dir in directories:

            if self._dir_exists(os.path.join(self.input_file, dir)):
                if self.verbose: print("Creating SubFolder : " + os.path.join(self._folder_name, dir))
                self._mkdir_p(os.path.join(self._folder_name, dir))
                #Now we set the attributes for that the parsers can get at them later
                setattr(self, directories[dir], os.path.join(self._folder_name, dir))

    def _dir_exists(self, path):
        return os.path.isdir(path)

    def _mkdir_p(self, path):
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise


    def parse_files(self):

        AndroidParser(input_folder=os.path.join(self.input_file, 'Android'), output_folder=self.android_path, verbose=self.verbose)
        AppleParser(input_folder=os.path.join(self.input_file, 'Apple'), output_folder=self.apple_path, verbose=self.verbose)
        ServerParser(input_folder=os.path.join(self.input_file, 'Server'), output_folder=self.server_path, verbose=self.verbose)

