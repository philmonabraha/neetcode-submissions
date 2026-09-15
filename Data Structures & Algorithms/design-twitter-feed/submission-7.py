class Twitter:

    def __init__(self):

        #filmon follows abebe
        self.followMap = {}
        self.tweetMap = {}
        self.time = 0

        #

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1       

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].remove(follweeId)
        
