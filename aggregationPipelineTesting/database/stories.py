import psycopg2
from database.config import load_config


# Columns in story table:
# id | timeline_id | centroid | content

def insert_story(story):

    """Inserting a new story into stories postgres table"""


    # Date is automatically added via DEFAULT
    sql = """INSERT INTO stories (id, timeline_id, centroid, content)
            VALUES (%s, %s, %s, %s);"""
    
    config = load_config()

    try:

        with psycopg2.connect(**config) as conn:

            with conn.cursor() as cur:

                cur.execute(sql, (
                    str(story.id),
                    str(story.timeline_id),
                    story.centroid.tolist(),
                    story.text
                ))

                conn.commit()
    
    except (Exception, psycopg2.DatabaseError) as Error:

        print(Error)



def latest_timeline_stories(timeline_id: str):

    """Given a timeline, I get at most 3 of the latest stories in the timeline.
    This is for context when the llm is deciding on whether a story fits in a timeline candidate."""

    sql = """SELECT * FROM stories
            WHERE timeline_id = %s
            ORDER BY date DESC
            LIMIT 3;"""


    config = load_config()

    try:

        with psycopg2.connect(**config) as conn:

            with conn.cursor() as cur:

                cur.execute(sql, (
                    timeline_id,
                ))
                
                return cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as Error:

        print(Error)