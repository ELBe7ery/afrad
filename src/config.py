"""
Global configurations
"""
import datetime

class ConfigBase(object):
    SCHEDULER_START_DATE = None
    NUM_SOLDIERS_PER_DAY_SERVICE = 18
    SCHEDULER_INTERVAL_DAYS = 30

class DevConfig(ConfigBase):

    # day to start scheduling from
    SCHEDULER_START_DATE = datetime.datetime.now()



class TestConfig(ConfigBase):
    SCHEDULER_START_DATE = datetime.date(day=23, month=4, year=2019)



class Config(object):
    """
    Global configuration singleton
    """
    __CONFIG_OBJ = None

    def __init__(self,
                 testing=False):
        """
        :param testing: testing configuration
        :type testing: bool
        """
        if Config.__CONFIG_OBJ is not None: return
        if testing:
            Config.__CONFIG_OBJ = TestConfig()
        else:
            Config.__CONFIG_OBJ = DevConfig()

    def get_instance(self):
        """
        :return: the app configuration object
        :rtype: ConfigBase
        """
        return Config.__CONFIG_OBJ
