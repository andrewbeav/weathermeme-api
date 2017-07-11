import sqlite3

conn = sqlite3.connect("db/memes.db")
c = conn.cursor()

def create_image_type_table(weather_condition):
    c.execute('CREATE TABLE IF NOT EXISTS ' + weather_condition + '(id INTEGER PRIMARY KEY AUTOINCREMENT)')
    conn.commit()

def add_image_to_table(weather_condition):
    c.execute('INSERT INTO ' + str(weather_condition) + ' DEFAULT VALUES')
    conn.commit()

if __name__ == "__main__":

    while True:
        command = input('> ')
        command_values = command.split(' ')

        if command_values[0].lower() == 'add_category':
            create_image_type_table(command_values[1])
        elif command_values[0].lower() == 'add_image':
            add_image_to_table(command_values[1])
        elif command_values[0].lower() == 'quit':
            break

    c.close()
    conn.close()


