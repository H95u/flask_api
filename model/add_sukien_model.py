import mysql.connector
from flask import request, make_response

from config.config import dbconfig


class add_sukien_model:
    def __init__(self):
        self.con = mysql.connector.connect(host=dbconfig['host'], user=dbconfig['username'],
                                           password=dbconfig['password'], database=dbconfig['database'])
        self.con.autocommit = True
        self.cur = self.con.cursor(dictionary=True)

    def get_add_sukien(self):
        self.cur.execute("select * from add_sukien")
        result = self.cur.fetchall()
        if len(result) > 0:
            return {"payload": result}
        else:
            return "No Data Found"
