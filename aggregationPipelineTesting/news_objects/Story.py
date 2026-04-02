

class Story:

    def __init__(self, embedding_centroid, text, date = "0"):
        
        # Embedding score after clustering multiple stories and summarizing
        # Used for similarity comparison to timeline scores
        self.centroid = embedding_centroid
        
        # The AI summarized story content
        self.text = text