import os
import pytest
import tempfile  # For creating temporary test files
from lines import count_lines_of_code


def test_count_lines_of_code_only_code():

    code = "print('Hello')\nprint('World')"
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(code)
        temp_name = f.name

    assert count_lines_of_code(temp_name) == 2

    os.remove(temp_name)  # Removes the temporary file


def test_count_lines_of_code_with_commments_and_blank_lines():

    code = "# Comment\n\nprint('Hello')\n    \n# Another comment\nprint('World')"
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(code)
        temp_name = f.name

    assert count_lines_of_code(temp_name) == 2

    os.remove(temp_name)


def test_count_lines_of_code_file_not_found():
    with pytest.raises(FileNotFoundError):
        count_lines_of_code("non_existent_file.py")
