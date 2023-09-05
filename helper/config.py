########################################
# Generates default configuration file #
########################################

import json

config = {
    "DEFAULT_PATH": "./lyre/automatic-tests/",
    "TEMPLATE_PATH": "./lyre/automatic-tests/templates",
    "REPORTS_PATH": "./lyre/automatic-tests/reports",
    "LOGS_PATH": "./lyre/automatic-tests/logs",
    "LOGGING_MODE": "all",
}

output_file = "../config.json"

with open(output_file, "w") as f:
    json.dump(config, f, indent=4)

print(f"Configuration file '{output_file}' generated successfully.")
