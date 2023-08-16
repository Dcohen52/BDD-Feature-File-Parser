import pyparsing as pp
from functions import ParsingContext, FeatureLine, ScenarioLine, GivenLine, WhenLine, ThenLine, AndLine, OrLine
from helper_functions import ADD_KEYWORD

context = ParsingContext()

FEATURE = pp.Keyword('Feature').setResultsName('feature')
SCENARIO = pp.Keyword('Scenario').setResultsName('scenario')
GIVEN = pp.Keyword('Given').setResultsName('given')
WHEN = pp.Keyword('When').setResultsName('when')
THEN = pp.Keyword('Then').setResultsName('then')
AND = pp.Keyword('And').setResultsName('and')
OR = pp.Keyword('Or').setResultsName('or')

feature_line = FEATURE + pp.restOfLine().setParseAction(FeatureLine(context).parse)
scenario_line = SCENARIO + pp.restOfLine().setParseAction(ScenarioLine(context).parse)
given_line = GIVEN + pp.restOfLine().setParseAction(GivenLine(context).parse)
when_line = WHEN + pp.restOfLine().setParseAction(WhenLine(context).parse)
then_line = THEN + pp.restOfLine().setParseAction(ThenLine(context).parse)
and_line = AND + pp.restOfLine().setParseAction(AndLine(context).parse)
or_line = OR + pp.restOfLine().setParseAction(OrLine(context).parse)

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
    try:
        with open(file_path, 'r') as file:
            feature_file = file.read()
            parsed_lines = feature_file_grammar.parseString(feature_file)

            # Print the structure of the feature
            if context.features:  # If we've parsed at least one feature
                print(context.features[0])  # Print the first feature

            return parsed_lines.asList()
    except FileNotFoundError:
        print(f"File {file_path} not found!")
        return []
    except pp.ParseException as e:
        print(f"Error while parsing file {file_path} at line {e.lineno}, column {e.col}: {e.msg}")
        return []
