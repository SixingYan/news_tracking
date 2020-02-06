#! coding: utf-8
from setting import domain_mapping


class DateService(object):
    """docstring for FictionService"""

    def __init__(self, mg):
        self.mg = mg

    def do(self, date: str)->int:
        """"""
        date = '2020-02-05'
        y = '2020'
        m = '02'
        d = '05'
        domains = ['people']
        count = 0
        for d in domains:
            c = self.mg['news_corpus'][date].count({
                'url':     {'$regex': re.compile(".*{}.*".format(domain_mapping[d]['pattern'].format(y, m, d)))},
                'domain':  {'$in': domain_mapping[d]['domain']}
            })
            count += c

        return count

if __name__ == '__main__':
    test()
