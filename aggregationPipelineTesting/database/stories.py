import psycopg2
from database.config import load_config

def insert_story(story):

    """Inserting a new story into stories postgres table"""

    # Columns in story table:
    # id | timeline_id | centroid | content

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