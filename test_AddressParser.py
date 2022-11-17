from unittest import TestCase
from AddressParser import AddressParser
import json

class AddressParserTest(TestCase):
    def _assert_match_address(self, test_data):
        for input_line, expected_output in test_data:
            parser = AddressParser(input_line)
            x  = parser.regex_matcher()
            print(x)
            self.assertEqual(
            expected_output,
            AddressParser(address= input_line).regex_matcher()
            )
    
    def test_simple_addresses(self):
        test_data = (
            ("Winterallee 3", json.dumps({"street": "Winterallee", "housenumber": "3"})),
            ("Musterstrasse 45", json.dumps({"street": "Musterstrasse", "housenumber": "45"})),
            ("Blaufeldweg 123B", json.dumps({"street": "Blaufeldweg", "housenumber": "123B"}))
        )
        self._assert_match_address(test_data)

    def test_complicated_addresses(self):
        test_data = (
            ("Am Bächle 23", json.dumps({"street": "Am Bächle", "housenumber": "23"}, ensure_ascii=False)),
            ("Auf der Vogelwiese 23 b", json.dumps({"street": "Auf der Vogelwiese", "housenumber": "23 b"}))
        )
        self._assert_match_address(test_data)

    def test_other_countries_addresses(self):
        test_data = (
            ("4, rue de la revolution", json.dumps({"street": "rue de la revolution", "housenumber": "4"})),
            ("200 Broadway Av", json.dumps({"street": "Broadway Av", "housenumber": "200"})),
            ("Calle Aduana, 29", json.dumps({"street": "Calle Aduana", "housenumber": "29"})),
            ("Calle 39 No 1540", json.dumps({"street": "Calle 39", "housenumber": "No 1540"}))
        )
        self._assert_match_address(test_data)

