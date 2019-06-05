"""
A fair service scheduler based on priority queues
"""
from queue import PriorityQueue
import datetime
import config


class ServiceScheduler(object):
    """
    Allocates daily services for the given list of soldiers according
    to their available time
    """

    def __init__(self,
                 soldiers_dict
                 ):
        """
        :param soldiers_dict: dict of all the soldiers that will be given services
        :type soldiers_dict: dict[soldier.soldier_time.SoldierTime, list[soldier.soldier.Soldier]]
        """
        self.__soldiers_dict = soldiers_dict
        self.__soldiers_list = list(soldiers_dict.values())
        self.__services_dict = dict()

    def __get_available_soldiers_at_date(self, check_date, num_soldiers):
        """
        returns a priority queue that contains all the soldiers available at the given
        check date with pqueue key as the number of services they had. Notice that soldiers exceeded their
        maximum number of services will not be included even if they are available
        :param check_date: the time to filter soldiers based on their availability
        :type check_date: datetime.date
        :param num_soldiers: the required number of soldiers for scheduling
        :type num_soldiers: int
        :return: pqueue of soldiers available at check_date
        :rtype queue.PriorityQueue[soldier.soldier.Soldier]
        """
        ret = PriorityQueue()
        sold_list = list()
        for soldier_time in self.__soldiers_dict:
            if soldier_time.is_available(check_date):
                sold_list += [i for i in self.__soldiers_dict[soldier_time] if i.is_free()]
        [ret.put(i) for i in sorted(sold_list)[:num_soldiers]]
        return ret

    def allocate(self):
        """
        performs fair allocation for soldier services per day
        :return: a dict with key as date and values as list of soldiers
        :rtype: dict[datetime.date, list[soldier.soldier.Soldier]]
        """
        ret = dict()
        cfg = config.Config().get_instance()
        start_date = cfg.SCHEDULER_START_DATE
        num_per_svc = cfg.NUM_SOLDIERS_PER_DAY_SERVICE
        days = [start_date + datetime.timedelta(days=i) for i in range(cfg.SCHEDULER_INTERVAL_DAYS)]
        for d in days:
            day_pque = self.__get_available_soldiers_at_date(d, num_per_svc)
            for i in range(num_per_svc):
                s = day_pque.get()
                if s.is_free():
                    s.add_service()
                    day_pque.put(s)

            ret[d] = list()
            while(not day_pque.empty()):
                ret[d] += [day_pque.get()]
            ll = [i for i in ret[d] if i.num_services != 0]
            ret[d] = sorted(ll)[:num_per_svc]

        return ret