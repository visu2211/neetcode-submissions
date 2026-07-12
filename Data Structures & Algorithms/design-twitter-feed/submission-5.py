"""
view 10 most recent tweets within own news feed
each user and tweet have their own id
tweet ids in news feed should be ordered from most to least recent
"""
class User:
    
    def __init__(self, userId):
        self.followers = set([userId])
        self.following = set([userId])
        self.userId = userId
        self.tweets = []
    
    def follow(self, followerId):
        if self.userId == followerId:
            return
        self.following.add(followerId)

    def unfollow(self, followerId):
        if self.userId == followerId:
            return
        self.following.discard(followerId)

    def addTweet(self, tweetId, timestamp):
        self.tweets.append((timestamp, tweetId))

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)
        self.users[userId].addTweet(tweetId, -self.timestamp)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #to get 10 most recent following, add all tweets
        following = self.users[userId].following
        newsFeed = []
        for followeeId in following:
            newsFeed += self.users[followeeId].tweets
        
        heapq.heapify(newsFeed)
        res = []
        for _ in range(min(10, len(newsFeed))):
            res.append(heapq.heappop(newsFeed)[1])
        return res    

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].unfollow(followeeId)
        
