from flask import Flask,render_template
from getData import getDbInfo,dataModel,getTBdataFromDB
from DBtool import treeDataModel,getTableData
from flask import request, jsonify
from dataModel import setField
import json

app = Flask(__name__)


@app.route('/tree')
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
@app.route('/')
def tree():
    #返回数据到页面
    # retVal = dataModel()
    # 改为从sql server数据库中取数
    retVal = treeDataModel()
    return render_template('tree.html',retValue=retVal)

@app.route('/getTBdata',methods=['POST'])
def getTBdata():
    # data = json.loads(request.form.get('data'))
    data = request.form.get('data')
    print('--data--',data)

    #将data转为字典对象
    obj = json.loads(data)
    tb_name = obj['tbname']
    db_name = obj['dbname']
    field_list = setField(tb_name)
    print('--db_name：{}\ttb_name：{}--'.format(db_name,tb_name))

    retVal = getTableData(tb_name,db_name)

    retData = {}
    retData['tb_head'] = field_list
    retData['tb_data'] = retVal


    print('tb_data',retVal)
    return json.dumps(retData,ensure_ascii=False)

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run(debug=True)
