import psycopg2
from database.config import load_config


def already_seen(url):

    """Checking if a url is already in seen_urls table"""

    sql = """SELECT 1 FROM seen_urls
            WHERE url = %s;"""
    
    config = load_config()

    try:

        with psycopg2.connect(**config) as conn:

            with conn.cursor() as cur:

                cur.execute(sql, (url,))

                return cur.fetchone() is not None
    
    except (Exception, psycopg2.DatabaseError) as Error:

        print(Error)


def insert_url(url):

    """Inserting a new url into seen_urls postgres table"""

    # Columns in story table:
    # url | added_at

    # Date is automatically added via DEFAULT
    sql = """INSERT INTO seen_urls (url)
            VALUES (%s);"""
    
    config = load_config()

    try:

        with psycopg2.connect(**config) as conn:

            with conn.cursor() as cur:

                cur.execute(sql, (
                    url,
                ))

                conn.commit()
    
    except (Exception, psycopg2.DatabaseError) as Error:

        print(Error)

