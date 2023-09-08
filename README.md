# Lyre: Your Storyboarding Assistant 🎭
Introducing Lyre: a specialized parsing engine that uses a modified DSL based on gherkin. Designed for seamless integration into automation workflows, Lyre elevates the efficiency and sophistication of your test automation processes. Continual development ensures that Lyre remains at the forefront of technological advancements.

### Prerequisites
* **Python Version:** 3.x (Incompatibility with Python 2.x has been observed)

To install the prerequisite libraries, execute the command below in your shell environment:
```bash
pip install -r requirements.txt
```
### Getting Started
1. **Clone the repository:**
   `git clone https://github.com/Dcohen52/Lyre.git`
3. **Ensure Compliance with Prerequisites:**
Verify that the Python version is 3.x and that pyparsing is successfully installed.
### Supported Grammar
Lyre currently recognizes the following keywords:

* Storyboard
* Case
* Given
* When
* Then
* And
* Or

#### Custom Directives

Here are some custom directives that you can use to enhance your tests, along with their descriptions:

```cucumber
    Notify: ["email@example.com"]
    Log: debug
    Environment: QA
    Version: 1.0.0
    Priority: 1
    Skip: true
    Screenshot: always
```

More on them, in the DOCS.md file.

### Example
```cucumber
Storyboard: Login Functionality
  Case: Successful Login
    Notify: ["email@example.com", "email2@example.com"]
    Log: detailed
    Given I am in the login screen
    And I input valid credentials
    Then I should be directed to the dashboard
    # this is a comment
```

In addition, Lyre also accommodates Python-style comments, identified by the "#" symbol.

### Customization Features
Lyre can be extended to accommodate additional keywords or functionalities. Detailed guidelines can be found in the `functions.py` source file.

### Acknowledgements
Lyre is a specialized parser and lays no claim to the foundational Gherkin technology. For an in-depth understanding of Gherkin, please visit the official documentation: Gherkin Language.

### Future Roadmap
* Support for additional Gherkin-inspired keywords.
* Refined and comprehensive error-handling capabilities.

### Licensing
This software is distributed under the terms of the MIT License. For comprehensive licensing details, please refer to the LICENSE file.
