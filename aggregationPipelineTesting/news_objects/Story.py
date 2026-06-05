import uuid

class Story:

    def __init__(self, embedding_centroid, text, date = "0"):
        
        # Embedding score after clustering multiple stories and summarizing
        # Used for similarity comparison to timeline scores
        self.centroid = embedding_centroid
        
        # The AI summarized story content
        self.text = text

        # Date the story was covered
        self.date = date

        # ID for unique identification in stories table
        self.id = uuid.uuid4()

        # Generates a new timeline idin case there are no matching timelines for the story
        # If there are, this will be updated and it will be added to db
        self.timeline_id = uuid.uuid4()
    
    def update_timeline_id(self, id):

        self.timeline_id = id