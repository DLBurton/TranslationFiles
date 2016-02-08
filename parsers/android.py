__author__ = 'darrenburton'

from base_parser import BaseParser
import os
import csv
from lxml import etree


class AndroidParser(BaseParser):

    def _go_parse(self):

        #Ok first lets get all the files that currently exist within the input folder
        for root, dirs, files in os.walk(self._input_folder):
            for file in files:
                if file.endswith(".csv"):
                    print(os.path.join(root, file))
                    self.parse_as_xml(input_file=os.path.join(root, file),
                                      output_file=os.path.join(self._output_folder, os.path.splitext(file)[0])+'.xml')



    def parse_as_xml(self, input_file=None, output_file=None):

        if self.verbose: print("Generating XML File :" + output_file + " from file : " + input_file)

        csvData = csv.reader(open(input_file))
        csvData.next()

        header = csvData.next()

        for index in range(2, len(header)):
            xmlFile = open(output_file[0:-4] + '_' + header[index] + '.xml', 'w')

            inner_csvData = csv.reader(open(input_file))
            inner_csvData.next()
            inner_csvData.next()

            root = etree.Element('resources')
            for row in inner_csvData:
                string = etree.SubElement(root, 'string', name=row[0].decode('utf-8'))
                string.text = row[index].decode('utf-8')


            result = etree.tostring(root, pretty_print=True)
            xmlFile.write(result)







