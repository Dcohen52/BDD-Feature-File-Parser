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
        if line_array[0] == " Outline":
            print("Found Scenario Outline line:", line)
        else:
            pass


class GivenLine:
    def parse(self, line):
        """

        :param line: list[0] converted to a string.
        :return: executes relevant method to the current line.
        """
        curr_line = line[0]
        line = curr_line[:2].replace(" ", "") + curr_line[2:]
        # print("Found Given line:", line)

        if line == 'the Maker has started a game with the word "silky"':
            self.maker_started_a_game()

    def maker_started_a_game(self):
        print('Method -> Given the Maker has started a game with the word "silky"')


class WhenLine:
    def parse(self, line):
        """

        :param line: list[0] converted to a string.
        :return: executes relevant method to the current line.
        """
        curr_line = line[0]
        line = curr_line[:1].replace(" ", "") + curr_line[1:]
        # print("Found Given line:", line)

        if line == 'the Maker starts a game':
            self.maker_waits_for_a_breaker()

        if line == "the Breaker joins the Maker's game":
            self.maker_joins_the_breaker()

    def maker_waits_for_a_breaker(self):
        print("Method -> When the Maker starts a game")

    def maker_joins_the_breaker(self):
        print("Method -> When the Breaker joins the Maker's game")


class ThenLine:
    def parse(self, line):
        """

        :param line: list[0] converted to a string.
        :return: executes relevant method to the current line.
        """
        curr_line = line[0]
        line = curr_line[:1].replace(" ", "") + curr_line[1:]
        # print("Found Given line:", line)

        if line == 'the Maker waits for a Breaker to join':
            self.maker_waits_for_a_breaker()

        if line == 'the Breaker must guess a word with 5 characters':
            self.breaker_must_guess()

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
