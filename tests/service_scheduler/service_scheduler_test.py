import unittest
from service_scheduler.service_scheduler import ServiceScheduler
from soldier.soldier_info_reader_excel import SoldierInfoReader
import config
import datetime


class ServiceSchedulerTest(unittest.TestCase):

    def setUp(self):
        print("poop")

    @classmethod
    def setUpClass(cls):
        pass
        #config.Config(testing=True)

    def test_allocate_db1(self):
        cfg = config.Config(testing=True)

        test_reader = SoldierInfoReader("assets/test_db1.xlsx")
        test_soldier_dict = test_reader.get_soldiers()

        test_soldier_sched = ServiceScheduler(test_soldier_dict)
        test_sched_result = test_soldier_sched.allocate()

        import matplotlib.pyplot as plt
        import pandas as pd
        objs = list()
        for d in test_sched_result:
            objs += [i for i in test_sched_result[d]]
            print(str(d) + ": " + str([i.name for i in test_sched_result[d]]))
        #plt.hist(objs)
        #
        pd.Series([i.name for i in objs]).value_counts().plot('bar')
        plt.show()
        #p

    def test_allocate_db0(self):
        cfg = config.Config(testing=True).get_instance()
        cfg.SCHEDULER_START_DATE = datetime.date(day=15, month=4, year=2019)
        cfg.SCHEDULER_INTERVAL_DAYS = 3
        cfg.NUM_SOLDIERS_PER_DAY_SERVICE = 2

        test_reader = SoldierInfoReader("assets/test_db0.xlsx")
        test_soldier_dict = test_reader.get_soldiers()

        test_soldier_sched = ServiceScheduler(test_soldier_dict)
        test_sched_result = test_soldier_sched.allocate()

        import matplotlib.pyplot as plt
        import pandas as pd
        objs = list()
        for d in test_sched_result:
            objs += [i for i in test_sched_result[d]]
            print(str(d) + ": " + str([i.name for i in test_sched_result[d]]))
        #plt.hist(objs)
        #
        pd.Series([i.name for i in objs]).value_counts().plot('bar')
        plt.show()
        #p

    def test_allocate_db2(self):
        cfg = config.Config(testing=True).get_instance()
        cfg.SCHEDULER_START_DATE = datetime.date(day=15, month=4, year=2019)
        cfg.SCHEDULER_INTERVAL_DAYS = 4
        cfg.NUM_SOLDIERS_PER_DAY_SERVICE = 3

        test_reader = SoldierInfoReader("assets/test_db2.xlsx")
        test_soldier_dict = test_reader.get_soldiers()

        test_soldier_sched = ServiceScheduler(test_soldier_dict)
        test_sched_result = test_soldier_sched.allocate()

        import matplotlib.pyplot as plt
        import pandas as pd
        objs = list()
        for d in test_sched_result:
            objs += [i for i in test_sched_result[d]]
            print(str(d) + ": " + str([i.name for i in test_sched_result[d]]))
        #plt.hist(objs)
        #
        pd.Series([i.name for i in objs]).value_counts().plot('bar')
        plt.show()
        #p