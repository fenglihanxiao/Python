"""
案例找出真凶
分析：
1.姓 name                startswith
2.名 name nick_name      find
3.性别 gender            ==
4.血型 blood             ==
5.籍贯 native            find
6.出生日期 idcard        切片，比较运算
"""
db_infos = [{"name": "张三丰","gender": 1, "nick_name": "三爷", "idcard": "110101153808081017", "blood": "b", "native":"湖北省丹江口市武当山玉虚宫"},{"name": "张大彪","gender": 1, "nick_name": "斌仔", "idcard": "130323197711111011", "blood": "b", "native":"河北省秦皇岛市武山海关区鞋拔子路胶水胡同103"}]
# 1. 循环列表，取出个人信息
for person in db_infos:
    # 2.取出个人信息
    name = person["name"]
    nick_name = person["nick_name"]
    gender = person["gender"]
    blood = person["blood"]
    native = person["native"]
    idcard = person["idcard"]
    # 3.判断是否满足条件
    # 3.1 所有条件都满足，打印个人信息
    # 3.2 只要有一个条件不满足，检查下一个人
    if not name.startswith("张") :
        continue
    if name.find("斌") == -1 and nick_name.find("斌") == -1 :
        continue
    if gender != 1:
        continue
    if blood.lower() != "b":
        continue
    if native.find("河北") == -1:
        continue
    # 身份证号： XXXXXX XXXX XX XX XXX X
    if int(idcard[6:10]) < 1975 or int(idcard[6:10]) > 1978 :
        continue

    # 设计字典，做对应关系（映射）
    genders = {1:"男",0:"女",-1:"不详"}

    # 到达此处说明所有条件都已经通过，打印个人信息
    print("姓名:"+name+",曾用名:"+nick_name+",性别:"+genders[gender]+",血型:"+blood+",籍贯:"+native+",身份证号:"+idcard)


