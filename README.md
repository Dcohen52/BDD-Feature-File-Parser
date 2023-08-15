# Gherkin Feature-File Parser
A parser tailored for Gherkin feature files, designed for seamless integration with automation projects. Please note that this parser is currently under active development.

### Prerequisites
* **Python Version:** 3.x
* **Library:** pyparsing
To install the required library, execute the following command:


```bash
pip install pyparsing
```
### Getting Started
Clone or download this repository to your local machine.
Ensure the aforementioned prerequisites are met.

### Usage
To parse a feature file:

```python
from functions import parse_feature_file
parsed_lines = parse_feature_file('path/to/feature/file.feature')
```
For customization, refer to the ```functions.py``` file. Functions are organized by keyword-classes, with each class containing a sample for ease of reference.

Supported Grammar
This parser recognizes the following Gherkin keywords:

* Feature
* Scenario
* Given
* When
* Then
* And
* Or

Additionally, Python-style comments, denoted by "#", are also supported.

### Acknowledgements
This project serves as a parser and does not claim ownership of the underlying technology. For more details on Gherkin, visit:
https://cucumber.io/docs/gherkin/

### Licensing
This software is distributed under the terms of the MIT License. For comprehensive licensing details, please refer to the LICENSE file.
