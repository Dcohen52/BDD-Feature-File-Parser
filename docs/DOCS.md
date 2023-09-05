# Lyre: Your Storyboarding Assistant 🎭
Lyre is a system designed to process and interpret scripts written in a specific domain language. It allows users to define storyboards, cases and specific steps for a given application or system behavior.
Lyre uses a modified DSL based on Gherkin. Designed for seamless integration into automation workflows, Lyre elevates the efficiency and sophistication of your test automation processes. Continual development ensures that Lyre remains at the forefront of technological advancements.
For more detailed information, visit Lyre's GitHub page.

### What Can Lyre Do? 🚀

* **Gherkin-esque Syntax:** Use simple, structured language to define your tests.
* **Custom Directives**: Use custom directives to enhance your tests.
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
    Log: debug
    Given I am in the login screen
    And I input valid credentials
    Then I should be directed to the dashboard
```

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

* **Notify:** Sends an email to the specified email addresses when the test is executed.
* **Log:** Sets the log mode for the test. The default log level is "none", you can set it to "debug", "none" for now.
* **Environment:** Sets the environment for the test.
* **Version:** Sets the version for the test.
* **Priority:** Sets the priority for the test.
* **Skip:** Skips the test if set to true. The default value is "false".
* **Screenshot:** Takes screenshot of the application at each step, available options are "always", "on-fail", "never". The default value is "never".

#### 3. Execute Your Tests 🏃‍♂️
Run Lyre and watch as it automates the testing process based on your described scenarios.


### 4. Review Results 📊
Check the logs for detailed info on each test and view reports for a summary.
Coming Soon: Integrated HTML reports for a holistic view of your tests.


### License 📄
Lyre believes in open testing for all. Learn more about our license [here]("engine/LICENSE").