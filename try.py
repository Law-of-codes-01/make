# from __init__ import create_db
# from flask import current_app

# create_db()

# current_app.run(debug=True)

from __init__ import create_app, create_db

app = create_app()

if __name__ == "__main__":
    create_db()
    app.run(debug=True)