################################
#    Edit this file to add     #
#  Functionality to the lines  #
################################

class Feature:
    def __init__(self, title):
        self.title = title
        self.scenarios = []

    def __str__(self):
        return f"Feature: {self.title}\n" + "\n".join(str(scenario) for scenario in self.scenarios)

    def add_scenario(self, scenario):
        self.scenarios.append(scenario)


class Scenario:
    def __init__(self, title):
        self.title = title
        self.steps = []

    def __str__(self):
        steps_str = "\n".join(f"{step_type}: {content}" for step in self.steps for step_type, content in step.items())
        return f"Scenario: {self.title}\n{steps_str}"

    def add_step(self, step_type, content):
        self.steps.append({step_type: content})


class ParsingContext:
    def __init__(self):
        self.current_feature = None
        self.current_scenario = None
        self.features = []


class FeatureLine:
    def __init__(self, context):
        self.context = context

    def parse(self, line):
        feature = Feature(line[0])
        self.context.current_feature = feature
        self.context.features.append(feature)
        print("Found Feature line:", str(line).strip("['']"))


class ScenarioLine:
    def __init__(self, context):
        self.context = context

    def parse(self, line):
        scenario = Scenario(line[0])
        self.context.current_scenario = scenario
        self.context.current_feature.add_scenario(scenario)
        print("Found Scenario line:", str(line).strip("[':'] "))
        if self.context.current_feature:
            print("    Related to Feature:", self.context.current_feature.title)


class StepLine:
    def __init__(self, context):
        self.context = context
        self.line_dispatcher = {}

    def parse(self, line):
        curr_line = line[0]
        method_to_invoke = self.line_dispatcher.get(curr_line)
        if method_to_invoke:
            method_to_invoke()
        # Also store the step in the current scenario
        self.context.current_scenario.add_step(self.__class__.__name__, curr_line)
        if self.context.current_scenario:
            print("        Current Scenario:", self.context.current_scenario.title)

            if self.context.current_scenario.title == "Scenario Outline":
                print("        Current Scenario Outline:", self.context.current_scenario.title)
                print("        Current Scenario Outline Examples:", self.context.current_scenario.title)


class GivenLine(StepLine):
    def __init__(self, context):
        super().__init__(context)
        self.line_dispatcher = {
            'Given the Maker has started a game with the word "silky"': self.maker_started_a_game
        }

    def maker_started_a_game(self):
        print('Method -> Given the Maker has started a game with the word "silky"')


class WhenLine(StepLine):
    def __init__(self, context):
        super().__init__(context)
        self.line_dispatcher = {
            'When the Maker waits for a Breaker to join': self.maker_waits_for_a_breaker,
            'When the Breaker joins the Maker\'s game': self.maker_joins_the_breaker
        }

    def maker_waits_for_a_breaker(self):
        print("Method -> When the Maker starts a game")

    def maker_joins_the_breaker(self):
        print("Method -> When the Breaker joins the Maker's game")


class ThenLine(StepLine):
    def __init__(self, context):
        super().__init__(context)
        self.line_dispatcher = {
            'Then the Maker waits for a Breaker to join': self.maker_waits_for_a_breaker,
            'Then the Breaker must guess a word with 5 characters': self.breaker_must_guess
        }

    def maker_waits_for_a_breaker(self):
        print("Method -> Then the Maker waits for a Breaker to join")

    def breaker_must_guess(self):
        print("Method -> Then the Breaker must guess a word with 5 characters")


class AndLine:
    def __init__(self, context):
        self.context = context
        self.line_dispatcher = {}

    def parse(self, line):
        """
        :param line: list[0] converted to a string.
        :return: executes relevant method to the current line.
        """
        curr_line = line[0]
        line = curr_line[:1].replace(" ", "") + curr_line[1:]
        # Retrieve method from dispatch dictionary and invoke it
        method_to_invoke = self.line_dispatcher.get(line)
        if method_to_invoke:
            method_to_invoke()


class OrLine:
    def __init__(self, context):
        self.context = context
        self.line_dispatcher = {}

    def parse(self, line):
        """
        :param line: list[0] converted to a string.
        :return: executes relevant method to the current line.
        """
        curr_line = line[0]
        line = curr_line[:1].replace(" ", "") + curr_line[1:]
        # Retrieve method from dispatch dictionary and invoke it
        method_to_invoke = self.line_dispatcher.get(line)
        if method_to_invoke:
            method_to_invoke()
