'''
Test the x-axis labels read in from the json file
are what we expect for the date unit. assertCountEqual
will check if the list size is identical as well as if
the contents of the list are identical.
'''
import unittest
import GetXaxis

class TestGetXaxis(unittest.TestCase):
    def setUp(self):
        self.expected_day_axis = ["12AM", "1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM", "9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM", "7PM", "8PM", "9PM", "10PM", "11PM"]
        self.results_day_axis = GetXaxis.get_x_axis('DAY')
        self.expected_week_axis = [ "Mon","Tue", "Wed" ,"Thu", "Fri", "Sat", "Sun"]
        self.results_week_axis = GetXaxis.get_x_axis('WEEK')
        self.expected_month_axis = ["Jan", "Feb", "Mar" ,"Apr", "May", "Jun", "Jul","Sep","Oct","Nov","Dec"]
        self.results_month_axis = GetXaxis.get_x_axis('MONTH')

    def test_eq(self):
        self.assertCountEqual(self.results_day_axis ,self.expected_day_axis)
        self.assertCountEqual(self.results_week_axis ,self.expected_week_axis)
        self.assertCountEqual(self.results_month_axis ,self.expected_month_axis)


if __name__ == '__main__':
    unittest.main()
