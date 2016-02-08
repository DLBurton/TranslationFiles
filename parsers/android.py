__author__ = 'darrenburton'

from base_parser import BaseParser
import os
import csv
from lxml import etree


class AndroidParser(BaseParser):

    def _go_csv(self):

        #Ok first lets get all the files that currently exist within the input folder
        for root, dirs, files in os.walk(self._input_folder):
            for file in files:
                if file.endswith(".xml"):
                    self.parse_for_translation(input_file=os.path.join(root, file),
                                      output_file=os.path.join(self._output_folder, os.path.splitext(file)[0])+'.csv')



    def _go_parse(self):

        #Ok first lets get all the files that currently exist within the input folder
        for root, dirs, files in os.walk(self._input_folder):
            for file in files:
                if file.endswith(".csv"):
                    self.parse_as_xml(input_file=os.path.join(root, file),
                                      output_file=os.path.join(self._output_folder, os.path.splitext(file)[0])+'.xml')


    def parse_for_translation(self, input_file=None, output_file=None):


        if self.verbose: print("    Generating CSV Translation File :" + output_file + " from file : " + input_file)

        field_names = ['attribute', 'english']

        outFile = open(output_file, 'w')
        write = csv.DictWriter(outFile, field_names)

        header = {'attribute': 'Attribute For App', 'english' : 'English'}
        write.writerow(header)

        for event,rec in etree.iterparse(input_file):
            row=dict()
            for child in rec:
                row['attribute'] = child.attrib['name']  if 'name' in child.attrib else ""
                row['english'] = child.text

                write.writerow(row)

        outFile.close()

    def parse_as_xml(self, input_file=None, output_file=None):

        if self.verbose: print("    Generating XML File :" + output_file + " from file : " + input_file)

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
                if row[0]:
                    string = etree.SubElement(root, 'string', name=row[0].decode('utf-8'))
                    string.text = row[index].decode('utf-8')


            result = etree.tostring(root, pretty_print=True)
            xmlFile.write(result)







