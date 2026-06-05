import psycopg2
from database.config import load_config

def insert_timeline(timeline):

    """Inserting a new timeline object that holds one story"""

    # Columns in timeline table:
    # id | title | centroid

    sql = """INSERT INTO timelines (id, title, centroid)
            VALUES (%s, %s, %s);"""
    
    config = load_config()

    try:

        with psycopg2.connect(**config) as conn:

            with conn.cursor() as cur:

                cur.execute(sql, (
                    str(timeline.id),
                    timeline.title,
                    timeline.centroid.tolist()
                ))

                conn.commit()
    
    except (Exception, psycopg2.DatabaseError) as Error:

        print(Error)