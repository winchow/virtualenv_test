from django.contrib.auth.models import User
from django.template.loader import get_template
from django.db import DatabaseError, transaction
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse
from exam.models import Lac,Subject
from django.views.generic.list import ListView
import json
import ast
import io
import xlwt
from .form import NameForm
import pandas as pd
import math



def jo(request):
	data ='static/scidb_staff.json'
	with open(data, 'r', encoding="utf-8") as fp:
		data = json.load(fp)
		#print(data)
		print(type(data[1]))
		print(data[1])
		for d in data:
			print(d)
			with transaction.atomic():
				Lac.objects.update_or_create(**d)
		# for i in len(data):
			# o = Lac.objects.update_or_create(data)
		return HttpResponse("Success")

def LacListView(request):
    thing_list = list(Lac.objects.all().values_list('name',flat=True))
    return render(request, 'form2.html', {'thing_list':thing_list})

def saved(request):
    print(request.POST)
    sub_id = request.POST.get("sub_id", "")
    academic_year = request.POST.get("academic_year", "")
    amount = 1
    TotalStu1 = request.POST.get("TotalStu1", "")
    TotalStu2 = request.POST.get("TotalStu2", "")
    if TotalStu2 != "":
        amount = 2
    TotalStu3 = request.POST.get("TotalStu3", "")
    if TotalStu3 != "":
        amount = 3
    TotalStu4 = request.POST.get("TotalStu4", "")
    if TotalStu4 != "":
        amount = 4
    TotalStu5 = request.POST.get("TotalStu5", "")
    if TotalStu5 != "":
        amount = 5
    TotalStu6 = request.POST.get("TotalStu6", "")
    if TotalStu6 != "":
        amount = 6
    TotalStu7 = request.POST.get("TotalStu7", "")
    if TotalStu7 != "":
        amount = 7
    TotalStu8 = request.POST.get("TotalStu8", "")
    if TotalStu8 != "":
        amount = 8
    TotalStu9 = request.POST.get("TotalStu9", "")
    if TotalStu9 != "":
        amount = 9
    TotalStu10 = request.POST.get("TotalStu10", "")
    if TotalStu10 != "":
        amount = 10
    ################################################
    myInput1 = request.POST.get("myInput1", "")
    print("***********************************************************")
    print(myInput1)
    myInput2 = request.POST.get("myInput2", "")
    print("***********************************************************")
    print(myInput2)
    myInput3 = request.POST.get("myInput3", "")
    print(myInput3)
    myInput4 = request.POST.get("myInput4", "")
    print(myInput4)
    myInput5 = request.POST.get("myInput5", "")
    myInput6 = request.POST.get("myInput6", "")
    myInput7 = request.POST.get("myInput7", "")
    myInput8 = request.POST.get("myInput8", "")
    myInput9 = request.POST.get("myInput9", "")
    myInput10 = request.POST.get("myInput10", "")
    ################################################
    ratio1 = request.POST.get("ratio1", "")
    ratio2 = request.POST.get("ratio2", "")
    ratio3 = request.POST.get("ratio3", "")
    ratio4 = request.POST.get("ratio4", "")
    ratio5 = request.POST.get("ratio5", "")
    ratio6 = request.POST.get("ratio6", "")
    ratio7 = request.POST.get("ratio7", "")
    ratio8 = request.POST.get("ratio8", "")
    ratio9 = request.POST.get("ratio9", "")
    ratio10 = request.POST.get("ratio10", "")
    ################################################
    sid = request.POST.get("sid", "")
    radio = request.POST.get("radio", "")

    test_type = request.POST.get("test_type", "")
    instructor_type = request.POST.get("instructor_type", "")
    
    print("************************************************************************************")
    print()
    print(ratio1)
    if amount >= 1:
        instru1_object = Subject.objects.create(examiner=myInput1,Sid=sid,student=TotalStu1,ratio=float(ratio1),T_type=test_type,S_type=instructor_type,\
        Degree=radio,yeasr=academic_year,amount=amount)
    if amount >= 2:
        instru2_object = Subject.objects.create(examiner=myInput2,Sid=sid,student=TotalStu2,ratio=float(ratio2),T_type=test_type,S_type=instructor_type,\
        Degree=radio,yeasr=academic_year,amount=amount)
    if amount >= 3:
        instru3_object = Subject.objects.create(examiner=myInput3,Sid=sid,student=TotalStu3,ratio=float(ratio3),T_type=test_type,S_type=instructor_type,\
        Degree=radio,yeasr=academic_year,amount=amount)
    if amount >= 4:
        instru4_object = Subject.objects.create(examiner=myInput4,Sid=sid,student=TotalStu4,ratio=float(ratio4),T_type=test_type,S_type=instructor_type,\
        Degree=radio,yeasr=academic_year,amount=amount)
    if amount >= 5:
        instru5_object = Subject.objects.create(examiner=myInput5,Sid=sid,student=TotalStu5,ratio=float(ratio5),T_type=test_type,S_type=instructor_type,\
        Degree=radio,yeasr=academic_year,amount=amount)
    if amount >= 6:
        instru6_object = Subject.objects.create(examiner=myInput6,Sid=sid,student=TotalStu6,ratio=float(ratio6),T_type=test_type,S_type=instructor_type,\
        Degree=radio,yeasr=academic_year,amount=amount)
    if amount >= 7:
        instru7_object = Subject.objects.create(examiner=myInput7,Sid=sid,student=TotalStu7,ratio=float(ratio7),T_type=test_type,S_type=instructor_type,\
        Degree=radio,yeasr=academic_year,amount=amount)
    if amount >= 8:
        instru8_object = Subject.objects.create(examiner=myInput8,Sid=sid,student=TotalStu8,ratio=float(ratio8),T_type=test_type,S_type=instructor_type,\
        Degree=radio,yeasr=academic_year,amount=amount)
    if amount >= 9:
        instru9_object = Subject.objects.create(examiner=myInput9,Sid=sid,student=TotalStu9,ratio=float(ratio9),T_type=test_type,S_type=instructor_type,\
        Degree=radio,yeasr=academic_year,amount=amount)
    if amount == 10:
        instru10_object = Subject.objects.create(examiner=myInput10,Sid=sid,student=TotalStu10,ratio=float(ratio10),T_type=test_type,S_type=instructor_type,\
        Degree=radio,yeasr=academic_year,amount=amount)

    thing_list = Subject.objects.order_by().values_list('yeasr',flat=True).distinct()

    return render(request, 'dw.html', {'thing_list':thing_list})

