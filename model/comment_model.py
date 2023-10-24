import mysql.connector
from flask import request, make_response

from config.config import dbconfig


class comment_model:
    def __init__(self):
        self.con = mysql.connector.connect(host=dbconfig['host'], user=dbconfig['username'],
                                           password=dbconfig['password'], database=dbconfig['database'])
        self.con.autocommit = True
        self.cur = self.con.cursor(dictionary=True)

    def get_comments(self):
        sql = "SELECT * FROM comment"
        conditions = []
        ip_comment = request.args.get('ip')
        uid = request.args.get('uid')

        if ip_comment:
            conditions.append("IP_Comment LIKE %s")
        if uid:
            conditions.append("id_user = %s")

        if conditions:
            sql += " WHERE " + " AND ".join(conditions)

        if ip_comment:
            self.cur.execute(sql, ('%' + ip_comment + '%',))
        elif uid:
            self.cur.execute(sql, (str(uid),))
        else:
            self.cur.execute(sql)
        result = self.cur.fetchall()
        if len(result) > 0:
            return {"payload": result}
        else:
            return {"message": "No data found"}

    def add_comment_model(self, data):
        sql = ("INSERT INTO comment(noi_dung_Comment,IP_Comment, device_Comment,"
               " id_toan_bo_su_kien, imageattach, thoi_gian_release,id_user,user_name,"
               "avatar_user,so_thu_tu_su_kien,location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        values = (
            data['noi_dung_Comment'] if 'noi_dung_Comment' in data else None,
            data['IP_Comment'] if 'IP_Comment' in data else None,
            data['device_Comment'] if 'device_Comment' in data else None,
            data['id_toan_bo_su_kien'] if 'id_toan_bo_su_kien' in data else None,
            data['imageattach'] if 'imageattach' in data else None,
            data['thoi_gian_release'] if 'thoi_gian_release' in data else None,
            data['id_user'] if 'id_user' in data else None,
            data['user_name'] if 'user_name' in data else None,
            data['avatar_user'] if 'avatar_user' in data else None,
            data['so_thu_tu_su_kien'] if 'so_thu_tu_su_kien' in data else None,
            data['location'] if 'location' in data else None
        )
        self.cur.execute(sql, values)
        return make_response("CREATED_SUCCESSFULLY", 201)

    def delete_comment_model(self, cid):
        self.cur.execute(f"DELETE FROM comment WHERE id_Comment={cid}")
        if self.cur.rowcount > 0:
            return make_response({"message": "DELETED_SUCCESSFULLY"}, 202)
        else:
            return make_response({"message": "CONTACT_DEVELOPER"}, 500)
