

# Timeline object meant to be a temporary holder of data for the additions of new timelines to the db
# Ex use:
# New story does not fit into existing timelines, so new object is created to hold values and add to db

class Timeline:

    def __init__(self, id, score, title):
        
        # UUID for organizing in database and connecting to stories
        self.id = id

        # Embedding score for comparison during story sorting process
        self.score = score

        # String title of timeline (May update over time, not sure yet)
        self.title = title

        # When a new timeline is created, it has >= 1 story
        self.numStories = 1

    