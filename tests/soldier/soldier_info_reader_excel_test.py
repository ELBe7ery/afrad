import unittest
import datetime
from soldier.soldier_info_reader_excel import SoldierInfoReader



class TestSoldierInfoReaderExcel(unittest.TestCase):

    def setUp(self):
        pass

    def soldiers_dict_to_list(self, lst):
        ret = []
        l = list(lst.values())
        for _l in l:
            for i in _l:
                ret += [i]
        return ret

    def test_get_soldiers_db1_load_soldiers(self):
        test_reader = SoldierInfoReader("assets/test_db1.xlsx")
        test_soldier_list = self.soldiers_dict_to_list(test_reader.get_soldiers())
        self.assertEqual(len(test_soldier_list), 40)

    def test_get_soldiers_db1_valid_soldier_info(self):
        test_reader = SoldierInfoReader("assets/test_db1.xlsx")
        test_soldier_list = self.soldiers_dict_to_list(test_reader.get_soldiers())
        self.assertTrue(any([i.name=="b8" and i.soldier_id==17 for i in test_soldier_list]))
        self.assertTrue(any([i.name=="c5" and i.soldier_id==23 for i in test_soldier_list]))
        self.assertTrue(any([i.max_num_svc==4 and i.soldier_id==37 for i in test_soldier_list]))


    def test_get_soldiers_db1_valid_soldier_availability(self):
        test_reader = SoldierInfoReader("assets/test_db1.xlsx")
        test_soldier_list = self.soldiers_dict_to_list(test_reader.get_soldiers())
        test_soldier = [i for i in test_soldier_list if i.name=="e3"][-1]
        test_date = datetime.date(year=2019, month=4, day=23)
        self.assertTrue(test_soldier.is_available_for_n_days(test_date, 1))
        self.assertTrue(test_soldier.is_available_for_n_days(test_date, 2))
        self.assertTrue(test_soldier.is_available_for_n_days(test_date, 3))
        self.assertTrue(test_soldier.is_available_for_n_days(test_date, 4))
        self.assertFalse(test_soldier.is_available_for_n_days(test_date, 5))
