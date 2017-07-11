import edit_database

conditions = ['rain', 'snow', 'windy', 'hot', 'cold', 'chilly', 'neutral']

for condition in conditions:
    edit_database.create_image_type_table(condition)
    for i in range(1, 6):
        edit_database.add_image_to_table(condition)
