__author__ = 'darrenburton'

from base_parser import BaseParser
import os
import csv
from shutil import copyfile

class ServerParser(BaseParser):

    def _go_parse(self):

        #Ok first lets get all the files that currently exist within the input folder
        for root, dirs, files in os.walk(self._input_folder):
            for file in files:
                if 'Django' in file:
                    self.parse_as_po(input_file=os.path.join(root, file),
                                      output_file=os.path.join(self._output_folder, os.path.splitext(file)[0])+'.po')
                elif file.endswith(".csv"):
                    self.parse_as_csv(input_file=os.path.join(root, file),
                                      output_file=os.path.join(self._output_folder, os.path.splitext(file)[0])+'.csv')


    def parse_as_csv(self, input_file=None, output_file=None):

        if self.verbose: print("    Generating CSV File :" + output_file + " from file : " + input_file)
        copyfile(input_file, output_file)


    def parse_as_po(self, input_file=None, output_file=None):

        if self.verbose: print("    Generating PO File :" + output_file + " from file : " + input_file)

        csvData = csv.reader(open(input_file))

        header = csvData.next()

        for index in range(2, len(header)):
            poFile = open(output_file[0:-3] + '_' + header[index] + '.po', 'w')

            inner_csvData = csv.reader(open(input_file))
            inner_csvData.next()

            fileString = ""

            for row in inner_csvData:
                if row[1]:
                    fileString += "msgid \"" + row[1] + "\"\n"
                    fileString += "msgstr \"" +  row[index] + "\"\n\n"

            poFile.write(fileString)





