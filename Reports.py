from main_ui import *


class Reporting(MyReportScreen.reportdb):
    def __init__(self):
        self.reportsdb = userReports
        self.rankingbd = {}

    def rankings(self):
        user_keys = self.reportsdb.keys()
        adrs_count = {}
        prblm_count = {}

        for name in user_keys:
            for num in range(len(self.reportsdb[name])):
                adrs = self.reportsdb[name][num][0]
                prblm = self.reportsdb[name][num][1]

                if adrs not in adrs_count:
                    adrs_count[adrs] = 1

                elif adrs in adrs_count:
                    adrs_count[adrs] += 1

                if prblm not in prblm_count:
                    prblm_count[prblm] = 1

                elif prblm in prblm_count:
                    prblm_count[prblm] += 1

        # sorted from lest to most
        adrs_count_sorted = sorted(adrs_count.items(), key=lambda x: x[1])
        prblm_count_sorted  = sorted(prblm_count.items(), key=lambda x: x[1])
