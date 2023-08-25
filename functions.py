################################
#    Edit this file to add     #
#  Functionality to the lines  #
################################

import re
from colorama import Fore, Back, Style


# from core import examples_headers, examples_rows


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
        # FOR OUTLINE
        self.examples_headers = []
        self.examples_rows = []

    def __str__(self):
        steps_str = ""
        for step in self.steps:
            for step_type, content in step.items():
                if self.examples_rows:
                    for row in self.examples_rows:
                        substituted_content = content
                        for header, value in zip(self.examples_headers, row):
                            substituted_content = substituted_content.replace(f"<{header}>", value)
                        steps_str += f"{step_type}: {substituted_content}\n"
                else:
                    steps_str += f"{step_type}: {content}\n"

    def add_examples_header(self, headers):
        self.examples_headers = headers[0].split("|")[0:-1]
        stipped_headers = [header.strip() for header in self.examples_headers]
        self.examples_headers = stipped_headers
        print(f"{Fore.LIGHTYELLOW_EX}Header: {Style.RESET_ALL}{self.examples_headers}")

    def add_examples_row(self, row):
        self.examples_rows.append(row[0].split("|")[0:-1])
        row_stripped = [value.strip() for value in self.examples_rows[-1]]
        self.examples_rows = row_stripped
        print(f"{Fore.LIGHTYELLOW_EX}Row: {Style.RESET_ALL}{self.examples_rows}")

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
        title = str(line).split(":")[1].strip("' []")
        feature = Feature(title)
        self.context.current_feature = feature
        self.context.features.append(feature)
        print(f"{Back.LIGHTGREEN_EX}{Fore.BLACK}Found Feature:{Style.RESET_ALL}", title)


class ScenarioLine:
    def __init__(self, context):
        self.context = context

    def parse(self, line):
        if " Outline:" in line[0]:
            title = str(line).split(":")[1].strip("' []")
            scenario = Scenario(title)
            self.context.current_scenario = scenario
            self.context.current_feature.add_scenario(scenario)
            print(f"{Back.LIGHTRED_EX}Found Scenario Outline:{Style.RESET_ALL}", title)
            print(
                f"    SO - Related to Feature: {Back.LIGHTGREEN_EX}{Fore.BLACK}{self.context.current_feature.title}{Style.RESET_ALL}")

            # HERE
        else:
            title = str(line).split(":")[1].strip("' []")
            scenario = Scenario(title)
            self.context.current_scenario = scenario
            self.context.current_feature.add_scenario(scenario)
            print(f"{Back.LIGHTBLACK_EX}Found Scenario:{Style.RESET_ALL}", title)
            print(
                f"    S - Related to Feature: {Back.LIGHTGREEN_EX}{Fore.BLACK}{self.context.current_feature.title}{Style.RESET_ALL}")

    def add_example_row(self, row):
        self.context.current_scenario.add_examples_row(row)


class StepLine:
    def __init__(self, context):
        self.context = context
        self.pattern_dispatcher = []  # Moved the dispatcher to this level for better structure

    def parse(self, line):
        curr_line = line[0]
        matched = False
        for pattern, handler in self.pattern_dispatcher:
            match = re.match(pattern, curr_line)
            if match:
                print(f"{Fore.LIGHTMAGENTA_EX}Matched pattern: {pattern} with line: {curr_line}{Style.RESET_ALL}")
                handler(*match.groups())  # Applying the handler function when a match is found
                # matched = True
                break
            if not matched:
                print(f"No handler found for: {curr_line}")

        # Store the step in the current scenario
        self.context.current_scenario.add_step(self.__class__.__name__, curr_line)
        print("        Current Scenario:", self.context.current_scenario.title)

        # Additional handling if the current scenario is a Scenario Outline
        if self.context.current_scenario.title == "Outline":
            print("        Current Scenario Outline:", self.context.current_scenario.title)
            print("        Current Scenario Outline Examples:", self.context.current_scenario.examples_rows)


