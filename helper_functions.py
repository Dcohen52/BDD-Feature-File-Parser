import pyparsing as pp


def ADD_KEYWORD(keyword, name):
    return pp.Keyword(f'{keyword}').setResultsName(f'{name}')

