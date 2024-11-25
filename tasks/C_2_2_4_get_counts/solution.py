import unittest
import pandas as pd

def get_counts(self, bins, **cut_kwargs):
    ser_bins = pd.cut(self, bins, **cut_kwargs)
    return pd.DataFrame({
        "relativen Häufigkeiten": ser_bins.value_counts(normalize=True),
        "absoluten Häufigkeiten": ser_bins.value_counts(normalize=False),
    })

pd.Series.get_counts = get_counts

if __name__ == '__main__':
    daten = pd.Series([1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9, 9, 9, 9, 9, 10])
    print(daten.get_counts(bins=[0, 3, 6, 9, 12], right=True))















#
# class TestGetCounts(unittest.TestCase):
#
#     def test_viktor_example(self):
#         expected_result = pd.DataFrame({
#             'Absolute Frequency': [4, 8, 7, 1],
#             'Relative Frequency': [0.20, 0.40, 0.35, 0.05]})
#         self.assertEqual(get_counts([1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9, 9, 9, 9, 9, 10], [0, 3, 6, 9, 12])[
#                              'Relative Frequency'].to_list(),
#                          expected_result['Relative Frequency'].to_list())
#         self.assertEqual(get_counts([1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9, 9, 9, 9, 9, 10], [0, 3, 6, 9, 12])[
#                              'Absolute Frequency'].to_list(),
#                          expected_result['Absolute Frequency'].to_list())
#
#     def test_viktor_similar(self):
#         expected_result = pd.DataFrame({
#             'Absolute Frequency': [4, 4, 5, 7],
#             'Relative Frequency': [0.20, 0.20, 0.25, 0.35]})
#         self.assertEqual(get_counts([1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9, 9, 9, 9, 9, 10], 4)[
#                              'Relative Frequency'].to_list(),
#                          expected_result['Relative Frequency'].to_list())
#         self.assertEqual(get_counts([1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9, 9, 9, 9, 9, 10], 4)[
#                              'Absolute Frequency'].to_list(),
#                          expected_result['Absolute Frequency'].to_list())
#
#     def test_empty_list(self):
#         with self.assertRaises(ValueError):
#             get_counts([], 3)
#
#     def test_bins_string(self):
#         with self.assertRaises(TypeError):
#             get_counts([1, 2, 3, 3], 'a')
#
#     def test_single_element(self):
#         expected_result = pd.DataFrame({
#             'Absolute Frequency': [1],
#             'Relative Frequency': [1.0]})
#         self.assertEqual(get_counts([4], 1)['Relative Frequency'].to_list(),
#                          expected_result['Relative Frequency'].to_list())
#
#     def test_single_element_multiple(self):
#         expected_result = pd.DataFrame({
#             'Absolute Frequency': [3],
#             'Relative Frequency': [1.0]})
#         self.assertEqual(get_counts([1, 1, 1], 1)['Relative Frequency'].to_list(),
#                          expected_result['Relative Frequency'].to_list())
#         self.assertEqual(get_counts([1, 1, 1], 1)['Absolute Frequency'].to_list(),
#                          expected_result['Absolute Frequency'].to_list())
#
