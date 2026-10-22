
<<<<<<< HEAD

from __init__ import create_app, create_db

app = create_app()
create_db()
if __name__ == "__main__":
    
    app.run(debug=True)
=======
from __init__ import create_app, db,create_db

law=create_app()
create_db()
if __name__ == "__main__":
    law.run(debug=True)
>>>>>>> a4338c45e2bd5e111e2219fc24642992f502e041
