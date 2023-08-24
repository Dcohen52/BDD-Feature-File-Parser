import pyparsing as pp
from functions import ParsingContext, FeatureLine, ScenarioLine, GivenLine, WhenLine, ThenLine, AndLine, OrLine, \
    ScenarioOutlineLine
from helper_functions import ADD_KEYWORD

context = ParsingContext()

FEATURE = pp.Keyword('Feature').setResultsName('feature')
SCENARIO = pp.Keyword('Scenario').setResultsName('scenario')
GIVEN = pp.Keyword('Given').setResultsName('given')
WHEN = pp.Keyword('When').setResultsName('when')
THEN = pp.Keyword('Then').setResultsName('then')
AND = pp.Keyword('And').setResultsName('and')
OR = pp.Keyword('Or').setResultsName('or')
SCENARIO_OUTLINE = pp.Keyword('Scenario Outline').setResultsName('scenario_outline')
EXAMPLES = pp.Keyword('Examples:').setResultsName('examples')

feature_line = FEATURE + pp.restOfLine().setParseAction(FeatureLine(context).parse)
scenario_line = SCENARIO + pp.restOfLine().setParseAction(ScenarioLine(context).parse)
given_line = GIVEN + pp.restOfLine().setParseAction(GivenLine(context).parse)
when_line = WHEN + pp.restOfLine().setParseAction(WhenLine(context).parse)
then_line = THEN + pp.restOfLine().setParseAction(ThenLine(context).parse)
and_line = AND + pp.restOfLine().setParseAction(AndLine(context).parse)
or_line = OR + pp.restOfLine().setParseAction(OrLine(context).parse)
# example_row = pp.lineStart + pp.Group(pp.delimitedList(pp.Word(pp.alphas + '_"'))).setParseAction(
#     ScenarioLine.add_example_row)
# examples_grammar = EXAMPLES + pp.lineEnd + pp.OneOrMore(example_row)

scenario_outline_line = SCENARIO_OUTLINE + pp.restOfLine().setParseAction(ScenarioOutlineLine(context).parse)

pipe_delimited = pp.delimitedList(pp.originalTextFor(pp.Word(pp.alphas + '_" ')), delim="|", combine=True)
example_header = pp.Suppress("|") + pipe_delimited + pp.Suppress("|") + pp.lineEnd()
example_row = pp.Suppress("|") + pipe_delimited + pp.Suppress("|") + pp.lineEnd()
examples_grammar = EXAMPLES + pp.lineEnd + example_header + pp.OneOrMore(example_row)

# example_header = pp.Group(pp.delimitedList(pp.Word(pp.alphas + '_'))).setParseAction(
#     ScenarioOutlineLine(context).add_example_header)
# example_row = pp.Group(pp.delimitedList(pp.Word(pp.alphas + '_"'))).setParseAction(
#     ScenarioOutlineLine(context).add_example_row)
# examples_grammar = EXAMPLES + pp.lineEnd + example_header + pp.lineEnd + pp.OneOrMore(example_row)

# pipe_delimited = pp.delimitedList(pp.Word(pp.printables + " "), delim="|", combine=True)
# examples_header = EXAMPLES + pp.LineEnd() + pp.Suppress("|") + pipe_delimited + pp.Suppress("|") + pp.LineEnd()
# examples_row = pp.Suppress("|") + pipe_delimited + pp.Suppress("|") + pp.LineEnd()
# example_block = examples_header + pp.OneOrMore(examples_row)


feature_file_grammar = pp.StringStart() + pp.OneOrMore(
    pp.pythonStyleComment |
    feature_line |
    scenario_line |
    scenario_outline_line |
    examples_grammar |
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

            is_scenario_outline = False
            scenario_outline_steps = []

            for idx, line in enumerate(parsed_lines):
                if 'scenario_outline' in line:
                    is_scenario_outline = True
                    print("\nScenario Outline:", line[1])  # Printing the scenario outline title
                    continue

                # If within a Scenario Outline block
                if is_scenario_outline:
                    if 'given' in line or 'when' in line or 'then' in line:
                        scenario_outline_steps.append(line)
                        continue

                if 'examples' in line:
                    headers = line[1]
                    rows = [row for row in line[2:] if row != '\n']

                    for row_idx, row in enumerate(rows):
                        print(f"\nExample {row_idx + 1}/{len(rows)}:")
                        for step in scenario_outline_steps:
                            print(step[0], end=' ')  # Given, When, or Then
                            step_text = step[1]
                            for header, value in zip(headers, row):
                                step_text = step_text.replace(f"<{header}>", value)
                            print(step_text)

                    # Resetting for the next Scenario or Scenario Outline
                    is_scenario_outline = False
                    scenario_outline_steps = []

            # Print the structure of the feature
            if context.features:
                print("\n", context.features[0])

            return parsed_lines.asList()

    except FileNotFoundError:
        print(f"File {file_path} not found!")
        return []
    except pp.ParseException as e:
        print(f"Error while parsing file {file_path} at line {e.lineno}, column {e.col}: {e.msg}")
        return []
