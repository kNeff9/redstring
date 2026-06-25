import psycopg2
from database.config import load_config

# Columns in timeline table:
# id | title | centroid

def fetch_timeline_stories(timeline_id: str):

    """Getting all stories from timeline with id"""

    sql = """SELECT * FROM stories
            WHERE timeline_id = %s
            ORDER BY date DESC;"""

    config = load_config()

    try:

        with psycopg2.connect(**config) as conn:

            with conn.cursor() as cur:

                cur.execute(sql, (
                    timeline_id,
                ))

                rows = cur.fetchall()

                return rows
    
    except (Exception, psycopg2.DatabaseError) as Error:

        print(Error)

