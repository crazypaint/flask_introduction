from flask import Flask
from routes import initialise_routes

app = Flask(__name__)

initialise_routes(app)
# main trick
# if this file is run directly, do this
if __name__ == "__main__":
    app.run(debug=True)


# HTTP Methods
# GET - read - SELECT
# POST - create - INSERT INTO
# PUT - update - UPDATE SET
# PATCH - partial update - UPDATE SET
# DELETE - delete - DELETE

# CRUD data

# URL -> invoke function
# 1. decorator
# 2. function call

# 1.
# @app.route("/api/hello/")
# def hello():
#     return "Hello from Flask!!!!!"

# # 2.
# def db():
#     return "Hello DB"
# # url, text-based name for end point, function pointer
# app.add_url_rule("/api/db/", "db", db)


