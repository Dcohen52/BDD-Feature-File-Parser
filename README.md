# BDD Feature-File Parser

This is a simple parser for Gherkin files, ready to use for automation projects - In development.

### Requirements
* Python 3.x
* pyparsing

Run the following command in your terminal:

```
pip install pyparsing
```
### Easy start
Just download this repo and you're ready.

### Example usage
```
from functions import parse_feature_file
parsed_lines = parse_feature_file('path/to/feature/file.feature')
```
And modify the functions on the ```functions.py``` file, they're sorted by keyword-classes. there's an example in every class for an easy start.

### Grammar
The grammar recognizes the following keywords:
* Feature
* Scenario
* Given
* When
* Then
* And
* Or

The grammar also recognizes Python-style comments: "#".

### More info
**THIS PROJECT IS JUST A PARSER, THE TECHNOLOGY BELOGS TO:**
https://cucumber.io/docs/gherkin/

### License
This code is licensed under the MIT License. See the LICENSE file for more information.
