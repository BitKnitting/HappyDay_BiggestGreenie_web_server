'''
Test readings came back.
'''
from calendar import monthrange
import unittest
import EnergyPlot as ep
import testRoutines as protoDates

class TestEnergyPlot(unittest.TestCase):
    def setUp(self):
        self.month, self.year = protoDates.get_random_date('MONTH')


    # BEGIN Testing get_month_list()
    def test_proto_month_in_test_db(self):
        ''' For testing, I am using data I got awhile back that is
        stored in a peewee database.
        Only Nov and Dec are available test values.
        '''
        self.assertTrue(11 <= self.month <= 12)

    def test_proto_year_in_test_db(self):
        '''The test database has readings for 2017 only '''
        self.assertEqual(self.year,2017)


    def test_bad_month(self):
        '''-1 is returned if the month can't be used. '''
        bad_reading = ep.get_month_list(555,555)
        self.assertEqual(bad_reading,-1)


    def test_good_month(self):
        '''See if the number returned in the list of energy
        readings is the right number for the month
        '''
        dates_for_month = monthrange(self.year,self.month)
        list_of_range_dates = list(dates_for_month)
        y = ep.get_month_list(self.month,self.year)
        self.assertEqual(len(y) ,list_of_range_dates[-1])
    # END Testing get_month_list()
        

if __name__ == '__main__':
    unittest.main()
