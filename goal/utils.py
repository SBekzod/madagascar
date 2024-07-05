from django.db import connections

def dict_fetchall(sql, using='default'):
    with connections[using].cursor() as cursor:
        cursor.execute(sql)
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]




