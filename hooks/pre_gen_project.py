import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.project_slug}}"

if not re.match(MODULE_REGEX, module_name):
    print(
        "ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead"
        % module_name
    )

    # Exit to cancel project
    sys.exit(1)

VERSION_REGEX = r"\d+.\d+.\d+$"

version = "{{ cookiecutter.version }}"
if not re.match(VERSION_REGEX, version):
    print(
        "ERROR: The version (%s) is not a valid version. It must be major.minor.patch style. eg. 0.1.0"
        % version
    )

    # Exit to cancel project
    sys.exit(1)
