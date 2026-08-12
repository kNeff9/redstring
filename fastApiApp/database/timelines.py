import psycopg2
from database.config import load_config

# Columns in timeline table:
# id | title | centroid

def fetch_all_timelines():

    """Getting all timeline objects from db"""

    sql = """SELECT * FROM timelines;"""

    config = load_config()

    try:

        with psycopg2.connect(**config) as conn:

            with conn.cursor() as cur:

                cur.execute(sql,)

                rows = cur.fetchall()

                return rows
    
    except (Exception, psycopg2.DatabaseError) as Error:

        print(Error)
        return []



def insert_timeline(timeline):

    """Inserting a new timeline object that holds one story"""


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