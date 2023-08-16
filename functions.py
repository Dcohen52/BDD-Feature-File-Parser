################################
#    Edit this file to add     #
#  Functionality to the lines  #
################################

class FeatureLine:
    def parse(self, line):
        print("Found Feature line:", line)


class ScenarioLine:
    def parse(self, line):
        print("Found Scenario line:", line)
        line_array = line[0].split(":")
        if line_array[0].strip() == "Outline":
            print("Found Scenario Outline line:", line)
        else:
            pass


class GivenLine:
    def __init__(self):
        self.line_dispatcher = {
            'the Maker has started a game with the word "silky"': self.maker_started_a_game
        }

    def parse(self, line):
        """
        :param line: list[0] converted to a string.
        :return: executes relevant method to the current line.
        """
        curr_line = line[0]
        line = curr_line[:2].replace(" ", "") + curr_line[2:]
        # Retrieve method from dispatch dictionary and invoke it
        method_to_invoke = self.line_dispatcher.get(line)
        if method_to_invoke:
            method_to_invoke()

    def maker_started_a_game(self):
        print('Method -> Given the Maker has started a game with the word "silky"')


class WhenLine:

    def __init__(self):
        self.line_dispatcher = {
            'the Maker starts a game': self.maker_waits_for_a_breaker,
            "the Breaker joins the Maker's game": self.maker_joins_the_breaker
        }

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

    def maker_waits_for_a_breaker(self):
        print("Method -> When the Maker starts a game")

    def maker_joins_the_breaker(self):
        print("Method -> When the Breaker joins the Maker's game")


class ThenLine:

    def __init__(self):
        self.line_dispatcher = {
            'the Maker waits for a Breaker to join': self.maker_waits_for_a_breaker,
            'the Breaker must guess a word with 5 characters': self.breaker_must_guess
        }

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

    def maker_waits_for_a_breaker(self):
        print("Method -> Then the Maker waits for a Breaker to join")

    def breaker_must_guess(self):
        print("Method -> Then the Breaker must guess a word with 5 characters")


class AndLine:
    def parse(self, line):
        print("Found And line:", line)


class OrLine:
    def parse(self, line):
        print("Found Or line:", line)
