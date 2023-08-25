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
SCENARIO_OUTLINE = pp.Keyword('Scenario Outline').setResultsName('scenario_outline')
EXAMPLES = pp.Keyword('Examples:').setResultsName('examples')

feature_line = FEATURE + pp.restOfLine().setParseAction(FeatureLine(context).parse)
scenario_line = SCENARIO + pp.restOfLine().setParseAction(ScenarioLine(context).parse)
given_line = GIVEN + pp.restOfLine().setParseAction(GivenLine(context).parse)
when_line = WHEN + pp.restOfLine().setParseAction(WhenLine(context).parse)
then_line = THEN + pp.restOfLine().setParseAction(ThenLine(context).parse)
and_line = AND + pp.restOfLine().setParseAction(AndLine(context).parse)
or_line = OR + pp.restOfLine().setParseAction(OrLine(context).parse)

pipe_delimited = pp.delimitedList(pp.originalTextFor(pp.Word(pp.alphas + '_" ')), delim="|", combine=True)
example_header = pp.Suppress("|") + pipe_delimited + pp.Suppress("|") + pp.lineEnd()
example_row = pp.Suppress("|") + pipe_delimited + pp.Suppress("|") + pp.lineEnd()
examples_grammar = EXAMPLES + pp.lineEnd + example_header + pp.OneOrMore(example_row)

feature_file_grammar = pp.StringStart() + pp.OneOrMore(
    pp.pythonStyleComment |
    feature_line |
    scenario_line |
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

                if 'Examples:' in line:
                    is_scenario_outline = False
                    scenario_outline_steps = []

                    examples_headers = []
                    examples_rows = []

                    print("\nExamples:")
                    for idx, line in enumerate(parsed_lines[idx + 1:]):
                        if 'examples' in line:
                            break

                        if idx == 0:
                            examples_headers.append(line)
                        else:
                            examples_headers.append(line)
                            examples_rows.append(line)

                    headers_splitted = examples_headers[1].split('|')
                    headers = [header.strip() for header in headers_splitted if header.strip() != '']
                    print(f"Headers: {headers}")

                    for row in examples_rows[2::2]:
                        row_splitted = row.split('|')
                        values = [value.strip() for value in row_splitted if value.strip() != '']
                        print(f"Values: {values}")

                    continue

            # # Print the structure of the feature
            # if context.features:
            #     print("\n", context.features[0])
            #
            # return parsed_lines.asList()

    except FileNotFoundError:
        print(f"File {file_path} not found!")
        return []
    except pp.ParseException as e:
        print(f"Error while parsing file {file_path} at line {e.lineno}, column {e.col}: {e.msg}")
        return []
