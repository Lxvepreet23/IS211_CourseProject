Select * From blog
CREATE TABLE "blog entry" (
	"blog_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"title"	TEXT NOT NULL,
	"body"	TEXT NOT NULL
INSERT INTO "blog" ("title", "body") VALUES (?, ?)
)

Select * From user
CREATE TABLE "user" (
	"user_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"Username"	TEXT NOT NULL UNIQUE,
	"Password"	TEXT NOT NULL
)