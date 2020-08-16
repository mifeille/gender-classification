from flask import Flask
from app import views


app = Flask(__name__)


# urls
app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/gender', 'gender', views.gender, methods=['GET', 'POST'])


if __name__ == "__main__":
    app.run(debug=True)
