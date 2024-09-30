#!/usr/bin/env bash

# perform static analysis to check pep8 compliance
if ! flake8 --ignore E501; then
    echo "STATUS SIGNIFIES ERROR PEP8 compliance check failed"
    exit 1
fi

# perform static analysis of types
if ! mypy ./main/*.py; then
    echo "STATUS SIGNIFIES ERROR type analysis failed"
    exit 1
fi

# run tests from tests folder
if ! python -m unittest discover -s tests -p 'test_*.py'; then
    echo "STATUS SIGNIFIES ERROR tests failed"
    exit 1
fi
