from flask import Flask,render_template
from getData import getDbInfo,dataModel,getTBdataFromDB
from flask import request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/index')
def index():
    retValue = getDbInfo()
    print('retValue:',retValue)
    return render_template('index.html',retValue=retValue)

#请求数据库和表结构
@app.route('/tree')
def tree():
    #返回数据到页面
    retVal = dataModel()
    return render_template('tree.html',retValue=retVal)
@app.route('/getTBdata',methods=['POST'])
def getTBdata():
    # data = json.loads(request.form.get('data'))
    data = request.form.get('data')
    print('--data--',data)
    tb_name = json.loads(data)['tbname']
    print('--tb_name--', tb_name)
    retVal = getTBdataFromDB(tb_name)

    print('tb_data',retVal)
    return json.dumps(retVal,ensure_ascii=False)

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run(debug=True)
