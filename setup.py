import pyparsing as pp
from functions import FeatureLine, ScenarioLine, GivenLine, WhenLine, ThenLine, AndLine, OrLine
from helper_functions import ADD_KEYWORD

FEATURE = pp.Keyword('Feature').setResultsName('feature')
SCENARIO = pp.Keyword('Scenario').setResultsName('scenario')
GIVEN = pp.Keyword('Given').setResultsName('given')
WHEN = pp.Keyword('When').setResultsName('when')
THEN = pp.Keyword('Then').setResultsName('then')
AND = pp.Keyword('And').setResultsName('and')
OR = pp.Keyword('Or').setResultsName('or')

# ADD_KEYWORD('Example', 'example')


feature_line = FEATURE + pp.restOfLine().setParseAction(FeatureLine().parse)
scenario_line = SCENARIO + pp.restOfLine().setParseAction(ScenarioLine().parse)
given_line = GIVEN + pp.restOfLine().setParseAction(GivenLine().parse)
when_line = WHEN + pp.restOfLine().setParseAction(WhenLine().parse)
then_line = THEN + pp.restOfLine().setParseAction(ThenLine().parse)
and_line = AND + pp.restOfLine().setParseAction(AndLine().parse)
or_line = OR + pp.restOfLine().setParseAction(OrLine().parse)

feature_file_grammar = pp.StringStart() + pp.OneOrMore(
    pp.pythonStyleComment |
    feature_line |
    scenario_line |
    given_line |
    when_line |
    then_line |
    and_line |
    or_line
)


def parse_feature_file(file_path):
    with open(file_path, 'r') as file:
        feature_file = file.read()
        parsed_lines = feature_file_grammar.parseString(feature_file)
        return parsed_lines.asList()
