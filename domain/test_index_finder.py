from domain.index_finder import find_index
import unittest

TEST_DATA_WITH_UNIQUE_ITEMS = [
	(['A'], ('A', 0)),
	(['A', 'B', 'C', 'A', 'C'], ('B', 1)),
	(['A', 'A', 'B', 'B', 'C'], ('C', 4)),
	(['A', 'B', 'A', ], ('B', 1)),
	(['A', 'B', 'B', 'B'], ('A', 0)),
	(['B', 'B', 'B', 'A'], ('A', 3))
]

TEST_DATA_WITHOUT_UNIQUE_ITEM = ['A', 'B', 'C', 'C', 'B', 'A']


class TestIndexFinder(unittest.TestCase):
	def test_finds_first_unique_item(self):
		for example in TEST_DATA_WITH_UNIQUE_ITEMS:
			self.assertEqual(find_index(example[0]), example[1])

	def test_returns_none_for_empty_array(self):
		self.assertEqual(find_index([]), None)

	def test_returns_none_for_no_unique_item(self):
		self.assertEqual(TEST_DATA_WITHOUT_UNIQUE_ITEM, None)

if __name__ == '__main__':
	unittest.main()