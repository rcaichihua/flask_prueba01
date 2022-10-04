from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
  return """
  <h1 style="font-size: 64px; color: blue;">Hola Davy</h1>
  """
if __name__ == '__main__':
  app.run(debug=True)