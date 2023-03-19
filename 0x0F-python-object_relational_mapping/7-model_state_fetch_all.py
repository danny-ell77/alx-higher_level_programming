postgres_db = {
    "drivername": "postgres",
    "username": "postgres",
    "password": "postgres",
    "host": "192.168.99.100",
    "port": 5432,
}
print(URL(**postgres_db))
