

from __init__ import create_app, create_db

app = create_app()
create_db()
if __name__ == "__main__":
    
    app.run(debug=True)