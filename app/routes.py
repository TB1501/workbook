from flask import render_template

def register_routes(app):

    @app.route("/",methods=["GET"])
    def home():
        return render_template("index.html")
    
    @app.route("/login", methods=["GET"])
    def login():
        return render_template("login.html")
    
    @app.route("/register", methods=["GET"])
    def register():
        return render_template("register.html")
