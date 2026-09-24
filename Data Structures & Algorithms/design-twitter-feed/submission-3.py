class Twitter:

    def __init__(self):
        self.userFollowers = {}
        self.userTweets = {}
        self.tweetRank = -1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.userTweets:
            self.userTweets[userId].append([self.tweetRank, tweetId])
        else:
            self.userTweets[userId] = [[self.tweetRank, tweetId]]

        self.tweetRank -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        if userId in self.userTweets:
            for i in self.userTweets[userId][:]:
                heapq.heappush(tweets, i)

        if userId in self.userFollowers:
            for i in self.userFollowers[userId]:
                if i in self.userTweets:
                    for j in self.userTweets[i]:
                        heapq.heappush(tweets, j)
        

        res = []
        while tweets and len(res) < 10:
            res.append(heapq.heappop(tweets)[1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollowers:
            self.userFollowers[followerId] = set()

        self.userFollowers[followerId].add(followeeId)            
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # print(self.userFollowers)
        self.userFollowers[followerId].discard(followeeId)
        # print(self.userFollowers)
        
