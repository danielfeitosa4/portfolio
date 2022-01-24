from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  # Ativando modo de desenvolvedor, agora toda modificação que eu fizer no meu template será atualizada automaticamente. 
    app.run(debug=True)