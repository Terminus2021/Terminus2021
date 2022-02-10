from flask import Flask,render_template
app = Flask(__name__)
@app.route("/nameboard")
def name():
   user = {'username':''}
   post1 = {'authorname':'','body':''}
   html = '''
  <html>
  <head>
    <meta charset-"utf-8">
    <title>'''+user['username']+''' 的Flask 留言板</title>
  </head>
  <body>
    <h1>欢迎来到'''+user['username']+'''的Flask留言板！</h1>
    <div><p>'''+post1['authorname']+'''：<b>'''+post1['body']+'''</b></p></div>
    <div><p>'''+post2['authorname']+'''：<b>'''+post2['body']+'''</b></p></div>
    <span class="hidden-xs">Powered by Flask and Python.</span>
  </body>
  </html>
    '''
   return html
if __name__ == '__main__':
     app.run()