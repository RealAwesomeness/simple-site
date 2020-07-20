from flask import *
app = Flask(__name__)
app.config['FAVICONS_DIRECTORY'] = './favicons'
@app.route('/')
def index():
      return render_template("template.html", content="<b>soon there shall be content</b>")


if __name__ == '__main__':
   app.run(debug = True)