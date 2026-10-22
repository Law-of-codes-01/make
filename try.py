from __init__ import create_app,create_db,db

law=create_app()
create_db()
if __name__=='__main__':
    law.run(debug=True)