# save as remove_other_admins.py или запускай в Python интерактивно
from your_db_module import db  # замени на модуль, где лежит db.connect()

ADMIN_ID = 6518832274

conn, cursor = db.connect()
cursor.execute('DELETE FROM adm_id WHERE value != ?', (ADMIN_ID,))
conn.commit()
cursor.close()
conn.close()

print("Другие админы удалены, остался только ADMIN_ID")
