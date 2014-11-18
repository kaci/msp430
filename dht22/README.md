dht22 sensor project

# create sqlite3 table

sqlite3 humy.db

sqlite> BEGIN;

sqlite> CREATE TABLE humytemp (date STRING, time STRING, humy REAL, temp REAL);

sqlite> COMMIT;

sqlite> .quit
