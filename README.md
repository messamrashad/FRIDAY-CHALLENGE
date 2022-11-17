# Friday Challenge For Data Engineering Role

The challange was related to design an Address Parser runnning application either in Python, Pyspark, SQL to solve an issue of dectecting the Street Name(s) and House Number(s) correctly in many different formats without any conflication.

# Input/Output:

The input part is just the Address Line in _String Format_.

The output part is just the Address Line splitted correctly in _JSON Format_.

### For example: 
##### Sample Cases
* `"Winterallee 3"` -> `{"street": "Winterallee", "housenumber": "3"}`
* `"Musterstrasse 45"`-> `{"street": "Musterstrasse", "housenumber": "45"}`
* `"Blaufeldweg 123B"` -> `{"street": "Blaufeldweg", "housenumber": "123B"}`
  
##### Complicated Cases
* `"Am Bächle 23"` -> `{"street": "Am Bächle", "housenumber": "23"}`
* `"Auf der Vogelwiese 23 b"` -> `{"street": "Auf der Vogelwiese", "housenumber": "23 b"}`

##### Complex Cases
* `"4, rue de la revolution"` -> `{"street": "rue de la revolution", "housenumber": "4"}`
* `"200 Broadway Av"` -> `{"street": "Broadway Av", "housenumber": "200"}`
* `"Calle Aduana, 29"` -> `{"street": "Calle Aduana", "housenumber": "29"}`
* `"Calle 39 No 1540"` -> `{"street": "Calle 39", "housenumber": "No 1540"}`

# Prerequisites:
- Python 3.9.6 was using while developing this application.

# Implementation Notes:
1. My implementation was built on having a pre-defined Regex sets suitable for all kinds of test cases mentioned above.
2. These Regex Sets are defined for either Street Number Part or House Number Part.
3. I prefered to put these Regex Sets in format of a list elements in a YAML File as they are should be reachable/configurable easily and shouldn't be scattered in the main script.
4. AddressParser Class has 1 main method (regex_matcher) and 3 other helper methods(_regex_reader, _format_street_name, _output_to_json).
5. Unit testing has been covered in `test_AddressParser.py` script.
6. Unit testing script is testing if we are getting _JSON Format_ address or not.
7. Umlauts have been proccessed ad showed correctly using  `ensure_asci=False`
### Assumptions:
1. I assumed that the input address cannot include any special characters and sucha a thing has been filtered/modified in the beforehand step before running this application. I believe this point makes sense.
2. For any application, if we can provide more test cases, we can detect bugs and correct our soultion better everyday. That's why i designed this application using the mentioned test cases nad getting the correct output as described. _Moreover, having issues in Regex can be easily modified through the YAML File which give us an advantage._

# Tests:
Run the following command into any terminal after changing your current directory to the project's directory:

`python3 -m unittest -v test_AddressPArser.py`