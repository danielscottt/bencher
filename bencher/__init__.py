# -*- coding: utf-8 -*-

from time import time

class Bencher():

    limit = 0

    def __init__(self, func):
        self.ops = []

        self._sorted = False
        self._func = func

    def __call__(self, *args, **kwargs):
        for i in range(0,self.limit):
            begin = time()
            if not 'ret' in locals():
                ret = self._func(*args, **kwargs)
            else:
                self._func(*args, **kwargs)
            end = time()
            self._add_to_ops(i, begin, end)
        print "%s:" % self._func.__name__
        print "  total exec time: 	%s" % self.total()
        print "  avg op time:		%iμs" % self.avg()
        print "  high op (seq %s):	%iμs" % (self.high()['seq'], int(self.high()['time']))
        print "  low op (seq %s):	%iμs" % (self.low()['seq'], int(self.low()['time']))
        return ret

    def avg(self):
        return self._get_total() / len(self.ops)

    def total(self):
        t = self._get_total()
        if t > 1000:
            return "%ims" % (t / 1000)
        return "%iμs" % t

    def high(self):
        if not self._sorted:
            self.ops.sort(key=lambda k: k['time'])
            self.sorted = True
        return self.ops[-1]

    def low(self):
        if not self._sorted:
            self.ops.sort(key=lambda k: k['time'])
            self.sorted = True
        return self.ops[0]

    def _add_to_ops(self, count, begin, end):
        op_time = ((end - begin) * 1000) * 1000
        self.ops.append({
            'time': op_time,
            'seq': count
        })

    def _get_total(self):
        return reduce(lambda x, y: x+y, [x['time'] for x in self.ops])
