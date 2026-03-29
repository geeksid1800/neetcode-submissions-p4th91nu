'''
Need to follow and unfollow a user in O(1) so set is an obvious choice
Need to store all tweets by a user, and user will only tweet in chronological order,
so list will suffice.
Main complication will arise when we get 10 most recent tweets by users current user is following.
For that, we need to know when each tweet was posted. Use a 'sno' (serial no)
variable which will increment each time we tweet.
Now, follow a similar to merge K linked lists. Take the tweet lists of all users that current user
follows. Take the most recent tweets by each, add to a pq (max-heap, highest count is most recent).
When you remove the most recent tweet, add the next most recent post by the same tweeter to the pq.
'''
class Twitter:
    def __init__(self):
        self.sno = 0
        self.userTweets = defaultdict(list) #userID: list of [tweet #, tweetID]
        self.userFollows = defaultdict(set) #userID: set of userIDs that key userID follows

    def postTweet(self, userID: int, tweetID: int) -> None:
        self.userTweets[userID].append([-self.sno, tweetID]) #-ve for max-heap
        self.sno += 1

    def getNewsFeed(self, userID: int) -> List[int]:
        ans = []
        followingTweets = []
        print(f"User {userID} follows IDs {[userID, *self.userFollows[userID]]}")
        for followedID in [userID, *self.userFollows[userID]]: #user themselves+ppl they follow
            ix = len(self.userTweets[followedID]) - 1
            if ix >=0: #if user we are following has any tweets at all
                nSno, tweetID = self.userTweets[followedID][ix]
                followingTweets.append([ #want pq to be ordered by recency i.e. -S.no
                    nSno, tweetID, ix, followedID
                ])
            heapq.heapify(followingTweets)

        while len(ans) < 10 and followingTweets:
            recent = heapq.heappop(followingTweets)
            nSno, tweetID, ix, followedID = recent
            ans.append(tweetID)
            if ix>0:
                ix -= 1
                nSno, tweetID = self.userTweets[followedID][ix]
                heapq.heappush(followingTweets, [nSno, tweetID, ix, followedID])
        
        return ans

    def follow(self, followerID: int, followeeID: int) -> None:
        if followerID != followeeID:
            self.userFollows[followerID].add(followeeID)

    def unfollow(self, followerID: int, followeeID: int) -> None:
        if followerID != followeeID:
            self.userFollows[followerID].discard(followeeID)