import pytest
import sys
from utils import check_file_is_python_file, check_command_line_args


def test_check_command_line_args_too_few_args():
    # Mock sys.argv to simulate too few argumets using MonkeyPatch
    pytest.MonkeyPatch().setattr(sys, "argv", ["lines.py"])

    with pytest.raises(SystemExit) as e:
        check_command_line_args()
    assert str(e.value) == "Too few command-line arguments"


def test_check_command_line_args_too_many_args():
    pytest.MonkeyPatch().setattr(sys, "argv", ["lines.py", "hello.py", "goodbye.py"])

    with pytest.raises(SystemExit) as e:
        check_command_line_args()
    assert str(e.value) == "Too many command-line arguments"


def test_check_file_is_python_file_not_python_file():
    with pytest.raises(SystemExit) as e:
        check_file_is_python_file("invalid_extension.txt")
    assert str(e.value) == "Not a python file"
