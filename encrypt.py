from flask import Flask,request
import threading
app = Flask(__name__)
ap = Flask(__name__)
@app.route('/sinocrypt')
def crypt():
    html = '''
    <html>
    <head>
    <meta charset="utf-8">
    <title>Flaskcrypt</title>
    </head>
    <body>
    <h1>Flaskcrypt 基于Flask和ASCII的加密网页app</h1>
    <form name="sub" action="/crypt" method='POST'>
    <input type="text" name="shuru" value="请输入要加密的中文单字（UTF-8）"><br>
    <input type="submit" value="加密">
    </form>
    </body>
    </html>
    '''
    return html
@app.route('/crypt',methods = ['POST', 'GET'])
def cryp():
    if request.method=="POST":
      sb = request.form['shuru']
      enc = ord(sb)
      ets = str(enc)
      return ets
if __name__ == '__main__':
    app.run()