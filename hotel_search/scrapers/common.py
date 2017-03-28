from tornado import gen
import simplejson as json
import os
from random import randint

class Scraper(object):

    provider = None

    @gen.coroutine
    def run(self):
        self.results = []

        # wait a bit
        # yield gen.sleep(1)

        self.load_results()
        self.results.sort(key=lambda r: r['ecstasy'])

        raise gen.Return(self.results)

    def load_results(self):
        self.load_fake_results(xrange(1, 20, self.step))

    def load_fake_results(self, range_iter):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/data.json') as data_file:
            dataset = json.load(data_file)
            data_keys = dataset.keys()

        for i in range_iter:
            data = dataset[data_keys[i]]
            data['provider'] = self.provider
            data['price'] = randint(50, 300)
            data['ecstasy'] = randint(1, 1000)
            self.results.append(data)

