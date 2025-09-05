# Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).
# System should accept a timestamp parameter (in seconds granularity),
# You may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
# Several hits may arrive roughly at the same time.

from collections import deque

class Counter:
    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp):
        self.queue.append(timestamp)

    def gethits(self, timestamp):
        while self. queue and (timestamp - self.queue[0]) >= 300:
            self.queue.popleft()
        print(len(self.queue))

c = Counter()
c.hit(1)
c.hit(2)
c.hit(3)
c.gethits(4)
c.hit(300)
c.gethits(300)
c.gethits(301)