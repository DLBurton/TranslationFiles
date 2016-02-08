__author__ = 'darrenburton'

from base_parser import BaseParser
import os
import csv

class AppleParser(BaseParser):

    def _go_csv(self):
        pass

    def _go_parse(self):

        #Ok first lets get all the files that currently exist within the input folder
        for root, dirs, files in os.walk(self._input_folder):
            for file in files:
                if file.endswith(".csv"):
                    self.parse_as_strings(input_file=os.path.join(root, file),
                                      output_file=os.path.join(self._output_folder, os.path.splitext(file)[0])+'.strings')


    def parse_as_strings(self, input_file=None, output_file=None):

         if self.verbose: print("   Generating iOS SDK .strings File :" + output_file + " from file : " + input_file)

         csvData = csv.reader(open(input_file))
         csvData.next()
         csvData.next()

         header = csvData.next()

         for index in range(2, len(header)):
            stringsFile = open(output_file[0:-8] + '_' + header[index] + '.strings', 'w')

            inner_csvData = csv.reader(open(input_file))
            inner_csvData.next()
            inner_csvData.next()
            inner_csvData.next()

            fileString = ""

            for row in inner_csvData:
                if row[0]:
                    fileString += "/* No comment provided by engineer. */ \n"
                    fileString += row[0] + "\"" + row[index] + '\"; \n\n\n'

            stringsFile.write(fileString)


