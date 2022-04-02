class Config:
    DEBUG = True
    SECRET_KEY = "a\xc8@\xcd\xf3*\xcc\xea\xff\xc3X\x12\xb0`\xf5\x1a\x13\x8e6}\x9fk\x14j"
    db = {
        "user": "root",
        "password": "1234",
        "host": "127.0.0.1",
        "port": "3306",
        "database": "usearch",
    }
    SQLALCHEMY_DATABASE_URI = (
        "mysql://"
        + db["user"]
        + ":"
        + db["password"]
        + "@"
        + db["host"]
        + ":"
        + db["port"]
        + "/"
        + db["database"]
        + "?charset=utf8"
    )