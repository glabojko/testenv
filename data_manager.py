import database


@database.connection_handler
def add_child_to_database(cursor, id:str, name:str, pesel:str):
    query = """
          INSERT INTO children (id, name, pesel) 
          VALUES (%(id)s, %(name)s, %(pesel)s); """
    data = {'id': id, 'name': name, 'pesel': pesel}
    cursor.execute(query, data)