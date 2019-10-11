# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import mysql.connector as mariadb
import json
import mssql
# import pyodbc
import operator

user = 'root'
db = 'IR'
passwd = 'ubuntu@2015'
host = 'localhost'

# Create your views here.
@login_required
def statistics_enroll(request):
    connect = mariadb.connect(user=user, db=db, passwd=passwd, host=host, charset='utf8')
    cursor = connect.cursor()
    query = "SELECT * FROM reg_school;"
    cursor.execute(query)
    schools = cursor.fetchall()
    return render_to_response('statistics/statistics_enroll.html',RequestContext(request, locals()))

@login_required
def enrollQuery(request):
    minYear = request.GET.get("minYear")
    maxYear = request.GET.get("maxYear")

    CB_way_0 = request.GET.get("CB_way_0", "").encode("utf-8")
    CB_way_1 = request.GET.get("CB_way_1", "").encode("utf-8")
    CB_way = []
    CB_way.append(CB_way_0)
    CB_way.append(CB_way_1)
    CB_way = "('" + "', '".join(map(str, tuple(CB_way))) + "')"

    CB_np_0 = request.GET.get("CB_np_0", "").encode("utf-8")
    CB_np_1 = request.GET.get("CB_np_1", "").encode("utf-8")
    CB_np = []
    CB_np.append(CB_np_0)
    CB_np.append(CB_np_1)
    CB_np = "('" + "', '".join(map(str, tuple(CB_np))) + "')"

    CB_dn_0 = request.GET.get("CB_dn_0", "")
    CB_dn_1 = request.GET.get("CB_dn_1", "")
    CB_dn = []
    CB_dn.append(CB_dn_0)
    if CB_dn_1 != "":
        CB_dn.append("N")
        CB_dn.append("P")
        CB_dn.append("V")
    CB_dn = "('" + "', '".join(map(str, tuple(CB_dn))) + "')"

    CB_level_0 = request.GET.get("CB_level_0", "")
    CB_level_1 = request.GET.get("CB_level_1", "")
    CB_level_2 = request.GET.get("CB_level_2", "")
    CB_level_3 = request.GET.get("CB_level_3", "")
    CB_level_4 = request.GET.get("CB_level_4", "")
    CB_level_5 = request.GET.get("CB_level_5", "")
    CB_level = []
    CB_level.append(CB_level_0)
    CB_level.append(CB_level_1)
    CB_level.append(CB_level_2)
    CB_level.append(CB_level_3)
    CB_level.append(CB_level_4)
    CB_level.append(CB_level_5)
    CB_level = "('" + "', '".join(map(str, tuple(CB_level))) + "')"

    sname = request.GET.get("sname", "")

    domain = request.GET.get("domain")
    program = request.GET.get("program")
    classes = request.GET.get("class")
    mid = domain + program[1:] + classes[2:]

    bname = request.GET.get("bname", "%")

    minRate = request.GET.get("minRate")
    maxRate = request.GET.get("maxRate")

    if request.user.is_staff:
        connect = mariadb.connect(user=user, db=db, passwd=passwd, host=host, charset='utf8')
        cursor = connect.cursor()
        try:
            query = "SELECT * FROM reg_vw_enroll WHERE"
            query += " rsemester BETWEEN '" + minYear + "' AND '" + maxYear + "'"
            query += " AND scategory IN " + CB_way.decode("utf-8")
            query += " AND sattribute IN " + CB_np.decode("utf-8")
            query += " AND dnid IN " + CB_dn
            query += " AND lid IN " + CB_level
            query += " AND sname IN (" + sname + ")"
            query += " AND sname <> '實踐大學'".decode("utf-8")
            query += " AND mid LIKE '" + mid + "%'"
            query += " AND mname LIKE '%" + bname + "%'"
            query += " AND renroll BETWEEN '" + minRate + "' AND '" + maxRate + "'"
            query += " ORDER BY rsemester, renroll DESC"
            cursor.execute(query)
            data = json.dumps(cursor.fetchall())
            query = "SELECT * FROM reg_vw_enroll WHERE"
            query += " rsemester BETWEEN '" + minYear + "' AND '" + maxYear + "'"
            query += " AND scategory IN " + CB_way.decode("utf-8")
            query += " AND sattribute IN " + CB_np.decode("utf-8")
            query += " AND dnid IN " + CB_dn
            query += " AND lid IN " + CB_level
            query += " AND sname = '實踐大學'".decode("utf-8")
            query += " AND mid LIKE '" + mid + "%'"
            query += " AND mname LIKE '%" + bname + "%'"
            query += " AND renroll BETWEEN '" + minRate + "' AND '" + maxRate + "'"
            query += " ORDER BY rsemester, renroll DESC"
            cursor.execute(query)
            dataUSC = json.dumps(cursor.fetchall())
            return render_to_response('statistics/chart.html',RequestContext(request, {"data":data, "dataUSC":dataUSC}))
        except mariadb.Error as e:
            connect.rollback()
            return HttpResponse(e[1])
    else:
        return HttpResponseRedirect("/accounts/login/")

