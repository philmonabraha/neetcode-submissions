class Twitter:

    def __init__(self):

        #filmon follows abebe
        self.followmap = {}
        self.tweets = {}
        self.time = 0

        #

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.tweets:
            self.tweets[userId] = []
        heapq.heappush(self.tweets[userId], [self.time, tweetId])
        self.time -= 1       

    def getNewsFeed(self, userId: int) -> List[int]:

        feed = []
        ids = self.followmap[userId]
        ids.add(userId)

        heap = []

        #top should be the old, min heap

        #iterate over the first items of each
        #if feed heap len over 10, pop the top
        
        for i in ids:

            time = self.tweets[i][0]
            tweetid = self.tweets[i][1]

            if len(heap) == 0:
                heapq.heappush(heap, [-time, tweetid])
            
            else:

                for u, t in range(self.tweets[i]):

                    if -1*t < heap[0][0]:
                        heapq.heappush(heap, [-time, tweetid])
                        
                        if len(heap) > 10:
                            heapq.heappop(heap)
                    
                    else:
                        break
        
        res = []
        for x in heap:
            res.append(x[1])
        
        return res



    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.followmap:
            self.followmap[followerId] = set()
        self.followmap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].remove(follweeId)
        
