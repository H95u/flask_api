from app import app
from model.comment_model import comment_model
from flask import request

obj = comment_model()


@app.route('/api/comments')
def all_comments():
    return obj.get_comments()


@app.route("/api/comments/<cid>", methods=["DELETE"])
def delete_comments(cid):
    return obj.delete_comment_model(cid)


@app.route("/api/comments", methods=["POST"])
def add_comments():
    return obj.add_comment_model(request.form)