@login_required
def selectQuery(request):
    name = request.GET.get("name")
    value = request.GET.get("value")

    connect = mariadb.connect(user=user, db=db, passwd=passwd, host=host, charset='utf8')
    cursor = connect.cursor()

    try:
        query = "SELECT * FROM reg_" + name + " WHERE "
        query += name[:1] + "id LIKE '" + value + "%'"
        query += " ORDER BY " + name[:1] + "id"
        cursor.execute(query)
        data = {}
        data["name"] = name
        data["data"] = cursor.fetchall()
        return HttpResponse(json.dumps(data))
    except mariadb.Error as e:
        connect.rollback()
        return HttpResponse(e[1])

@login_required
def enrollMap(request):
    semester = request.GET.get("semester")
    m1 = request.GET.get("m1")
    m2 = request.GET.get("m2")
    m3 = request.GET.get("m3")

    connect = mariadb.connect(user=user, db=db, passwd=passwd, host=host, charset='utf8')
    cursor = connect.cursor()
    query = "SELECT name, zip FROM zips"
    cursor.execute(query)
    zip = {}
    for row in cursor.fetchall():
        zip[str(row[1])] = row[0]

    con_string = mssql.con_string
    cnxn = pyodbc.connect(con_string)
    cursor = cnxn.cursor()

    data = {}
    if m1 != None:
        cursor.execute("select SUBSTRING(A22, 1, 3) AS 'zip', COUNT(*) as 'total' from TBA where A20 = " + semester +  " group by SUBSTRING(A22, 1, 3) order by 'zip'")
        for row in cursor.fetchall():
            if row[0].encode("utf-8") in zip:
                if zip[row[0].encode("utf-8")] in data:
                    data[zip[row[0].encode("utf-8")]] += row[1]
                else:
                    data[zip[row[0].encode("utf-8")]] = row[1]

    if m2 != None:
        cursor.execute("select SUBSTRING(C27, 1, 3) AS 'zip', COUNT(*) as 'total' from TBC where C25 = " + semester +  " group by SUBSTRING(C27, 1, 3) order by 'zip'")
        for row in cursor.fetchall():
            if row[0].encode("utf-8") in zip:
                if zip[row[0].encode("utf-8")] in data:
                    data[zip[row[0].encode("utf-8")]] += row[1]
                else:
                    data[zip[row[0].encode("utf-8")]] = row[1]

    if m3 != None:
        cursor.execute("select SUBSTRING(B32, 1, 3) AS 'zip', COUNT(*) as 'total' from TBB where B30 = " + semester +  " group by SUBSTRING(B32, 1, 3) order by 'zip'")
        for row in cursor.fetchall():
            if row[0].encode("utf-8") in zip:
                if zip[row[0].encode("utf-8")] in data:
                    data[zip[row[0].encode("utf-8")]] += row[1]
                else:
                    data[zip[row[0].encode("utf-8")]] = row[1]

    data = json.dumps(data)

    cursor.execute("select A20 from TBA group by A20 order by A20")
    semester = []
    for row in cursor.fetchall():
        semester.append(row[0])
    semester = json.dumps(semester)

    return render_to_response('statistics/map.html', locals(), RequestContext(request, {"data":data, "semester":semester}))
