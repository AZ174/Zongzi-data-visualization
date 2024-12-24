from flask import Flask
from flask import render_template
import pymysql
import pandas as pd
import json

app = Flask(__name__)


connection = pymysql.connect(
        host='192.168.146.138',
        user='root',
        password='123',
        database='mysql',
        charset='utf8')


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/about')
def about():  # put application's code here
    query = "SELECT id, clust1, clust2 FROM kmeans"

    # 使用 pandas 读取数据
    df = pd.read_sql(query, connection)
    data = df.to_dict(orient='records')
    json_data = json.dumps(data, indent=4)
    return render_template("about.html" , cluster=json_data)


@app.route('/contact')
def contact():  # put application's code here
    query = "SELECT name, sale FROM sales_by_store"
    df = pd.read_sql(query, connection)
    df1 = df.head(15)
    names = df1.iloc[:, 0].tolist()
    datas = df1.iloc[:, 1].tolist()
    query1 = "SELECT name,num FROM word"
    df2 = pd.read_sql(query1, connection)
    df2.columns = ['name', 'value']
    df2 = df2.head(50)
    data1 = df2.to_dict(orient='records')
    json_data1 = json.dumps(data1, indent=4)
    return render_template("contact.html", name=names, data=datas, json_data=json_data1)


@app.route('/service')
def service():  # put application's code here
    query = "SELECT province, sale FROM sales_by_province"
    df = pd.read_sql(query, connection)
    df.columns = ['name', 'value']
    data = df.to_dict(orient='records')
    json_data = json.dumps(data, indent=4)
    return render_template("service.html", province=json_data)

@app.route('/bingtu')
def bingtu():
    query = "SELECT ranges,num FROM bing"
    df = pd.read_sql(query, connection)
    df.columns = ['name', 'value']
    data = df.to_dict(orient='records')
    json_data = json.dumps(data, indent=4)
    return render_template("bingtu.html",datas=json_data)

if __name__ == '__main__':
    app.run()
