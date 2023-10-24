import mysql.connector
from flask import make_response

from config.config import dbconfig


class report_comment_model:
    def __init__(self):
        self.con = mysql.connector.connect(host=dbconfig['host'], user=dbconfig['username'],
                                           password=dbconfig['password'], database=dbconfig['database'])
        self.con.autocommit = True
        self.cur = self.con.cursor(dictionary=True)

    def all_report_comment_model(self):
        self.cur.execute("SELECT * FROM report_comment")
        result = self.cur.fetchall()
        if len(result) > 0:
            return {"payload": result}
            # return make_response({"payload":result},200)
        else:
            return "No Data Found"

    def add_report_comment_model(self, data):
        self.cur.execute(
            f"INSERT INTO user(link_avatar,user_name, ip_register, device_register, password, email,count_sukien,count_comment,count_view) "
            f"VALUES('{data['link_avatar']}', '{data['user_name']}', '{data['ip_register']}', '{data['device_register']}', '{data['password']}','{data['email']}',0,0,0)")
        return make_response({"message": "CREATED_SUCCESSFULLY"}, 201)
