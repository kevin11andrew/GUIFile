import csv
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    rows=[]
    with open('facts.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    # print(rows)
    return render_template('p1.html',rows=rows)
    # return "<form><input type='text'></input></form>"


# view update delete
@app.route("/<action>/<id>", methods=['GET', 'POST'])
def view_update_delete(action, id):
    if request.method =="GET":
        if action=='add':
            temp=[id,"","","","","","","","","","","","","",""]
        else:
            print(action)
            print(id)
            temp=[]
            with open('facts.csv', 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    if row[0]==id:
                        temp=row[0]
        return render_template('p2.html', row=temp, action=action)
    
    elif request.method == "POST":
        fname=request.form["fname"]
        batch=request.form["batch"]
        ccode=request.form["ccode"]
        cname=request.form["cname"]
        cpw=request.form["cpw"]
        dept=request.form["dept"]

        dl=''
        if 'dl' in request.form.keys():
            dl=request.form["dl"]

        fcode=request.form["fcode"]

        room=''
        if 'room' in request.form.keys():
            room=request.form["room"]

        # print("ROOM=  ",room)
        # print("----------------------------------")
        # print(request.form.values())
        # print(fname)
        for i in request.form.keys():
            print(i,"\t",request.form[i]) 

        sec=request.form["sec"]
        sem=request.form["sem"]
        # print(request.form)
        return redirect('/')
        

@app.route("/add")
def add_course():
    ids=[]
    with open('facts.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            ids.append(row[0])
    print(ids)
    ids.sort()
    print(ids)
    id=0
    for i in ids:
        print(i)
        print(id)
        if int(i)!=id:
            break
        id+=1
    print(id)
    
    return redirect('/add/'+str(id))

