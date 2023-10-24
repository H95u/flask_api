import mysql.connector
from flask import make_response, request

from config.config import dbconfig


class user_model:
    def __init__(self):
        self.con = mysql.connector.connect(host=dbconfig['host'], user=dbconfig['username'],
                                           password=dbconfig['password'], database=dbconfig['database'])
        self.con.autocommit = True
        self.cur = self.con.cursor(dictionary=True)

    def get_users(self):
        sql = "SELECT * FROM user"
        conditions = []
        email = request.args.get('email')
        ip_register = request.args.get('ip_register')

        if email:
            conditions.append("email LIKE %s")
        if ip_register:
            conditions.append("ip_register LIKE %s")

        if conditions:
            sql += " WHERE " + " ".join(conditions)

        print(sql)
        if email:
            self.cur.execute(sql, ('%' + email + '%',))
        elif ip_register:
            self.cur.execute(sql, ('%' + ip_register + '%',))
        else:
            self.cur.execute(sql)
        result = self.cur.fetchall()
        if len(result) > 0:
            return result
            # return make_response({"payload":result},200)
        else:
            return {"message": "No data found"}

    def add_user_model(self, data):
        self.cur.execute(
            f"INSERT INTO user(link_avatar,user_name, ip_register, device_register, password, email,count_sukien,count_comment,count_view) "
            f"VALUES('{data['link_avatar']}', '{data['user_name']}', '{data['ip_register']}', '{data['device_register']}', '{data['password']}','{data['email']}',0,0,0)")
        return make_response({"message": "CREATED_SUCCESSFULLY"}, 201)

    def patch_user_model(self, data, uid):
        qry = "UPDATE user SET "
        for key in data:
            if key != 'id':
                qry += f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE id_user = {uid}"
        self.cur.execute(qry)
        if self.cur.rowcount > 0:
            return make_response({"message": "UPDATED_SUCCESSFULLY"}, 201)
        else:
            return make_response({"message": "NOTHING_TO_UPDATE"}, 204)

    def update_user_model(self, data):
        self.cur.execute(
            f"UPDATE user SET link_avatar='{data['link_avatar']}', user_name='{data['user_name']}', ip_register='{data['ip_register']}',"
            f" device_register='{data['device_register']}', password='{data['password']}', email='{data['email']}' WHERE id={data['id']}")
        if self.cur.rowcount > 0:
            return make_response({"message": "UPDATED_SUCCESSFULLY"}, 201)
        else:
            return make_response({"message": "NOTHING_TO_UPDATE"}, 204)

    def delete_user_model(self, uid):
        self.cur.execute(f"DELETE FROM user WHERE id_user={uid}")
        if self.cur.rowcount > 0:
            return make_response({"message": "DELETED_SUCCESSFULLY"}, 202)
        else:
            return make_response({"message": "CONTACT_DEVELOPER"}, 500)
