
from __init__ import create_app, db

law=create_app()

if __name__ == "__main__":
    create_db()
    law.run(debug=True)
