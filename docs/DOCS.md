# Lyre: Your Storyboarding Assistant 🎭
Lyre is a system designed to process and interpret scripts written in a specific domain language. It allows users to define storyboards, scenarios, and specific steps for a given application or system behavior.

For more detailed information, visit Lyre's GitHub page.

### What Can Lyre Do? 🚀

* **Gherkin-esque Syntax:** Use simple, structured language to define your tests.
* **Easy Test Crafting:** Describe your application's behavior in user-centric terms.
* **Automated Execution:** Run tests automatically, ensuring your software is always up to the mark.
* **Notification System:** Stay informed about your tests' statuses.
* **Logs & Reports:** Detailed logs to debug issues and reports for a holistic view.
* **Community-Driven Enhancements:** Continuously updated with features inspired by testers for testers.

### Prerequisites 📋

* **Python Version:** 3.x (Incompatibility with Python 2.x has been observed)
* **Library:** pyparsing

To install the prerequisite library, execute the command below in your shell environment:

```bash
pip install pyparsing
```

### Quick Start Guide 🚀
#### 1. Define Your Case 💼
Think of an application behavior or functionality. E.g., "User login to the application."

#### 2. Describe Using Lyre Syntax 🖋
Use the Lyre syntax to describe the behavior. E.g.,

```cucumber
Storyboard: Login Functionality
  Case: Successful Login
    Notify: ["email@example.com", "email2@example.com"]
    Log: detailed
    Given I am in the login screen
    And I input valid credentials
    Then I should be directed to the dashboard
```

#### 3. Execute Your Tests 🏃‍♂️
Run Lyre and watch as it automates the testing process based on your described scenarios.


### 4. Review Results 📊
Check the logs for detailed info on each test and view reports for a summary.
Coming Soon: Integrated HTML reports for a holistic view of your tests.


### License 📄
Lyre believes in open testing for all. Learn more about our license [here]("engine/LICENSE").