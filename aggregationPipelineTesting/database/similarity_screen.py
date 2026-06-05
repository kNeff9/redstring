import psycopg2
from database.config import load_config
import uuid


def get_timeline_candidates(story):

    """Getting timlines with similar centroid to story object"""


    sql = """SELECT id, title, centroid
            FROM timelines
            WHERE centroid <=> %s::vector < %s;"""
    
    diff_threshold = 0.4

    config = load_config()

    try:

        with psycopg2.connect(**config) as conn:

            with conn.cursor() as cur:

                cur.execute(sql, (
                    story.centroid.tolist(),
                    diff_threshold
                ))
                
                return cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as Error:

        print(Error)
