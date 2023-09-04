from engine.core import parse_feature_file

if __name__ == '__main__':
    file_path = 'engine/new_syntax.lyre'
    parsed_lines = parse_feature_file(file_path)