import database


@database.connection_handler
def add_new_child(cursor, name:str, pesel:int):
    query = """
          INSERT INTO children (name, pesel) 
          VALUES (%(name)s, %(pesel)s); """
    data = {'name': name, 'pesel': pesel}
    cursor.execute(query, data)