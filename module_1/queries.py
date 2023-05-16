SELECT_ALL = '''SELECT character_id, name
                FROM charactercreator_character;'''
SELECT_ALL_FIVE = '''SELECT name,hp
                FROM charactercreator_character LIMIT 5;'''
CHAR_ID_80PLUS = '''SELECT * FROM charactercreator_character
                WHERE character_id>80;'''
CHAR_ID_AND = '''SELECT character_id,name
                FROM charactercreator_character
                WHERE character_id>80
                AND character_id<100;'''
CHAR_ID_BETWEEN = '''SELECT character_id,name
                FROM charactercreator_character
                WHERE character_id BETWEEN 5 AND 12;'''
UNIQUE_NAMES = '''SELECT DISTINCT name
                FROM charactercreator_character;'''
NAMES_GROUPBY = '''SELECT * FROM charactercreator_character
                GROUP BY name;'''
COUNT_GROUPBY = '''SELECT name, COUNT(*)
                FROM charactercreator_character
                GROUP BY name;'''
COUNT_ORDER_BY_ASC = '''SELECT name, COUNT(*)
                FROM charactercreator_character
                GROUP BY name ORDER BY COUNT(*)ASC;'''
COUNT_ORDER_BY_DESC = '''SELECT name, COUNT(*)
                FROM charactercreator_character
                GROUP BY name
                ORDER BY COUNT(*)DESC;'''
FILTER_WITH_HAVING = '''SELECT name, COUNT(*)
                FROM charactercreator_character
                GROUP BY name HAVING COUNT(*)=2;'''
ANOTHER_WAY = '''SELECT name, COUNT(*)
                FROM charactercreator_character
                GROUP BY name HAVING COUNT(*)=2
                ORDER BY name DESC;'''
JOIN_TABLES = '''SELECT * FROM charactercreator_character
                JOIN charactercreator_mage
                ON charactercreator_character.character_id
                =charactercreator_mage.character_ptr_id;'''
RENAME_AS_ALIAS = '''SELECT * FROM charactercreator_mage AS ccm
                JOIN charactercreator_character AS cc_char
                ON cc_char.character_id=ccm.character_ptr_id;'''
RENAME_COLUMN_ALIAS = '''SELECT name, COUNT(*) AS num_characters
                FROM charactercreator_character GROUP BY name;'''
# Instructor's example of how to properly tab over for such query statements.
AVG_ITEM_WEIGHT_PER_CHARACTER = '''
    SELECT cc_char.name, AVG(ai.weight) AS avg_item_weight
    FROM charactercreator_character AS cc_char
    JOIN charactercreator_character_inventory as cc_inv
    ON cc_char.character_id=cc_inv.character_id
    JOIN armory_item AS ai;
    ON ai.item_id=cc_inv.item_id;
    GROUP BY cc_char.character_id;
    '''
