#! coding: utf-8
import re
domain_mapping = {
    'jxcn': {
        'es_index': 'jxcn',
        'domains': ['jxcn.cn']
    },
    'jschina': {
        'es_index': 'jschina',
        'domains': ['jschina.com.cn']
    },
    'qhnews': {
        'es_index': 'qhnews',
        'domains': ['qhnews.cn']
    },
    'people': {
        'es_index': 'people',
        'domains': ['people.com', 'people.cn', 'people.com.cn'],
        'pattern': '{}/{}{}'

    },
    'xinhuanet': {
        'es_index': 'xinhuanet',
        'domains': ['xinhuanet.com'],
        'pattern': '{}-{}/{}'
    },
    'cnwest': {
        'es_index': 'cnwest',
        'proxy_rate': 0.5,
        'domains': ['cnwest.com']
    },
    'yicai': {
        'es_index': 'yicai',
        'proxy_rate': 0.1,
        'domains': ['yicai.com']
    },
    'jjckb': {
        'es_index': 'jjckb',
        'proxy_rate': 0.1,
        'domains': ['jjckb.cn', 'jjckb.xinhuanet.com']
    },
    'eastday': {
        'es_index': 'eastday',
        'proxy_rate': 0.5,
        'domains': ['eastday.com']
    },
    'gxnews': {
        'es_index': 'gxnews',
        'proxy_rate': 0.3,
        'domains': ['gxnews.com.cn']
    },
    'caijing': {
        'es_index': 'caijing',
        'proxy_rate': 0.3,
        'domains': ['caijing.com.cn']
    },
    'southcn': {
        'domains': ['southcn.com'],
        'pattern': '{}-{}/{}'
    },
    'zqrb': {
        'es_index': 'zqrb',
        'proxy_rate': 0.5,
        'domains': ['zqrb.cn']
    },
    'gzw': {
        'es_index': 'gzw',
        'proxy_rate': 0.4,
        'domains': ['gzw.net']
    },
    'hinews': {
        'es_index': 'hinews',
        'proxy_rate': 0.4,
        'domains': ['hinews.cn']
    },
    'hxnews': {
        'es_index': 'hxnews',
        'proxy_rate': 0.4,
        'domains': ['hxnews.com']
    },
    'sdnews': {
        'es_index': 'sdnews',
        'domains': ['sdnews.com.cn'],
        'pattern': '{}{}{}/'
    },
    'hebnews': {
        'es_index': 'hebnews',
        'proxy_rate': 0.4,
        'domains': ['hebnews.cn']
    },
    'hrn': {
        'es_index': 'hrn',
        'proxy_rate': 0.4,
        'domains': ['hrn.cn']
    },
    'qq': {
        'es_index': 'qq',
        'domains': ['qq.com'],
        'pattern': '{}{}{}/'
    },
    'cctv':{
        'es_index': 'cctv',
        'domains': ['cctv.com'],
        'pattern': '{}/{}/{}'
    }
}

class DateService(object):
    """docstring for FictionService"""

    def __init__(self, mg):
        self.mg = mg

    def do(self, date: str)->int:
        """"""
        print(date)
        y = date[:4]
        m = date[4:6]
        d = date[6:8]
        print('{}-{}-{}'.format(y,m,d))
        domains = ['people', 'xinhuanet', 'qq', 'sdnews', 'cctv', 'southcn']
        count = 0
        for d in domains:
            c = self.mg['news_corpus']['{}-{}-{}'.format(y,m,d)].count({
                'url':     {'$regex': re.compile(".*{}.*".format(domain_mapping[d]['pattern'].format(y, m, d)))},
                'domain':  {'$in': domain_mapping[d]['domains']}
            })
            print('{} {}'.format(d, c))
            count += c

        return count

if __name__ == '__main__':
    pass
