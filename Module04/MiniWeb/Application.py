import time
import re
from pymysql import connect
from urllib.parse import unquote

# 路由 (路径，对应的执行的代码)   路由列表 django框架添加路由的方式 -直观
route_list = [
    # ('/gettime.py', gettime),
    # ('/index.py', index)
    # ('/center.py', center)
]


def route(url):
    """装饰器工厂函数 接收路径参数"""
    def warpped(func):
        """装饰器函数 接收路径对应的函数 func就是被装饰器之前的函数的引用"""
        route_list.append((url, func))
        def inner():
            """在inner函数内部 才完成了func函数功能的拓展"""
            print("正在执行某些拓展功能")
            return func()
        return inner
    return warpped


# 只有手动的调用 gettime()函数才会执行 inner函数代码
@route('/gettime.html')
def gettime(path_info):
    """当用户请求/gettime.py执行当前函数"""
    return time.ctime()


@route("/center.html")
def center(path_info):
    """当用户请求/center.py执行当前函数"""
    # 从数据库中读取数据 - 动态资源
    data_from_mysql = ""
    # 连接ｍｙｓｑｌ
    try:
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cur = conn.cursor()
        sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus f on i.id = f.info_id;"""
        cur.execute(sql)

        # 获取ＳＱＬ语句的执行结果
        for line in cur.fetchall():
            data = """	<tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a></td>
            <td> <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s"></td>
            </tr>
            """ % (line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[0], line[0])
            data_from_mysql += data

        conn.commit()
    except Exception as e:
        conn.rollback()
        return "ERROR" + str(e)
    else:
        # 从本地将模板文件读取到内存中
        with open("./template/center.html", "r") as file:
            file_data = file.read()
        # 将动态资源替换到模板中  {%content%}
        #    正则    替换数据          整体的数据
        file_data = re.sub(r"\{%content%\}", data_from_mysql, file_data)

        # 通过返回值返回
        return file_data
    finally:
        cur.close()
        conn.close()

@route("/index.html")
def index(path_info):
    """当用户请求/index.py执行当前函数"""
    # 从数据库中读取数据 - 动态资源

    data_from_mysql = ""

    # 连接数据库 创建和数据库的连接
    conn = connect(host='localhost', port=3306, db='stock_db',
            user='root',password='mysql', charset='utf8')
    # 获取游标　.execute(sql)
    cur = conn.cursor()
    sql = "select * from info;"
    cur.execute(sql)

    # 获取ｓｑｌ执行结果　
    # print(cur.fetchall())
    for line in cur.fetchall():
        # (1, '000007', '全新好', '10.01%', '4.40%', Decimal('16.05'), Decimal('14.60'), datetime.date(2017, 7, 18))
        line_data = """
        <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s"></td>
    </tr>
        """ % (line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[1])
        data_from_mysql += line_data
    # 关闭游标和连接
    cur.close()
    conn.close()
    # 从本地将模板文件读取到内存中
    with open("./template/index.html","r") as file:
        file_data = file.read()

    # 将动态资源替换到模板中  {%content%}
    #    正则    替换数据          整体的数据
    file_data = re.sub(r"\{%content%\}", data_from_mysql, file_data)

    # 通过返回值返回
    return file_data

# 实现添加指定股票到收藏夹中 /add/000007.html /add/000036.html
# /add/\d{6}\.html

@route(r"/add/\d{6}\.html")
def add(path_info):
    """当用户在 股票信息页面 点击添加的时候 """
    print("in add")
    result = re.match(r"/add/(\d{6})\.html", path_info)
    # 从正则结果中获取到股票代码
    code = result.group(1)
    # 连接数据数据　将股票信息插入到收藏夹中
    try:
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cursor = conn.cursor()
        # 再插入数据之前 先判断一下 股票是否已经被收藏了
        sql = """select * from focus where info_id = (select id from info where code = %s);"""
        if cursor.execute(sql, [code]):
            return "哥们儿 已经添加过了 再添加我弄死你"

        sql = """insert into focus (info_id) select id from info where code =%s;"""
        cursor.execute(sql, [code])
        conn.commit()
    except Exception as e:
        conn.rollback()
        return "失败" + str(e)
    else:
        return "成功"
    finally:
        cursor.close()
        conn.close()

# 从收藏夹删除指定的股票
@route(r"/del/\d{6}\.html")
def delete(path_info):
    """当用户在 个人中心页面点击删除 /del/股票代码.html"""
    print("in delete")
    # 获取股票代码
    result = re.match(r"/del/(\d{6})\.html", path_info)
    stock_code = result.group(1)

    # 连接数据 从数据库中删除指定股票代码的数据
    try:
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cursor = conn.cursor()
        sql = """delete from focus where info_id = (select id from info where code=%s);"""

        cursor.execute(sql, [stock_code])
        conn.commit()
    except Exception as e:
        conn.rollback()
        return "删除失败" + str(e)
    else:
        return "删除成功"
    finally:
        cursor.close()
        conn.close()


@route(r"/update/\d{6}\.html")
def update(path_info):
    """/update/000007.html 获取000007股票信息和备注的  页面"""
    # 获取用户需要修改备注的 股票代码
    result = re.match(r"/update/(\d{6})\.html", path_info)
    stock_code = result.group(1)

    # 连接数据库
    try:
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cursor = conn.cursor()
        sql = """select note_info from focus where info_id = (select id from info where code = %s);"""
        if cursor.execute(sql, [stock_code]) == 0:
            return "ERROR"
        # 从SQL结果中获取备注信息
        # print(cursor.fetchone()) ('潜力股',)

        note_info = cursor.fetchone()[0]
        conn.commit()
        # 读取模板文件
        with open("./template/update.html",'r') as file:
            html_data = file.read()

    except Exception as e:
        conn.rollback()
        return "ERROR" + str(e)
    else:
        # 完成模板替换 股票代码{%code%} 备注信息{%note_info%}
        html_data = re.sub(r"\{%code%\}", stock_code, html_data)
        html_data = re.sub(r"\{%note_info%\}", note_info, html_data)

        return html_data
    finally:
        cursor.close()
        conn.close()

#        /update/股票代码/新备注信息.html


@route(r"/update/(\d{6})/(.*)\.html")
def update_note_info(path_info):
    # 根据路劲提取股票代码 和 新备注
    result = re.match(r"/update/(\d{6})/(.*)\.html", path_info)
    stock_code, new_note_info = result.group(1,2)

    # 对可能存储的 URL编码 进行解码
    new_note_info = unquote(new_note_info)

    # 根据股票代码修改某只股票的备注为 新备注
    try:
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cursor = conn.cursor()
        sql = """update info join focus on info.id = focus.info_id set focus.note_info = %s where info.code = %s;"""
        cursor.execute(sql, [new_note_info, stock_code])

        conn.commit()
    except Exception as e:
        conn.rollback()
        return "更新备注失败" + str(e)
    else:
        return "更新备注成功"
    finally:
        cursor.close()
        conn.close()


def app(environ, start_response):
    # 参数1 一个存储的HTTP请求相关的 字典 其中PATH_INFO表示用户请求的资源路径
    # 参数2 是一个函数的引用

    # 通过字典取出     用户的资源请求路径
    path_info = environ['PATH_INFO']
    print("收到用户的动态资源请求", path_info)
    print(route_list)
    # 收到用户的资源请求的  遍历路由列表
    for url, func in route_list:
        # /add/000007.html  == /add/\d{6}\.html
        # if path_info == url:
        # 由于路由中已经含有正则了 不能进行完全的等价匹配 而应该使用正则 和 用户路径进行匹配
        if re.match(url, path_info):
            start_response('200 OK', [('Server', 'PWS9.0')])
            return func(path_info)
    else:
        # 设置响应状态和响应头数据
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        # 返回值是 响应体数据
        return 'Hello World!!!!!!!!'