class GivenLine(StepLine):
    def __init__(self, context):
        super().__init__(context)
        self.pattern_dispatcher = [
            (r'\s*the Maker has started a game with the word "(.*)"', self.maker_started_a_game)
        ]

    def parse(self, line):
        curr_line = line[0].strip()
        # print(f"{Fore.LIGHTYELLOW_EX}DEBUG: Parsing '{curr_line}{Style.RESET_ALL}'")
        matched = False
        for pattern, handler in self.pattern_dispatcher:
            match = re.match(pattern, curr_line.strip())
            if match:
                # print(f"{Fore.LIGHTBLUE_EX}DEBUG: Matched using {pattern}{Style.RESET_ALL}")
                # print(f"{Fore.LIGHTMAGENTA_EX}Matched pattern: {pattern} with line: {curr_line}{Style.RESET_ALL}")
                handler(*match.groups())
                matched = True
                break
        if not matched:
            # print(f"{Fore.LIGHTBLUE_EX}DEBUG: Failed to match {curr_line} using {pattern}{Style.RESET_ALL}")
            print(f"{Fore.RED}No handler found for: {curr_line}{Style.RESET_ALL}")

        # Store the step in the current scenario
        self.context.current_scenario.add_step(self.__class__.__name__, curr_line)

    def maker_started_a_game(self, word):
        print(
            f"{Back.BLUE}{Fore.BLACK}Method -> Given the Maker has started a game with the word {word}{Style.RESET_ALL}")


class WhenLine(StepLine):
    def __init__(self, context):
        super().__init__(context)
        self.line_dispatcher = {
            (r'\s*the Maker starts a game', self.maker_starts_a_game),
            (r'\s*the Breaker guesses the word "(.*)"', self.breaker_guesses_word),
            (r"\s*the Breaker joins the Maker's game", self.breaker_joins_the_makers_game)

        }

    def parse(self, line):
        curr_line = line[0].strip()
        matched = False
        for pattern, handler in self.line_dispatcher:
            match = re.match(pattern, curr_line)
            if match:
                handler(*match.groups())
                matched = True
                break
        if not matched:
            print(f"{Fore.RED}No handler found for: {curr_line}{Style.RESET_ALL}")

        # Store the step in the current scenario
        self.context.current_scenario.add_step(self.__class__.__name__, curr_line)

    def maker_starts_a_game(self):
        print(f"{Back.GREEN}{Fore.BLACK}Method -> When the Maker starts a game{Style.RESET_ALL}")

    def breaker_guesses_word(self, guess):
        print(f"{Back.GREEN}{Fore.BLACK}Method -> When the Breaker guesses the word {guess}{Style.RESET_ALL}")

    def breaker_joins_the_makers_game(self):
        print(f"{Back.GREEN}{Fore.BLACK}Method -> When the Breaker joins the Maker's game{Style.RESET_ALL}")


class ThenLine(StepLine):
    def __init__(self, context):
        super().__init__(context)
        self.line_dispatcher = {
            (r'\s*the outcome is "(.*)"', self.outcome_is),
            (r"\s*the Maker waits for a Breaker to join", self.maker_waits_for_breaker_to_join),
            (r'\s*the Breaker must guess a word with "(.*)" characters', self.breaker_must_guess_a_word_with_n_chars),
        }

    def parse(self, line):
        curr_line = line[0].strip()
        matched = False
        for pattern, handler in self.line_dispatcher:
            match = re.match(pattern, curr_line)
            if match:
                handler(*match.groups())
                matched = True
                break
        if not matched:
            print(f"{Fore.RED}No handler found for: {curr_line}{Style.RESET_ALL}")

        # Store the step in the current scenario
        self.context.current_scenario.add_step(self.__class__.__name__, curr_line)

    def outcome_is(self, outcome):
        print(f"{Back.CYAN}{Fore.BLACK}Method -> Then the outcome is {outcome}{Style.RESET_ALL}")

    def maker_waits_for_breaker_to_join(self):
        print(f"{Back.CYAN}{Fore.BLACK}Method -> Then the Maker waits for a Breaker to join{Style.RESET_ALL}")

    def breaker_must_guess_a_word_with_n_chars(self, n):
        print(
            f"{Back.CYAN}{Fore.BLACK}Method -> Then the Breaker must guess a word with {n} characters{Style.RESET_ALL}")


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


class ExamplesLine:
    def __init__(self, context):
        self.context = context

    def parse(self, lines, current_index):
        print(
            f"{Back.LIGHTYELLOW_EX}{Fore.BLACK}Found Examples{Style.RESET_ALL} related to Scenario Outline: {Back.LIGHTRED_EX}{self.context.current_scenario.title}{Style.RESET_ALL}")


class ExamplesValuesLine:
    def __init__(self, context):
        self.context = context

    def parse(self, line):
        # self.context.current_scenario.add_examples_header(line)
        # HEADER
        if not self.context.current_scenario.examples_headers:
            self.context.current_scenario.add_examples_header(line)
        # ROW
        else:
            self.context.current_scenario.add_examples_row(line)
