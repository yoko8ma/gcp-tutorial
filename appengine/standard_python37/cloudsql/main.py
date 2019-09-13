import responder
import datetime
import os
import sqlalchemy

db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

app = responder.API()

db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
        drivername='mysql+pymysql',
        username=db_user,
        password=db_pass,
        database=db_name,
        query={
            'unix_socket': '/cloudsql/{}'.format(cloud_sql_connection_name)
        }
    )
)

@app.route("/")
async def index(req, resp):
    with db.connect() as conn:
        results = []

        entries = conn.execute(
            "SELECT guestName, content FROM entries"
        ).fetchall()

        for entry in entries:
            results.append({
                'guestName': entry[0],
                'content': entry[1]
            })

    resp.media = results