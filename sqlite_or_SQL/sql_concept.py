# Any sql, ref doc
import sqlite3

conn =sqlite3.connect('new_or_old_db')
# cursor for lite
query = conn.cursor()

cmd = 'imported sql cmds or single line statement'
# single sql statement
query.execute(cmd)
# sql multiline script
query.executescript(cmd)