"""
Helper class for reading soldier related info from external file
and building the proper objects
"""
from soldier.isolder_info_reader import ISoldierInfoReader
from soldier.soldier_time import SoldierTime
from soldier.soldier import Soldier
import pandas as pd


class SoldierInfoReader(ISoldierInfoReader):
    """
    Soldier info reader for excel data sources
    """
    def __init__(self, excel_name):
        self.__soldier_df = pd.read_excel(excel_name, sheet_name=0)
        self.__soldier_time_df = pd.read_excel(excel_name, sheet_name=1)
        self.__soldier_time_name_df = pd.read_excel(excel_name, sheet_name=2)
        self.__max_soldier_days_df = pd.read_excel(excel_name, sheet_name=3)

    def get_soldiers(self):
        """
        :rtype: dict[SoldierTime, list[Soldier]]
        """
        dofaat = self.__get_soldier_times()
        ret = {i:list() for i in set(dofaat.values())}
        soldiers_max_svc = self.__get_soldier_max_svc()
        for i in self.__soldier_df.itertuples():
            dofaa = dofaat[i.dofaa_id]
            s = Soldier(
                name=i.soldier_name,
                soldier_id=i.soldier_id,
                service_time=dofaa
            )
            if i.soldier_id in soldiers_max_svc.keys():
                s.max_num_svc=soldiers_max_svc[i.soldier_id]
            ret[dofaa] += [s]
        return ret

    def __get_name_dict(self):
        ret = dict()
        for i in self.__soldier_time_name_df.itertuples():
            ret[i.dofaa_id] = i.name
        return ret

    def __get_soldier_times(self):
        """
        rtype: dict[int, SoldierTime]
        """
        ret = dict()
        dofaat_name = self.__get_name_dict()
        for i in self.__soldier_time_df.itertuples():
            if i.dofaa_id not in ret.keys():
                ret[i.dofaa_id] = SoldierTime(dofaat_name[i.dofaa_id], i.dofaa_id)
            dofaa = ret[i.dofaa_id]
            dofaa.add_available_period(i.available_from.date(),
                                       i.available_till.date())
        return ret

    def __get_soldier_max_svc(self):
        ret = dict()
        for i in self.__max_soldier_days_df.itertuples():
            ret[i.soldier_id] = i.max_svc
        return ret