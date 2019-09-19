PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS "users";
DROP TABLE IF EXISTS "sekwencje";

CREATE TABLE "users"
(
    "id"       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "username" TEXT    NOT NULL,
    "password" TEXT    NOT NULL,
    "is_admin" BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO "users"
VALUES (1, 'Ola', 'pbkdf2:sha256:50000$F5xdsWLU$f01e92ee98190b796371b551f657bc806b415f5e374090058e26607fbf9cade0', 0),
       (2, 'Aga', 'pbkdf2:sha256:50000$KZ8tNqYD$c05449736ba6d231b043a2826ddff7a84d6e5fa3aaaa1e94b1b2390d7547971a', 0),
       (3, 'Ania', 'pbkdf2:sha256:50000$JSzIa7bc$4d7e75255448b25fe6bf53143c4953ac9016ce542860b4f4e68ad9732b60bb33', 0),
       (4, 'admin', 'pbkdf2:sha256:50000$3QnWdGBG$1a4098b934a8c2a526fec8dfe1a23fd0da2e2fecbd5183e8ea1e3ef1c238a43a',
        1);


CREATE TABLE "sekwencje"
(
    'id'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    'user_id' INTEGER NOT NULL,
    'nazwa' TEXT NOT NULL,
    'sekwencja_wejscie'	TEXT,
    'rodzaj_zmiany' TEXT,
    'sekwencja_wyjscie'	TEXT,
    'data'	TEXT,
    'godzina' TEXT,
    FOREIGN KEY ("user_id") REFERENCES "users" ("id")
);
