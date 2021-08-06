import unittest
import json

from search_results_utils import create_search_results, rel_diff_is_too_small

unittest.util._MAX_LENGTH=2000

class TestCreateEmailResponse(unittest.TestCase):

    def test_create_search_results(self):
        input_data = """
{
  "data": [
    {
      "document": 0,
      "object": "search_result",
      "score": 32.734
    },
    {
      "document": 1,
      "object": "search_result",
      "score": 30.557
    },
    {
      "document": 2,
      "object": "search_result",
      "score": 36.299
    }
  ],
  "model": "ada:2020-05-03",
  "object": "list"
}
        """
        response_json = json.loads(input_data)
        actual = create_search_results(response_json)
        self.assertEqual(len(actual), 3)
        self.assertEqual(actual[0].type[0], "erk")
        self.assertEqual(len(actual[1].type), 2)
        self.assertEqual(actual[2].type[0], "elk")

    def test_rel_diff_is_too_small(self):
        input_data = """
{
  "data": [
    {
      "document": 0,
      "object": "search_result",
      "score": 32.734
    },
    {
      "document": 1,
      "object": "search_result",
      "score": 30.557
    },
    {
      "document": 2,
      "object": "search_result",
      "score": 36.299
    }
  ],
  "model": "ada:2020-05-03",
  "object": "list"
}
        """
        response_json = json.loads(input_data)
        actual = create_search_results(response_json)
        self.assertTrue(rel_diff_is_too_small(actual))
