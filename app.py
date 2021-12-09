import os
from datetime import datetime
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def homepage():
    # get all forum posts newest first
    posts = mongo.db.forum_posts.find().sort('created_at', -1)
    return render_template("homepage.html", posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checks if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username Already Exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # if username doesn't exist adds new username to db
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checks if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # if username exists check if password matches
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                flash("Incorrect password")
                return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/post/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        post = {
            "post_title": request.form.get("post_title"),
            "post_description": request.form.get("post_description"),
            "post_image": request.form.get("post_image"),
            "created_by": session["user"],
            "created_at": datetime.now(),
            "edited_at": "n"
        }
        # inserts post into db
        mongo.db.forum_posts.insert_one(post)
        flash("Post Successful")
        return redirect(url_for("homepage"))

    return render_template("new_post.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    try:
        # grabs username of current session
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        # get all forum posts made by user
        users_posts = mongo.db.forum_posts.find(
            {"created_by": username}
        ).sort('sort_date', -1)

        if session["user"]:
            return render_template(
                "profile.html", username=username, users_posts=users_posts)

        return redirect(url_for("login"))

    except KeyError:
        flash("Not logged in")
        return redirect(url_for("homepage"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/post/<post_id>/view")
def post_details(post_id):
    # gets the post using the id
    post = mongo.db.forum_posts.find_one({"_id": ObjectId(post_id)})

    # finds all replies to the post with matching id
    replies = mongo.db.replies.find({"reply_to": post_id})

    return render_template("view_replies.html", post=post, replies=replies)


@app.route("/post/<post_id>/reply", methods=["GET", "POST"])
def post_reply(post_id):
    # gets the post using the id
    post = mongo.db.forum_posts.find_one({"_id": ObjectId(post_id)})

    # finds all replies to the post with matching id
    replies = mongo.db.replies.find({"reply_to": post_id})

    if request.method == "POST":
        reply = {
            "reply_to": post_id,
            "reply_description": request.form.get("reply_description"),
            "reply_image": request.form.get("reply_image"),
            "created_by": session["user"],
            "created_at": datetime.now(),
            "edited_at": "n"
        }
        # inserts reply into db
        mongo.db.replies.insert_one(reply)
        flash("Reply Successful")
        return redirect(url_for(
            "post_details", post_id=post_id, replies=replies))

    return render_template("reply.html", post=post)


@app.route("/post/<post_id>/delete")
def delete_post(post_id):
    try:
        # removes post with matching id from db
        mongo.db.forum_posts.remove({"_id": ObjectId(post_id)})
        flash("Post Deleted")
        return redirect(url_for("homepage"))
    except:
        return redirect(url_for("homepage"))


@app.route("/reply/<reply_id>/delete")
def delete_reply(reply_id):
    try:
        # removes reply with matching id
        mongo.db.replies.remove({"_id": ObjectId(reply_id)})
        flash("Reply Deleted")
        return redirect(url_for("homepage"))
    except:
        return redirect(url_for("homepage"))


# edit post
@app.route("/post/<post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    post = mongo.db.forum_posts.find_one(ObjectId(post_id))

    if request.method == "POST":
        edit = {
            "$set": {
                "post_title": request.form.get("post_title"),
                "post_description": request.form.get("post_description"),
                "post_image": request.form.get("post_image"),
                "edited_at": datetime.now()
            }
        }

        mongo.db.forum_posts.update_one({"_id": ObjectId(post_id)}, edit)
        flash("Edit Successful")
        return redirect(url_for("homepage"))

    return render_template("edit_post.html", post=post)


# edit reply
@app.route("/reply/<reply_id>/edit", methods=["GET", "POST"])
def edit_reply(reply_id):
    reply = mongo.db.replies.find_one(ObjectId(reply_id))

    if request.method == "POST":
        edit = {
            "$set": {
                "reply_description": request.form.get("reply_description"),
                "reply_image": request.form.get("reply_image"),
                "edited_at": datetime.now()
            }
        }

        mongo.db.replies.update_one({"_id": ObjectId(reply_id)}, edit)
        flash("Edit Successful")
        return redirect(url_for("homepage"))

    return render_template("edit_reply.html", reply=reply)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
