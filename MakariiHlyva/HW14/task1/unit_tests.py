import unittest
import fuctions_with_errors
import fuctions
from parameterized import parameterized
from types import MappingProxyType


class test_fuctions(unittest.TestCase):

    @parameterized.expand([
        ["name", "Hello name!", f"Test_greeting_by_name"],
        ["Ivan", "Hello Ivan!", f"Test_greeting_by_name"],
        ["", "Hello !", f"Test_greeting_by_name"]
    ])
    def test_greeting_by_name(self, name, expected, message):
        self.assertEqual(fuctions_with_errors.greeting_by_name(name), expected, f"{message} in FUNCTIONS_WITH_ERRORS({name}) - FAILED")
        self.assertEqual(fuctions.greeting_by_name(name), expected, f"{message} in FUNCTIONS ({name}) - FAILED")

    @parameterized.expand([
        ['', "Ivan ta Olesya", "Not found", "test_get_symbol_position with empty symbol FAILED"],
        ['12', "Ivan ta Olesya", "Error! Symbol can be string with only one letter", "test_get_symbol_position with to long symbol FAILED"],
        ['t', "Ivan ta Olesya", 5, "test_get_symbol_position with existing symbol PASSED"],
        ['o', "Ivan ta Olesya", "Not found", "test_get_symbol_position with not existing symbol FAILED"]
    ])
    def test_get_symbol_position(self, symbol, text, result, message):
        self.assertEqual(fuctions_with_errors.get_symbol_position(text, symbol), result, f"in FUNCTIONS_WITH_ERRORS{message}")
        self.assertEqual(fuctions.get_symbol_position(text, symbol), result, f"in FUNCTIONS {message}")

    @parameterized.expand([
        [   {"12": 21, "123": 1234}, 
            {"dsf23": "123", "23f": 2314},
            {"12": 21, "123": 1234, "23f": 2314, "dsf23": "123"},
            "Merge Passed"],
        [   MappingProxyType({"12": 32, "1234": "fsdfdsf"}),
            {28: "df"},
            {"12": 32, "1234": "fsdfdsf", 28: "df"},
            "Dict1 is immutable, merge Failed"]
    ])
    def test_merge(self, dict1, dict2, expected, message):
        self.assertEqual(fuctions_with_errors.merge(dict1, dict2), expected, f"in FUNCTIONS_WITH_ERRORS Failed {message}")
        self.assertEqual(fuctions.merge(dict1, dict2), expected, f"in FUNCTIONS Failed {message}")

if __name__ == '__main__':
    unittest.main()

