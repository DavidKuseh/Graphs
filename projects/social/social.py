import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        # generate all possible friendship combinations
        possible_friendships = []
        # avoid dups by making sure the first number is smaller than the second
        # iterate over user id in users...
        for user in range(1, self.last_id + 1):
            # iterate over friend id in in a range from user id + 1 to last id + 1...
            for friend in range(user + 1, self.last_id + 1):
                # append a user id and friend id tuple to the possible friendships
                possible_friendship = (user, friend)
                possible_friendships.append(possible_friendship)
                
        # shuffle friendships random import
        random.shuffle(possible_friendships)
    
        # create friendships for the first N pairs of the list
        # N is determined by the formula: num users * avg friendships // 2
        # NOTE: need to divide by 2 since each add_friendship() creates 2 friendships
        total_friendships = num_users * avg_friendships // 2
        random_friendships = possible_friendships[:total_friendships]
    
        # iterate over a range using the formula as the end base...
        for frienship in random_friendships:
            # set friendship to possible friendships at index
            # add friendship of frienship[0], friendship[1]
            self.add_friendship(frienship[0], frienship[1])

    def get_friendships(self, user_id):
        return self.friendships[user_id]

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        
        # create queue
        q = Queue()
        
        # set user id to path
        path = [user_id]
        # enqueue path 
        q.enqueue(path)
        
        # while queue is not empty set the last user as the new user
        while q.size() > 0:
            current_path = q.dequeue()
            new_user_id = current_path[-1]
            
            # if new user not visited, visit and include in current path
            if new_user_id not in visited:
                visited[new_user_id] = current_path
                
                # get friends of new user
                friends = self.get_friendships(new_user_id)
                # loop through friends, and append each friend to current path
                for friend in friends:
                    path_copy = list(current_path)
                    path_copy.append(friend)
                    q.enqueue(path_copy)
                    
        # return path
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
    