def download(request):

    return render(request,'dw.html')

def SubjectListView(request):
    thing_list = Subject.objects.order_by().values_list('yeasr',flat=True).distinct()
    return render(request, 'dw.html', {'thing_list':thing_list})

def export(request):
    a = request.POST.get("academic_year", "")
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        print('**************************45')
        a = request.POST.get("academic_year", "")
        b = 'attachment; filename='+ a +".xls"
        print(a)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print('**************************51')
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        print('**************************51')

    #return render(request, 'name.html', {'form': form})
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = b

    #searchWord = request.POST.get('year','')
  
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('ค่าตรวจข้อสอบ',cell_overwrite_ok=True)
    

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ชื่อผู้ตรวจข้อสอบ','อัตราส่วนในการตรวจ','จำนวนนักศึกษาที่เข้าสอบ','วิชา','ประเภทข้อสอบ','ประเภทการสอน','ระดับ','ปีการศึกษา','จำนวนเงิน บาท']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = Subject.objects.all().values_list('examiner','ratio','student','Sid','T_type','S_type','Degree','yeasr','amount')


    #num = 0
    #money = {()}
    #for row2 in rows:
    #    if row2[4] == '0' and row2[5] == '0' and row2[6] == '0':
    #        money = money + {(str(float(row2[1])*15 ),)
    #rows = rows + money
    ws.col(0).width = int(13*600)
    ws.col(1).width = int(13*400)
    ws.col(2).width = int(13*450)
    ws.col(4).width = int(13*350)
    ws.col(5).width = int(13*350)
    ws.col(7).width = int(13*200)
    ws.col(8).width = int(13*350)
    for row in rows:
        if(row[7] == a):
            row_num += 1
            for col_num in range(len(row)):
                if col_num == 4 :
                    if row[4] == '0':
                        ws.write(row_num, col_num, 'อัตนัย', font_style)
                    elif row[4] == '1':
                        ws.write(row_num, col_num, 'ปรนัย', font_style)
                    elif row[4] == '2' : 
                        ws.write(row_num, col_num, 'อัตนัย+ปรนัย',font_style)
                    else:
                        ws.write(row_num, col_num, 'สัมภาษณ์ + ปฏิบัติ', font_style)
                elif col_num == 5:
                    if row[5] == '0':
                        ws.write(row_num, col_num, 'เป็นวิชาสอนท่านเดียว', font_style)
                    else:
                        ws.write(row_num, col_num, 'เป็นวิชาสอนหลายท่าน', font_style)
                elif col_num == 6:
                    if row[6] == '0':
                       ws.write(row_num, col_num, 'ป.ตรี', font_style)
                    elif row[6] == '1':
                       ws.write(row_num, col_num, 'ป.โท', font_style) 
                    else:
                        ws.write(row_num, col_num, 'ป.เอก', font_style) 
                elif col_num == 7:
                    ws.write(row_num, col_num, row[col_num], font_style)
                elif col_num == 8:
                    
                    if row[4] == '0' and row[6] == '0': ##4bht/hour          
                            ws.write(row_num,col_num,int(((row[2]*3*4)*float(row[1]))/100),font_style)
                            print(float(row[1]))
                    elif row[4] == '0' and (row[6] == '1' or row[6] == '2'): ##6bht/hour                     
                            ws.write(row_num,col_num,int(((row[2]*3*6)*float(row[1]))/100),font_style)

                    elif row[4] == '1' and row[6] == '0': ##1bht/hour                     
                            ws.write(row_num,col_num,int((row[2]*3*1)*float(row[1])),font_style)

                    elif row[4] == '1' and  (row[6] == '1' or row[6] == '2'): ##1.5bht/hour                 
                            ws.write(row_num,col_num,int(((row[2]*3*1.5)*float(row[1]))/100),font_style)

                    elif row[4] == '2' and row[6] == '0': ##2bht/hour                       
                            ws.write(row_num,col_num,int(((row[2]*3*2)*float(row[1]))/100),font_style)

                    elif row[4] == '2' and  (row[6] == '1' or row[6] == '2'): ##3bht/hour           
                            ws.write(row_num,col_num,int(((row[2]*3*3)*float(row[1]))/100),font_style)

                    elif row[4] == '3' and row[6] == '0': ##2bht/hour               
                            ws.write(row_num,col_num,int(((row[2]*3*2)*float(row[1]))/100),font_style)

                    elif row[4] == '3' and  (row[6] == '1' or row[6] == '2'): ##2bht/hour      
                            ws.write(row_num,col_num,int(((row[2]*3*2)*float(row[1]))/100),font_style)


                else :
                    ws.write(row_num, col_num, row[col_num], font_style)
        
    wb.save(response)

    return response
    template_name='dw.html'
