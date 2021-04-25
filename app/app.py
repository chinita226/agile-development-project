"""Main application logic."""
import database

database.update("""INSERT INTO restaurants VALUES
    (123, 'name', 'sweden', '123456', 'username', '12345');""")

res = database.query("SELECT * FROM restaurants;")

print(res)

database.update("DELETE FROM restaurants WHERE orgNumber = 123;")

res = database.query("SELECT * FROM restaurants;")

print(res)
