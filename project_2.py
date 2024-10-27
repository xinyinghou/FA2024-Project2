from bs4 import BeautifulSoup
import re
import os
import csv
import unittest

# IMPORTANT NOTE:
"""
If you are getting "encoding errors" while trying to open, read, or write from a file, add the following argument to any of your open() functions:
    encoding="utf-8-sig"

An example of that within the function would be:
    open("filename", "r", encoding="utf-8-sig")

There are a few special characters present from Airbnb that aren't defined in standard UTF-8 (which is what Python runs by default). This is beyond the scope of what you have learned so far in this class, so we have provided this for you just in case it happens to you. Good luck!
"""

def load_listing_results(html_file): 
    """
    INPUT: A string containing the path of the html file
    RETURN: A list of tuples
    """
    pass 

def get_listing_details(listing_id): 
    """
    INPUT: A string containing the listing id
    RETURN: A tuple
    """
    pass

def create_listing_database(html_file): 
    """
    INPUT: A string containing the path of the html file
    RETURN: A list of tuples
    """
    pass


def output_csv(data, filename): 
    """
    INPUT: A list of tuples and a string containing the filename
    RETURN: None
    """
    pass

def validate_policy_numbers(data):
    """
    INPUT: A list of tuples
    RETURN: A list of tuples
    """
    pass 

# EXTRA CREDIT 
def google_scholar_searcher(query): 
    """
    INPUT: query (str)
    Return: a list of titles on the first page (list)
    * see PDF instructions for more details
    """
    pass


# TODO: Don't forget to write your test cases! 
class TestCases(unittest.TestCase):
    def setUp(self):
        self.listings = load_listing_results("html_files/search_results.html")

    def test_load_listing_results(self):

        # check that the number of listings extracted is correct (18 listings)
        self.assertEqual(len(self.listings), 18)

        # check that the variable you saved after calling the function is a list
        self.assertEqual(type(self.listings), list)

        # check that each item in the list is a tuple

        # check that the first title and listing id tuple is correct (open the search results html and find it)

        # check that the last title and listing id tuple is correct (open the search results html and find it)

    def test_get_listing_details(self):
        html_list = ["467507",
                     "1550913",
                     "1944564",
                     "4614763",
                     "6092596"]
        
        # call get_listing_details for i in html_list:
        listing_information = [get_listing_details(id) for id in html_list]

        # check that the number of listing information is correct
        self.assertEqual(len(listing_information), 5)
        for info in listing_information:
            # check that each item in the list is a tuple
            self.assertEqual(type(info), tuple)
            # check that each tuple has 6 elements
            self.assertEqual(len(info), 6)
            # check that the first four elements in the tuple are strings
            self.assertEqual(type(info[0]), str)
            self.assertEqual(type(info[1]), str)
            self.assertEqual(type(info[2]), str)
            self.assertEqual(type(info[3]), str)
            # check that the rest two elements in the tuple are integers
            self.assertEqual(type(info[4]), int)
            self.assertEqual(type(info[4]), int)

        # check that the first listing in the html_list has the correct policy number

        # check that the last listing in the html_list has the correct place type

        # check that the third listing has the correct cost

    def test_create_listing_database(self):
        detailed_data = create_listing_database("html_files/search_results.html")

        # check that we have the right number of listings (18)
        self.assertEqual(len(detailed_data), 18)

        for item in detailed_data:
            # assert each item in the list of listings is a tuple
            self.assertEqual(type(item), tuple)
            # check that each tuple has a length of 8

        # check that the first tuple is made up of the following:
        # ('Loft in Mission District', '1944564', '2022-004088STR', 'Superhost', 'Brian', 'Entire Room', 422, 181)
        # check that the last tuple is made up of the following:
        # ('Guest suite in Mission District', '467507', 'STR-0005349', 'Superhost', 'Jennifer', 'Entire Room', 324, 165)

    def test_output_csv(self):
        # call create_listing_database on "html_files/search_results.html"
        # and save the result to a variable
        detailed_data = create_listing_database("html_files/search_results.html")

        # call output_csv() on the variable you saved
        output_csv(detailed_data, "test.csv")

        # read in the csv that you wrote
        csv_lines = []
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.csv'), 'r') as f:
            csv_reader = csv.reader(f)
            for i in csv_reader:
                csv_lines.append(i)

        # check that there are 19 lines in the csv
        self.assertEqual(len(csv_lines), 19)

        # check that the header row is correct

        # check that the next row is the correct information about Guest suite in San Francisco
        
        # check that the row after the above row is the correct infomration about Private room in Mission District
        

    def test_validate_policy_numbers(self):
        # call create_listing_database on "html_files/search_results.html"
        # and save the result to a variable
        detailed_data = create_listing_database("html_files/search_results.html")

        # call validate_policy_numbers on the variable created above and save the result as a variable
        invalid_listings = validate_policy_numbers(detailed_data)

        # check that the return value is a list
        self.assertEqual(type(invalid_listings), list)

        # check that the elements in the list are tuples
        # and that there are exactly three element in each tuple

def main (): 
    detailed_data = create_listing_database("html_files/search_results.html")
    output_csv(detailed_data, "airbnb_dataset.csv")

if __name__ == '__main__':
    # main()
    unittest.main(verbosity=2)