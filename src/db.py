import sqlite3


class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def form_exists(self, user_id):
        result = self.cursor.execute("SELECT COUNT (*) FROM `forms` WHERE `users_id` = ?", (self.get_user_id(user_id),))
        result = result.fetchone()[0]

        if result == 0:
            return False
        elif result == 1:
            return True
        else:
            return None

    def get_user_id(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def get_photo_id(self, users_id):
        result = self.cursor.execute("SELECT `user_id` FROM `users` WHERE `id` = ?", (users_id,))
        return result.fetchone()[0]

    def get_username(self, user_id):
        result = self.cursor.execute("SELECT `username` FROM `forms` WHERE `users_id` = (SELECT `id` FROM `users` WHERE `user_id` = ?)", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_form(self, user_id, gender, interest, name, age, city, text, liked, username):
        self.cursor.execute("INSERT INTO `forms` (`users_id`, `name`, `age`, `city`, `text`, `gender`, `interest`, `liked`, `username`) \
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.get_user_id(user_id), name, age, city.title(), text, gender, interest, liked, username))
        return self.conn.commit()

    def add(user_id, gender, interest, name, age, city, text, self=None):
        self.cursor.execute("INSERT INTO `forms` (`users_id`, `name`, `age`, `city`, `text`, `gender`, `interest`) \
        VALUES(?, ?, ?, ?, ?, ?, ?)", (user_id, name, age, city.title(), text, gender, interest))
        return self.conn.commit()

    def update_text(self, user_id, new_text):
        self.cursor.execute("UPDATE `forms` SET `text` = ? WHERE `users_id` = ?", (new_text, self.get_user_id(user_id)))
        return self.conn.commit()

    def get_form(self, user_id):
        result = self.cursor.execute("SELECT * FROM `forms` WHERE `users_id` = ?", (self.get_user_id(user_id),))
        return result.fetchall()

    def delete_form(self, user_id):
        self.cursor.execute("DELETE FROM `forms` WHERE `users_id` = ?", (self.get_user_id(user_id),))
        return self.conn.commit()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM `users` WHERE `id` = ?", (self.get_user_id(user_id),))
        return self.conn.commit()

    def find_forms(self, user_id, interest, city, age):
        gender: str = ""
        if interest == "парни":
            gender = "парень"
        if interest == "девушки":
            gender = "девушка"

        result = self.cursor.execute("SELECT * FROM `forms` WHERE `users_id` != ? AND `gender` = ? AND `age` \
        BETWEEN ? AND ?", (self.get_user_id(user_id), gender, int(age) - 5, int(age) + 5))

        return result.fetchall()

    def get_user_liked(self, user_id):
        result = self.cursor.execute("SELECT `liked` FROM `forms` WHERE `users_id` = (SELECT `id` FROM `users` WHERE `user_id` = ?)", (user_id,))
        return result.fetchone()[0]

    def update_liked(self, user_id, new_liked):
        self.cursor.execute("UPDATE `forms` SET `liked` = ? WHERE `users_id` = ?", (new_liked, self.get_user_id(user_id)))
        return self.conn.commit()

    def restart(self):
        self.cursor.execute("DELETE FROM `forms` WHERE `users_id` = 20")
        self.cursor.execute("DELETE FROM `forms` WHERE `users_id` = 21")
        return self.conn.commit()

    def drop(self):
        self.cursor.execute("DELETE FROM `forms`")
        return self.conn.commit()

    def close(self):
        self.connection.close()