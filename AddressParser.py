from logging import exception
import unittest
import re
import yaml
import json

class AddressParser():
    def __init__(self, address: str):
        self.raw_address = address
        self.config_file_path = "./config/regex_patterns.yaml"
        self.street_regex, self.house_number_regex = self._regex_reader()

    def _regex_reader(self):
        """
        This function reads the Yaml file which contains the Regex Sets.
        :param config_file_path: This param has been defined already in the __init__ of the AddressParser Class.

        :return: A List of Regex Patterns either for Street Name or House Number Parts.
        """
        yaml_file = self.config_file_path
        try:
            with open(file=yaml_file) as f:
             patterns = yaml.safe_load(f)
            street_name_patterns = patterns['Street_Name']
            house_number_patterns = patterns['House_Number']
            return [street_name_patterns, house_number_patterns]
        except FileNotFoundError as e:
            print("Yaml Config file couldn't be read successfully due to the following error: {0}".format(e))

    def _format_street_name(self, street_name: list):
        """
        This function formats the street name part after matched with a Regex already.
        :param street_name: A List contians 1 element which reflects to the output of "findall" method.

        :return: A Formattted String without any whitespace(s) or Commas or "No"
        """
        street_name_element = street_name[0]
        street_name_element = street_name_element.replace(" No", "")
        street_name_element = street_name_element.replace(", ", "")
        street_name_element = street_name_element.replace(",", "")
        street_name_element = street_name_element.strip()

        return street_name_element

    def _output_to_json(self, street_name: str, house_number: str):
        """
        This function creates new JSON Object for each extracted Street Name & House Number with their keys.
        :param street_name: A Str defines the Street Name Part after formatting.
        :param house_number: A Str defines the House Number Part.
        
        :return: A JSON Object consisting of street name and house number with their respective keys.
        """
        output_dict = {}
        output_dict["street"] = street_name
        output_dict["housenumber"] = house_number
        returned_json = json.dumps(dict(output_dict), ensure_ascii=False)
        return returned_json

    def regex_matcher(self):
        """
        This function parses an address string into street name and house number. This function will use 
        "_format_to_string" & "_output_to_json" to get its desired output.
        Raises SyntaxError in case the address couldn't be applied to any of the predefined Regex set.
        
        :param raw_address: This variable has been defined already in __init__ part while calling the class.

        :return: A JSON Object consisting of street name and house number with their respective keys.
        """
        try:
            for pattern in self.house_number_regex:
                house_number = re.findall(pattern, self.raw_address)
                if house_number:
                    break

            for pattern in self.street_regex:
                street_name = re.findall(pattern, self.raw_address)
                if street_name:
                    formatted_street_name = self._format_street_name(street_name)
                    break
            
            json_dict = self._output_to_json(formatted_street_name, house_number[0])
            
            return json_dict
        except:
            # No match found in the config YAML file
            raise SyntaxError("Address {0} Couldn't be parsed successfully. Please Regex in your config YAML File".\
                format(self.raw_address))

if __name__ == '__main__':
    addresses_list = ["Winterallee 3", "Musterstrasse 45", "Blaufeldweg 123B", "Am Bächle 23",\
         "Auf der Vogelwiese 23 b", "4, rue de la revolution", "200 Broadway Av", "Calle Aduana, 29",\
            "Calle 39 No 1540"]
    for address in addresses_list:
        parser = AddressParser(address)
        x  = parser.regex_matcher()
        print(x)