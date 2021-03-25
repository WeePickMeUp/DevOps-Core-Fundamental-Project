from application import app, db
from application.models import Name, Groups
from flask import Flask, render_template, request, redirect, url_for 

@app.route("/")
def index():
    name_list = Name.query.all()
    return render_template('index.html', name_list=name_list)

@app.route("/group")
def groups():
    groups_list = Groups.query.all()
    return render_template('group.html', groups_list=groups_list)

@app.route("/read")
def read():
    return render_template('read.html')

@app.route("/create", methods=["POST"])
def new():
    title = request.form.get("title")
    new_new = Name(title=title, complete=False)
    db.session.add(new_new)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/creategroup", methods=["POST"])
def newgroups():
    title = request.form.get("title")
    new_newgroups = Groups(title=title, complete=False)
    db.session.add(new_newgroups)
    db.session.commit()
    return redirect(url_for("groups"))

@app.route("/update/<int:Name_id>")
def update(Name_id):
    name = Name.query.filter_by(id=Name_id).first()
    name.complete = not name.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:Name_id>")
def delete(Name_id):
    name = Name.query.filter_by(id=Name_id).first()
    db.session.delete(name)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/deletegroup/<int:Groups_id>")
def deletegroup(Groups_id):
    groups = Groups.query.filter_by(id=Groups_id).first()
    db.session.delete(groups)
    db.session.commit()
    return redirect(url_for("groups"))