import random
from collections import defaultdict

# Step 1: Create list of friends
friends = ['A', 'B', 'C', 'D', 'E']
friend_map = defaultdict(set)

# Randomly assign 1 to 3 friends for each person (excluding themselves)
for person in friends:
    possible_friends = [f for f in friends if f != person]
    num_friends = random.randint(1, 3)
    selected = random.sample(possible_friends, num_friends)
    for f in selected:
        friend_map[person].add(f)
        friend_map[f].add(person)  # ensure mutual friendship

# Display friendship map
print("Friendship Mapping:")
for person, f_list in friend_map.items():
    print(f"{person}: {sorted(f_list)}")

# Step 2: Find who has most and least friends
def find_most_least_friends(fmap):
    max_friends = max(fmap.items(), key=lambda x: len(x[1]))
    min_friends = min(fmap.items(), key=lambda x: len(x[1]))
    return max_friends, min_friends

most, least = find_most_least_friends(friend_map)
print(f"\nMost friends: {most[0]} with {len(most[1])} friends")
print(f"Least friends: {least[0]} with {len(least[1])} friends")