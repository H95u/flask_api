from app import app
from model.user_model import user_model
from flask import request

obj = user_model()


@app.route('/api/users')
def all_users():
    return obj.get_users()


@app.route("/api/users", methods=["POST"])
def add_user():
    return obj.add_user_model(request.json)


@app.route("/api/users", methods=["PUT"])
def update_user():
    return obj.update_user_model(request.form)


@app.route("/api/users/<uid>", methods=["DELETE"])
def delete_user(uid):
    return obj.delete_user_model(uid)


@app.route("/api/users/<uid>", methods=["PATCH"])
def patch_user(uid):
    return obj.patch_user_model(request.form, uid)
