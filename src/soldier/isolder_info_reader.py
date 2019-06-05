"""
Defines the contract for soldier data readers

Currently data is stored and fetched from excel sheets, later it will be fetched from
some database
"""


class ISoldierInfoReader(object):

    def get_soldiers(self):
        """
        returns an array of soldier objects initialized from the implementation
        specific data source
        :rtype: list[soldier.soldier.Soldier]
        """
        raise NotImplementedError()
