import unittest

from flatten import flatten_dictionary


class Test(unittest.TestCase):
    def test_flatten(self):
        given_dictionary = {
            "key": 3,
            "foo": {
                "a": 5,
                "bar": {
                    "baz": 8
                }
            }
        }

        expected_dictionary = {
            "key": 3,
            "foo.a": 5,
            "foo.bar.baz": 8
        }

        self.assertEqual(flatten_dictionary(given_dictionary), expected_dictionary)
