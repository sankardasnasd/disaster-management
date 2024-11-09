import joblib
import math
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import datetime

# Create your views here.
from myapp.models import *


def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert('Logout successfull');window.location='/';</script>''')


def home(request):
    return render(request, 'Admin/home.html')

def login(request):
    return render(request,'login.html')

def login_post(request):
    name=request.POST['textfield']
    password=request.POST['textfield2']

    user=login_table.objects.filter(username=name,password=password)
    if user.exists():
        a = login_table.objects.get(username=name, password=password)
        request.session['lid']=a.id
        if a.type=='admin':
            return HttpResponse('''<script>alert('Login successfull');window.location='/admin_home';</script>''')
        elif a.type=='coordinator':
            return HttpResponse('''<script>alert('Login successfull');window.location='/coordinator_home';</script>''')
        elif a.type=='ert':
            # return redirect('/emergency_home')
            return HttpResponse('''<script>alert('Login successfull');window.location='/emergency_home';</script>''')
        else:
            return HttpResponse('''<script>alert('Login unsuccessfull');window.location='/';</script>''')
    else:
        return HttpResponse('''<script>alert('Login unsuccessfull');window.location='/';</script>''')




def admin_add_guideline(request):
    a=coordinator_table.objects.all()
    return render(request,'Admin/ADD GUIDELINE.html',{'value':a})

def admin_add_guideline_post(request):
    guidelines=request.FILES['file1']
    name=request.POST['coordinator']
    details=request.POST['text']

    fs = FileSystemStorage()
    fp = fs.save(guidelines.name, guidelines)

    ob1=guideline_table()
    ob1.guidelines=fp
    ob1.name=name
    ob1.details=details
    ob1.COORDINATOR_id=name
    ob1.date=datetime.datetime.now().date()
    ob1.save()
    return HttpResponse('''<script>alert('added');window.location='/admin_view_guideline'</script>''')

def admin_view_guideline(request):
    ob=guideline_table.objects.all()
    return render(request,'Admin/VIEW GUIDELINE.html',{'data':ob} )

def admin_delete_guideline(request,gid):
    guideline=guideline_table.objects.get(id=gid)
    guideline.delete()
    return HttpResponse('''<script>alert('DELETED GUIDELINE');window.location='/admin_view_guideline';</script>''')

def admin_view_notification(request):
    data=notification.objects.all()
    return render(request, 'Admin/admin_view_noti.html',{'data':data})

def admin_add_new_notification(request):
    return render(request,'Admin/ADD NEW NOTI.html')

def admin_add_notification_post(request):
    noti=request.POST['textfield']
    details=request.POST['DETAILS']
    date=datetime.datetime.today()
    ob=notification()
    ob.notification=noti
    ob.date=date
    ob.details=details
    ob.save()
    return HttpResponse('''<script>alert('NOTIFICATION ADDED');window.location='/admin_view_notification';</script>''')



def admin_camp_registration(request):
    camp=camp_table.objects.all()
    return render(request, 'Admin/CAMP MANAGE.html',{'camp':camp})

def camp_search(request):
    query=request.POST['textfield']
    print(query)
    camp=camp_table.objects.filter(name__startswith=query)
    return render(request, 'Admin/CAMP MANAGE.html', {'camp': camp})
def admin_complaint_reply_send(request,rid):
    request.session['rid']=rid
    return render(request,'Admin/COMPLAINT REPLAY SEND.html')

def admin_complaint_reply_send_post(request):
    rep=request.POST['replyText']
    comp=Complaint.objects.filter(id=request.session['rid']).update(reply=rep)
    return HttpResponse('''<script>alert('REPLIED');window.location='/admin_view_complaint';</script>''')

def admin_delete_complaint(request,did):
    data=Complaint.objects.get(id=did)
    data.delete()
    return HttpResponse('''<script>alert('deleted');window.location='/admin_view_complaint';</script>''')



def admin_manage_ert(request):
    kkk=emergency_response_team_table.objects.filter(LOGIN__type='pending')
    return render(request,'Admin/MANAGE ERT.html',{"val":kkk})


def admin_accept_ert(request,eid):
    ert=login_table.objects.filter(id=eid).update(type='ert')
    return HttpResponse('''<script> alert ('Ert added');window.location='/admin_manage_ert';</script>''')

def admin_reject_ert(request,eid):
    ert=login_table.objects.filter(id=eid).update(type='reject')
    return HttpResponse('''<script> alert ('Ert rejected');window.location='/admin_manage_ert';</script>''')


def admin_notification(request):
    return render(request,'Admin/NOTIFICATION.html')

def admin_view_complaint(request):
    comp=Complaint.objects.all()
    return render(request,'Admin/VIEW COMPLAINT.html',{'comp':comp})

def admin_view_coordinator(request):
    aa=coordinator_table.objects.all()
    return render(request,'Admin/VIEW COORDINATOR.html',{"val":aa})

def admin_change_password(request):
    return render(request,'Admin/CHANGE PASSWORD.html')

def admin_home(request):
    a=emergency_response_team_table.objects.all()
    ert=a.count()
    request.session['ert']=ert

    b=camp_table.objects.all()
    camp=b.count()
    request.session['camp']=camp

    c=coordinator_table.objects.all()
    co=c.count()
    request.session['co']=co

    d=medical_support_table.objects.all()
    m=d.count()
    request.session['m']=m


    return render(request,'Admin/adminindex.html',{'ert':ert,'camp':camp,'co':co,'m':m})

def admin_add_camp(request):
    return render(request,'Admin/ADD CAMP.html')

def admin_add_camp_post(request):
    name=request.POST['name']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    land=request.POST['textfield4']
    capacity=request.POST['textfield5']
    details=request.POST['textfield6']
    lattitude=request.POST['textfield7']
    longitude=request.POST['textfield8']
    image=request.FILES['file']

    fs=FileSystemStorage()
    fp=fs.save(image.name,image)

    ob=camp_table()
    ob.name=name
    ob.place=place
    ob.post=post
    ob.landmark=land
    ob.capacity=capacity
    ob.details=details
    ob.lattitude=lattitude
    ob.longitude=longitude
    ob.image=fp

    ob.save()

    return HttpResponse('''<script> alert('CAMP ADDED');window.location='/admin_camp_registration';</script>''')

def admin_edit_camp(request,cid):
    request.session['camp']=cid
    campe=camp_table.objects.get(id=cid)
    return render(request,'Admin/EDIT CAMP.html',{'camp':campe})

def admin_edit_camp_post(request):
    ob=camp_table.objects.get(id=request.session['camp'])

    name=request.POST['name']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    landmark=request.POST['textfield4']
    capacity=request.POST['textfield5']
    details=request.POST['textfield6']
    lattitude=request.POST['textfield7']
    longitude=request.POST['textfield8']

    if 'image' in request.FILES:
        image=request.FILES['file']
        fs=FileSystemStorage()
        fp = fs.save(image.name, image)
        ob.image = fp

    # ob.id=camp_table.objects.get(id=request.session['camp'])
    ob.name=name
    ob.place=place
    ob.post=post
    ob.landmark=landmark
    ob.capacity=capacity
    ob.details=details
    ob.lattitude=lattitude
    ob.longitude=longitude


    ob.save()
    return HttpResponse('''<script> alert('CAMP Edited');window.location='/admin_camp_registration';</script>''')


def admin_delete_camp(request,cid):
    camp=camp_table.objects.get(id=cid)
    camp.delete()
    return HttpResponse('''<script> alert('CAMP Deleted');window.location='/admin_camp_registration';</script>''')



def admin_add_coordinator(request):
    camp = camp_table.objects.all()
    return render(request, 'Admin/COORDINATOR REGISTRATION.html',{'camp':camp})

def admin_add_coordinator_post(request):
    name=request.POST['textfield']
    image=request.FILES['file']
    dob=request.POST['textfield3']
    gender=request.POST['radiobutton']
    address=request.POST['textfield4']
    phone=request.POST['textfield7']
    email=request.POST['textfield8']
    username=request.POST['textfield82']
    password=request.POST['textfield83']
    camp=request.POST['camp']

    fs = FileSystemStorage()
    fp = fs.save(image.name, image)

    login_detail = login_table(
        username=username,
        password=password,
        type='coordinator'
    )
    login_detail.save()

    profile = coordinator_table(
        LOGIN=login_detail,
        CAMP=camp_table.objects.get(id=camp),
        name=name,
        dob=dob,
        phone_number=phone,
        email=email,
        address=address,
        gender=gender,
        image=fp
    )
    profile.save()
    return HttpResponse('''<script> alert('Added');window.location='/admin_view_coordinator';</script>''')

def admin_edit_coordinator(request,cid):
    request.session['coordinator']=cid
    cod=coordinator_table.objects.get(id=cid)
    ob=camp_table.objects.all()
    kk=cod.dob
    print(kk)
    return render(request,'Admin/coordinat_edit.html',{'cod':cod,"camp":ob,"date":kk})


def admin_edit_coordinator_post(request):
    try:
        name = request.POST['textfield']
        image = request.FILES['file']
        dob = request.POST['textfield3']
        gender = request.POST['radiobutton']
        address = request.POST['textfield4']
        phone = request.POST['textfield7']
        email = request.POST['textfield8']
        camp = request.POST['camp']
        fs = FileSystemStorage()
        fp = fs.save(image.name, image)
        profile = coordinator_table.objects.get(id=request.session['coordinator'])
        profile.CAMP=camp_table.objects.get(id=camp)
        profile.name=name
        profile.dob=dob
        profile.phone_number=phone
        profile.email=email
        profile.address=address
        profile.gender=gender
        profile.image=fp
        profile.save()
        return HttpResponse('''<script> alert('EDITED');window.location='/admin_view_coordinator';</script>''')
    except:
        name = request.POST['textfield']
        dob = request.POST['textfield3']
        gender = request.POST['radiobutton']
        address = request.POST['textfield4']
        phone = request.POST['textfield7']
        email = request.POST['textfield8']
        camp = request.POST['camp']
        profile = coordinator_table.objects.get(id=request.session['coordinator'])
        profile.CAMP=camp_table.objects.get(id=camp)
        profile.name=name
        profile.dob=dob
        profile.phone_number=phone
        profile.email=email
        profile.address=address
        profile.gender=gender
        profile.save()
        return HttpResponse('''<script> alert('EDITED');window.location='/admin_view_coordinator';</script>''')


def admin_delete_coordinator(request,lid):
    ob=login_table.objects.get(id=lid)
    ob.delete()
    return HttpResponse('''<script> alert('DELETED');window.location='/admin_view_coordinator';</script>''')

def coordinator_home(request):
    a=volunteer_table.objects.all()
    ac=a.count()
    request.session['ac']=ac

    s=goods_table.objects.all()
    stock=s.count()
    request.session['stock']=stock

    c=medical_support_table.objects.all()
    medical=c.count()
    request.session['medical']=medical
    return render(request,'Coordinator/cindex.html',{'ac':ac,'stock':stock,'medical':medical})

def coordinator_change_password(request):
    return render(request,'Coordinator/CHANGE PASSWORD.html')

def coordinator_change_password_post(request):
    a=request.POST['textfield']
    b=request.POST['textfield2']
    c=request.POST['textfield3']

    user=login_table.objects.filter(id=request.session['lid'],password=a)
    if user:
        if b==c:
            a=login_table.objects.filter(id=request.session['lid'],password=a).update(password=b)
            return HttpResponse('''<script> alert('Password updated');window.location='/coordinator_home';</script>''')

        else:
            return HttpResponse('''<script> alert('Password mismatch');window.location='/coordinator_change_password';</script>''')
    else:
        return HttpResponse('''<script> alert('current password mismatch');window.location='/coordinator_change_password';</script>''')


def cordinator_manage_volunteer(request):
    ob=volunteer_table.objects.all()
    return render(request,'Coordinator/MANAGE  VOLUNTEER.html',{'val':ob})
def coordinator_add_volunteer(request):
    return render(request,'Coordinator/VOLUNTEER REGISTRATION.html')

def coordinator_add_volunteer_post(request):
    name=request.POST['textfield']
    dob=request.POST['textfield3']
    gender=request.POST['radiobutton']
    place=request.POST['textfield4']
    post=request.POST['textfield5']
    pin=request.POST['textfield6']
    phone=request.POST['textfield7']
    email=request.POST['textfield8']
    username=request.POST['textfield82']
    password=request.POST['textfield83']
    image = request.FILES['file']
    fs = FileSystemStorage()
    fp = fs.save(image.name, image)


    bb = login_table()
    bb.username = username
    bb.password = password
    bb.type = 'volunteer'
    bb.save()

    ob = volunteer_table()
    ob.name = name
    ob.dob=dob
    ob.gender=gender
    ob.place = place
    ob.post = post
    ob.pin=pin
    ob.phone=phone
    ob.email=email
    ob.image = fp
    ob.LOGIN=bb
    ob.save()
    return HttpResponse('''<script> alert('VOLUNTEER ADDED');window.location='/cordinator_manage_volunteer';</script>''')


def coor_delete_volu(request,id):
    ob=volunteer_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('DELETED voluneteer');window.location='/cordinator_manage_volunteer';</script>''')

def edit_volunteer(request,id):
    request.session['volunteer']=id
    ob=volunteer_table.objects.get(id=id)
    return render(request,'Coordinator/edit_volunteer.html',{'val':ob})

def edit_volunteer_post(request):
    ob = volunteer_table.objects.get(id= request.session['volunteer'])
    name = request.POST['textfield']
    dob = request.POST['textfield3']
    gender = request.POST['radiobutton']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    phone = request.POST['textfield7']

    if 'image' in request.FILES:
        image=request.FILES['file']
        fs=FileSystemStorage()
        fp = fs.save(image.name, image)
        ob.image = fp

    ob.name=name
    ob.dob=dob
    ob.gender=gender
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.phone=phone
    ob.save()

    return HttpResponse('''<script>alert('edit sucess');window.location='cordinator_manage_volunteer';</script>''')

def coordinator_stock_manage(request):
    a=goods_table.objects.filter(COORDINATOR__LOGIN_id=request.session['lid'])

    return render(request,'Coordinator/STOCK MANAGE.html',{'data':a})


def add_needs(request,id):
    a=goods_table.objects.get(id=id)
    return render(request,'Coordinator/add need.html',{'data':a})

def add_needs_post(request):
    id=request.POST['id']
    quantity=request.POST['quantity']
    date=request.POST['date']

    a=needs_table()
    a.COORDINATOR=coordinator_table.objects.get(LOGIN_id=request.session['lid'])
    a.GOODS=goods_table.objects.get(id=id)
    a.date=date
    a.quantity=quantity
    a.status='need'
    a.save()
    return HttpResponse('''<script>alert('Added sucess');window.location='coordinator_stock_manage';</script>''')


def view_needs(request):
    a=needs_table.objects.filter(COORDINATOR__LOGIN=request.session['lid'])
    return render(request,'Coordinator/VIEW NEEDS.html',{'data':a})


def coordinator_add_stock(request):
    return render(request,'Coordinator/STOCK ADD.html')

def coordinator_add_stock_post(request):
    type = request.POST['type']
    name = request.POST['name']
    details = request.POST['details']
    date = request.POST['date']
    stock = request.POST['stock']
    quantity = request.POST['quantity']
    place = request.POST['place']


    ob = goods_table()
    ob.type = type
    ob.name=name
    ob.details=details
    ob.date = date
    ob.stock = stock
    ob.quantity=quantity
    ob.COORDINATOR=coordinator_table.objects.get(LOGIN_id=request.session['lid'])
    ob.place=place

    ob.save()

    return HttpResponse('''<script> alert('Stock ADDED');window.location='/coordinator_stock_manage';</script>''')

def coordinator_delete_stock(request,id):
    ob = goods_table.objects.get(id=id)
    ob.delete()
    return HttpResponse(
        '''<script>alert('DELETED stock');window.location='/coordinator_stock_manage';</script>''')

def coordinator_edit_stock(request,id):
    request.session['goods'] = id
    ob = goods_table.objects.get(id=id)
    return render(request, 'Coordinator/EDIT STOCK.html', {'val': ob})

def coordinator_edit_stock_post(request):
    id = request.POST['id']
    type = request.POST['textfield']
    name = request.POST['textfield2']
    details = request.POST['textfield3']
    date = request.POST['textfield4']
    stock = request.POST['textfield5']
    quantity = request.POST['textfield6']
    place = request.POST['textfield7']

    ob = goods_table.objects.get(id=id)
    ob.type = type
    ob.name = name
    ob.details = details
    ob.date = date
    ob.stock = stock
    ob.quantity = quantity
    ob.place = place
    ob.COORDINATOR=coordinator_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script> alert('Stock EDITED');window.location='/coordinator_stock_manage';</script>''')





def add_medical_support(request):
    if 'submit' in request.POST:
        details=request.POST['details']
        a=medical_support_table()
        a.COORDINATOR=coordinator_table.objects.get(LOGIN_id=request.session['lid'])
        a.date=datetime.datetime.now().today().date()
        a.status='added'
        a.details=details
        a.save()
        return HttpResponse('''<script> alert('Added');window.location='/view_medi_support';</script>''')
    return render(request,'Coordinator/add medical support.html')

def view_medi_support(request):
    a=medical_support_table.objects.filter(COORDINATOR__LOGIN_id=request.session['lid'])
    return render(request,'Coordinator/view_med.html',{'data':a})


def view_guidellines(request):
    a=guideline_table.objects.filter(COORDINATOR__LOGIN_id=request.session['lid'])
    return render(request,'Coordinator/VIEW GUIDELINES.html',{'data':a})
def delete_med(request,id):
    a=medical_support_table.objects.get(id=id)
    a.delete()
    return HttpResponse('''<script> alert('Deleted');window.location='/view_medi_support';</script>''')


def add_guideline(request):
    if 'submit' in request.POST:
        details=request.POST['details']

        image = request.FILES['guidelines']
        fs = FileSystemStorage()
        fp = fs.save(image.name, image)

        a=guideline_table()
        a.COORDINATOR=coordinator_table.objects.get(LOGIN_id=request.session['lid'])
        a.guidelines=fp
        a.details=details
        a.date=datetime.datetime.now().today().date()
        a.save()
        return HttpResponse('''<script> alert('Added');window.location='/view_guidellines';</script>''')

    return render(request,'Coordinator/add guideline.html')


def delete_guidline(request,id):
    a=guideline_table.objects.get(id=id)
    a.delete()
    return HttpResponse('''<script> alert('Deleted');window.location='/view_guidellines';</script>''')


def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0077

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Difference in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(dlat / 2) * 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) * 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c
    return distance


def emergency_reg(request):
    if 'submit' in request.POST:
        name=request.POST['name']
        place=request.POST['place']
        post=request.POST['post']
        phone=request.POST['phone']
        experience=request.POST['experience']
        username=request.POST['username']
        password=request.POST['password']

        aa=login_table.objects.filter(username=username)
        if aa.exists():
            return HttpResponse('''<script> alert('Username Already Taken');window.location='/emergency_reg';</script>''')

        a=login_table()
        a.username=username
        a.password=password
        a.type='pending'
        a.save()

        b=emergency_response_team_table()
        b.name=name
        b.place=place
        b.post=post
        b.phone=phone
        b.experience=experience
        b.LOGIN=a
        b.save()

        return HttpResponse('''<script> alert('Registered');window.location='/';</script>''')
    return render(request,'emergency/emergency_reg.html')


def emergency_home(request):
    return render(request,'emergency/emergencyindex.html')


def emergency_change_password(request):

    if 'submit' in request.POST:
        old = request.POST['oldPassword']
        new = request.POST['newPassword']
        confirm = request.POST['confirmPassword']

        a = login_table.objects.filter(password=old, id=request.session['lid'])
        if a.exists():
            if new == confirm:

                b = login_table.objects.filter(password=old, id=request.session['lid']).update(password=new)
                return HttpResponse('''<script> alert('Updated');window.location='/';</script>''')

            else:
                return HttpResponse(
                    '''<script> alert('Password mismatches');window.location='/emergency_change_password';</script>''')

        else:
            return HttpResponse(
                '''<script> alert('Password mismatches');window.location='/emergency_change_password';</script>''')
    return render(request,'emergency/change password.html')



def emergency_view_request(request):
    a=request_table.objects.filter(EMERGENCY__LOGIN_id=request.session['lid'])
    return render(request,'emergency/view request.html',{'data':a})


def update_status(request,id):
    a=request_table.objects.get(id=id)
    return render(request,'emergency/update.html',{'data':a})


def update_status_post(request):
    id=request.POST['id']
    update=request.POST['update']
    a=request_table.objects.get(id=id)
    a.status=update
    a.save()
    return HttpResponse(
        '''<script> alert('Update');window.location='/emergency_view_request';</script>''')







def android_login(request):
    username=request.POST['username']
    password=request.POST['password']
    a=login_table.objects.filter(username=username,password=password)
    if a.exists():
        b = login_table.objects.get(username=username, password=password)
        if b.type=='user':
            lid = b.id
            var = user_table.objects.get(LOGIN_id=str(lid))
            name = var.first_name
            return JsonResponse({"status": "ok", "lid":str(lid),'name':name,'type':'user'})
        elif b.type=='volunteer':
            lid=b.id
            var = volunteer_table.objects.get(LOGIN_id=str(lid))
            name = var.name
            print(var)
            print(var.LOGIN.type)
            return JsonResponse({"status": "ok", "lid":str(lid),'name':name,'type':'volunteer'})
        else:
            return JsonResponse({"status": "notok"})
    else:
        return JsonResponse({"status": "notok"})


def user_reg(request):

    password=request.POST['password']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    gender=request.POST['gender']
    age=request.POST['age']
    address=request.POST['address']
    email=request.POST['email']
    phone=request.POST['phone']



    lobj = login_table()
    lobj.username = email
    lobj.password = password
    lobj.type = 'user'
    lobj.save()

    f = user_table()
    f.first_name = first_name
    f.last_name = last_name
    f.gender = gender
    f.age = age
    f.email = email
    f.phone_number = phone
    f.address = address
    f.LOGIN = lobj
    f.save()

    return JsonResponse({"status": "ok"})

def user_change_password(request):

    old = request.POST['old']
    new = request.POST['new']
    confirm = request.POST['confirm']
    lid = request.POST['lid']

    a = login_table.objects.filter(password=old, id=lid)
    if a.exists():
        if new == confirm:

            b = login_table.objects.filter(password=old, id=lid).update(password=new)
            return JsonResponse({"status": "ok"})

        else:
            return JsonResponse({"status": "Not ok"})

    else:
        return JsonResponse({"status": "Not ok"})

def send_complaint(request):
    lid=request.POST['lid']
    complaint=request.POST['complaint']

    a=Complaint()
    a.USER=user_table.objects.get(LOGIN_id=lid)
    a.complaints=complaint
    a.date=datetime.datetime.now().today().date()
    a.reply='pending'
    a.save()
    return JsonResponse({"status": "ok"})


def user_view_reply(request):
    lid=request.POST['lid']
    a=Complaint.objects.filter(USER__LOGIN_id=lid).order_by('-id')
    l=[]
    for i in a:
        l.append({'id': i.id,
                  'complaint': i.complaints,
                  'reply': i.reply,
                  'date': str(i.date) })
    print(l)
    return JsonResponse({"status": "ok",'data':l})


def add_item(request):
    details=request.POST['details']
    lid=request.POST['lid']
    picture=request.POST['picture']
    type=request.POST['type']

    import datetime
    import base64
    date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a=base64.b64decode(picture)
    fh=open("C:\\Users\\GAYATHRI\\Downloads\\crisis\\demo\\media\\missing_item\\"+date+".jpg","wb")
    path="missing_item/"+date+".jpg"
    fh.write(a)
    fh.close()




    f = item_table()
    f.details = details
    f.picture = path
    f.type = type

    f.LOGIN = login_table.objects.get(id=lid)
    f.save()

    return JsonResponse({"status": "ok"})


def view_missing_item(request):
    lid=request.POST['lid']
    l=[]
    a=item_table.objects.filter(LOGIN_id=lid).order_by('-id')
    for i in a:
        l.append({'id':i.id,'type':i.type,'details':i.details,'image':i.picture.url})
        print(i.picture.url,'=========================')

    print(l)
    return JsonResponse({"status": "ok",'data':l})

def delete_item(request):
    id=request.POST['id']
    a=item_table.objects.get(id=id)
    a.delete()
    return JsonResponse({"status": "ok"})



def user_view_nearest_camp(request):
    a=camp_table.objects.all()
    l=[]
    for i in a:
        l.append({'id':i.id,'name':i.name,
                  'place':i.place,
                  'image':i.image.url,
                  'landmark':i.landmark,
                  'capacity':str(i.capacity),

                  })
    print(l)
    return JsonResponse({"status": "ok",'data':l})


def user_view_emergency(request):
    a=emergency_response_team_table.objects.all()
    l=[]

    for i in a:
        l.append({'id':i.id,'name':i.name,
                  'place':i.place,
                  'post':i.post,
                  'phone':str(i.phone),

                  })
    print(l)
    return JsonResponse({"status": "ok",'data':l})


def user_send_request(request):
    lid=request.POST['lid']
    eid=request.POST['eid']
    details=request.POST['details']
    type=request.POST['type']
    a=request_table()
    a.USER=user_table.objects.get(LOGIN_id=lid)
    a.EMERGENCY=emergency_response_team_table.objects.get(id=eid)
    a.details=details
    a.date=datetime.datetime.now().today().date()
    a.type=type
    a.status='Requested'
    a.save()
    return JsonResponse({"status": "ok"})


def user_view_needs(request):
    l=[]
    a=needs_table.objects.all()
    for i in a:
        l.append({'id':i.id,'COORDINATOR':i.COORDINATOR.name,
                  'GOODS':i.GOODS.name,
                  'qty':str(i.quantity),'date':str(i.date)})
    print(l)
    return JsonResponse({"status": "ok",'data':l})


# def user_donate(request):
#     lid=request.POST['lid']
#     nid=request.POST['nid']
#     qty=request.POST['qty']
#
#     a=donate_table()
#     a.NEEDS=needs_table.objects.get(id=nid)
#     a.USER=user_table.objects.get(LOGIN_id=lid)
#     a.date=datetime.datetime.now().today().date()
#     a.quantity=qty
#     a.save()
#     return JsonResponse({"status": "ok"})



from django.http import JsonResponse
from .models import donate_table, needs_table, user_table
import datetime


from django.http import JsonResponse
from .models import donate_table, needs_table, user_table
import datetime

def user_donate(request):
    lid = request.POST['lid']
    nid = request.POST['nid']
    qty = int(request.POST['qty'])

    need_entry = needs_table.objects.get(id=nid)
    current_qty = int(need_entry.quantity)

    if qty > current_qty:
        return JsonResponse({"status": "error", "message": "Out of Stock"})

    new_qty = current_qty - qty

    need_entry.quantity = str(new_qty)
    need_entry.save()

    a = donate_table()
    a.NEEDS = need_entry
    a.USER = user_table.objects.get(LOGIN_id=lid)
    a.date = datetime.datetime.now().date()
    a.quantity = qty
    a.save()

    return JsonResponse({"status": "ok"})


def volounteer_reg(request):


    password = request.POST['password']
    name = request.POST['name']
    photo = request.POST['image']
    dob = request.POST['dob']
    gender = request.POST['gender']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    phone = request.POST['phone']
    email = request.POST['email']
    import datetime
    import base64
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a = base64.b64decode(photo)
    fh = open("C:\\Users\\GAYATHRI\\Downloads\\crisis\\demo\\media\\volunteer\\" + date + ".jpg", "wb")
    path = "volunteer/" + date + ".jpg"
    fh.write(a)
    fh.close()

    lobj = login_table()
    lobj.username = email
    lobj.password = password
    lobj.type = 'volunteer'
    lobj.save()

    f = volunteer_table()
    f.name = name
    f.place = place
    f.pin = pin
    f.phone = phone
    f.email = email
    f.dob = dob
    f.gender = gender
    f.post = post
    f.image = path
    f.LOGIN = lobj
    f.save()

    return JsonResponse({"status": "ok"})



def volounteer_change_password(request):

    old = request.POST['old']
    new = request.POST['new']
    confirm = request.POST['confirm']
    lid = request.POST['lid']

    a = login_table.objects.filter(password=old, id=lid)
    if a.exists():
        if new == confirm:

            b = login_table.objects.filter(password=old, id=lid).update(password=new)
            return JsonResponse({"status": "ok"})

        else:
            return JsonResponse({"status": "Not ok"})

    else:
        return JsonResponse({"status": "Not ok"})


def v_view_needs(request):
    l=[]
    a=needs_table.objects.all()
    for i in a:
        l.append({'id':i.id,'COORDINATOR':i.COORDINATOR.name,
                  'GOODS':i.GOODS.name,
                  'qty':str(i.quantity),'date':str(i.date)})
    print(l)
    return JsonResponse({"status": "ok",'data':l})


def v_add_services(request):
    type=request.POST['type']
    details=request.POST['details']
    a=services_table()
    a.details=details
    a.type=type
    a.save()
    return JsonResponse({"status": "ok"})



def v_view_services(request):
    l=[]
    a=services_table.objects.all()
    for i in a:
        l.append({'id':i.id,'type':i.type,
                  'details':i.details,
                })
    print(l)
    return JsonResponse({"status": "ok",'data':l})


def delete_service(request):
    id=request.POST['id']
    a=services_table.objects.get(id=id)
    a.delete()
    return JsonResponse({"status": "ok"})



def v_view_goods(request):
    a=goods_table.objects.all()
    l=[]
    for i in a:
        l.append({'id':i.id,'COORDINATOR':i.COORDINATOR.name,
                  'type':i.type,'name':i.name,
                  'stock':i.stock,'quantity':i.quantity,'place':i.place,'details':i.details
                  })
    print(l,'===========')
    return JsonResponse({"status": "ok",'data':l})



def update_goods(request):
    gid=request.POST['gid']
    qty=request.POST['qty']
    a=goods_table.objects.get(id=gid)
    o=a.quantity
    c=int(qty)+int(o)
    a.quantity=c
    a.save()
    return JsonResponse({"status": "ok"})


def v_view_medical_support(request):
    a=medical_support_table.objects.all()
    l=[]
    for i in a:
        l.append({'id':i.id,'details':i.details,'date':str(i.date),'COORDINATOR':i.COORDINATOR.name,'status':i.status})
    print(l,'medical==========')
    return JsonResponse({"status": "ok",'data':l})




def update_medical_support(request):
    mid=request.POST['mid']
    status=request.POST['status']
    a=medical_support_table.objects.get(id=mid)
    a.status=status
    a.save()
    return JsonResponse({"status": "ok"})


def v_add_item(request):
    details=request.POST['details']
    lid=request.POST['lid']
    picture=request.POST['picture']
    type=request.POST['type']

    import datetime
    import base64
    date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a=base64.b64decode(picture)
    fh=open("C:\\Users\\GAYATHRI\\Downloads\\crisis\\demo\\media\\missing_item\\"+date+".jpg","wb")
    path="missing_item/"+date+".jpg"
    fh.write(a)
    fh.close()




    f = item_table()
    f.details = details
    f.picture = path
    f.type = type

    f.LOGIN = login_table.objects.get(id=lid)
    f.save()

    return JsonResponse({"status": "ok"})


def v_view_missing_item(request):
    lid=request.POST['lid']
    l=[]
    a=item_table.objects.filter(LOGIN_id=lid)
    for i in a:
        l.append({'id':i.id,'type':i.type,'details':i.details,'image':i.picture.url})
        print(i.picture.url,'=========================')

    print(l)
    return JsonResponse({"status": "ok",'data':l})



import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from .sample import getmaindata
from .river import get_rivers_near_location
API_KEY = '521b3713f9804dc5af807fe5dc27a3c3'

@csrf_exempt  # Disable CSRF for simplicity; remove this in production for security
# def get_weather(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             lat = data.get('latitude')
#             lon = data.get('longitude')
#             distance_str="1000"
#             river_data = get_rivers_near_location(lat, lon)
#             if "error" in river_data:
#                 print(river_data["error"])
#             else:
#                 print(f"Rivers near location ({lat}, {lon}):")
#                 for river in river_data:
#                     # Check if the distance is numeric or a string
#                     if isinstance(river["distance_km"], (float, int)):
#                         # If numeric, format the distance
#                         distance_str = river['distance_km']
#                         break
#                     else:
#                         # If it's a string (e.g., "Distance not available"), display as is
#                         distance_str = river["distance_km"]
#                         break
#
#             elevation, soil_type, slope_angle=getmaindata(float(lat),float(lon))
#             print(elevation, soil_type, slope_angle,distance_str)
#             if lat is None or lon is None:
#                 return JsonResponse({'error': 'Invalid coordinates'}, status=400)
#
#             # Fetch weather data
#             api_url = f'https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key={API_KEY}'
#             response = requests.get(api_url)
#             weather_data = response.json()
#             print(weather_data)
#
#             # if response.status_code == 200:
#             #     weather_data = response.json()
#             #     print(weather_data)
#             #     return JsonResponse(weather_data)
#             # else:
#             #     return JsonResponse({'error': 'Failed to fetch weather data'}, status=response.status_code)
#
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
#     knn = joblib.load(r"C:\Users\GAYATHRI\Downloads\crisis\demo\myapp\knn-model.joblib")
#     # row=[lat,lon,elevation,distance_str,]
#     row = [float(lat), float(lon), elevation, float(distance_str),slope_angle]  # Adjust to include all necessary features
#
#     res = knn.predict([row])
#     print(res, "++++++++++++++++++")
#     if res[0] == 0:
#         return JsonResponse({'status':'ok'}, val="Non-landslide")
#     else:
#         # return render("result.html", val="Landslide")
#         return JsonResponse({'status': 'not ok'}, val="Landslide")
#
#     return JsonResponse({'status': 'not ok'}, val="Landslide")



def get_weather(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            lat = data.get('latitude')
            lon = data.get('longitude')
            distance_str = "1000"

            # Get river data
            river_data = get_rivers_near_location(lat, lon)
            if "error" in river_data:
                print(river_data["error"])
            else:
                print(f"Rivers near location ({lat}, {lon}):")
                for river in river_data:
                    if isinstance(river["distance_km"], (float, int)):
                        distance_str = float(river['distance_km'])
                        break
                    else:
                        distance_str = "Distance not available"
                        break

            # Fetch elevation, soil type, and slope angle data
            elevation, soil_type, slope_angle = getmaindata(float(lat), float(lon))
            print(elevation, soil_type, slope_angle, distance_str)

            if lat is None or lon is None:
                return JsonResponse({'error': 'Invalid coordinates'}, status=400)

            # Fetch weather data
            api_url = f'https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key={API_KEY}'
            response = requests.get(api_url)
            weather_data = response.json()
            print(weather_data)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    # Load the KNN model
    knn = joblib.load(r"C:\Users\GAYATHRI\Downloads\crisis\demo\myapp\knn-model.joblib")

    # Ensure the input data matches the expected dimensions
    try:
        # Adjust the row to have the correct number of features
        st = [
            'Fluvisols',
            'Andosols',
            'Arenosols',
            'Chernozem',
            'Gleysols',
            'Histosols',
            'Kastanozems',
            'Luvisols',
            'Nitisols',
            'Regosols',
            'Vertisols',
            'Solonchaks',
            'Podzols',
            'Alisols',
            'Cambisols',
            'Calcisols',
            'Phaeozems',
            'Acrisols',
            'Plinthosols'
        ]
        row = [float(lat), float(lon), float(elevation), float(distance_str), float(slope_angle),weather_data['data'][0]['precip'],st.index(soil_type),weather_data['data'][0]['rh'],weather_data['data'][0]['rh']]  # Adjust as necessary
        if len(row) != knn.n_features_in_:
            raise ValueError(f"Expected {knn.n_features_in_} features, but got {len(row)}")

        # Make the prediction
        res = knn.predict([row])
        print(res, "++++++++++++++++++")

        if res[0] == 0:
            return JsonResponse({'status': 'ok', 'val': 'Non-landslide','weather_data':weather_data,'st':soil_type,'river':distance_str,'altitude':elevation,'rainfall':weather_data['data'][0]['precip']})
        else:
            return JsonResponse({'status': 'not ok', 'val': 'Landslide','weather_data':weather_data,'st':soil_type,'river':distance_str,'altitude':elevation,'rainfall':weather_data['data'][0]['precip']})

    except ValueError as e:
        print("Error in prediction:", str(e))
        return JsonResponse({'error': 'Prediction failed', 'details': str(e)}, status=500)

    return JsonResponse({'status': 'not ok', 'val': 'Landslide','weather_data':weather_data})


def predict(request):
    v1=request.form['textfield']
    v2=request.form['textfield2']
    v3=request.form['textfield3']
    v4=request.form['textfield4']
    v5=request.form['textfield5']
    v6=request.form['textfield6']
    v7=request.form['textfield7']
    v8=request.form['select']
    v9=request.form['textfield8']
    row=[float(v1),
         float(v2),
         float(v3),
         float(v4),
         float(v5),
         float(v6),
         float(v7),
         float(v8),
         float(v9)]
    knn=joblib.load("knn-model.joblib")
    res=knn.predict([row])
    print(res,"++++++++++++++++++")
    if res[0]==0:
        return  render_template("result.html",val="Non-landslide")
    else:
        return render_template("result.html", val="Landslide")



def map_start(request):
    return render(request,'emergency/map_start.html')

def get_predict(request):
    if request.method == 'POST':
        try:

            lat = float(request.POST['lat'])
            lon = float(request.POST['lon'])
            distance_str = "1000"

            # Get river data
            river_data = get_rivers_near_location(lat, lon)
            if "error" in river_data:
                print(river_data["error"])
            else:
                print(f"Rivers near location ({lat}, {lon}):")
                for river in river_data:
                    if isinstance(river["distance_km"], (float, int)):
                        distance_str = float(river['distance_km'])
                        break
                    else:
                        distance_str = "Distance not available"
                        break

            # Fetch elevation, soil type, and slope angle data
            elevation, soil_type, slope_angle = getmaindata(float(lat), float(lon))
            print(elevation, soil_type, slope_angle, distance_str)

            if lat is None or lon is None:
                return render(request,"emergency/result.html",{"val":"invalid"})
            # Fetch weather data
            api_url = f'https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key={API_KEY}'
            response = requests.get(api_url)
            weather_data = response.json()
            print(weather_data)

        except json.JSONDecodeError as e:
            print(e)
            return render(request, "emergency/result.html", {"val": "invalid"})

            # return JsonResponse({'error': 'Invalid JSON'}, status=400)

    # Load the KNN model
    knn = joblib.load(r"C:\Users\GAYATHRI\Downloads\crisis\demo\myapp\knn-model.joblib")

    # Ensure the input data matches the expected dimensions
    try:
        # Adjust the row to have the correct number of features
        st = [
            'Fluvisols',
            'Andosols',
            'Arenosols',
            'Chernozem',
            'Gleysols',
            'Histosols',
            'Kastanozems',
            'Luvisols',
            'Nitisols',
            'Regosols',
            'Vertisols',
            'Solonchaks',
            'Podzols',
            'Alisols',
            'Cambisols',
            'Calcisols',
            'Phaeozems',
            'Acrisols',
            'Plinthosols'
        ]
        row = [float(lat), float(lon), float(elevation), float(distance_str), float(slope_angle),weather_data['data'][0]['precip'],st.index(soil_type),weather_data['data'][0]['rh'],weather_data['data'][0]['rh']]  # Adjust as necessary
        if len(row) != knn.n_features_in_:
            raise ValueError(f"Expected {knn.n_features_in_} features, but got {len(row)}")

        # Make the prediction
        res = knn.predict([row])
        print(res, "++++++++++++++++++")

        if res[0] == 0:
            return render(request,"emergency/result.html",{'status': 'ok', 'val': 'Non-landslide','weather_data':weather_data,'st':soil_type,'river':distance_str,'altitude':elevation,'rainfall':weather_data['data'][0]['precip'],'city_name':weather_data['data'][0]['city_name']})
        else:
            return HttpResponse({'status': 'not ok', 'val': 'Landslide','weather_data':weather_data,'st':soil_type,'river':distance_str,'altitude':elevation,'rainfall':weather_data['data'][0]['precip'],'city_name':weather_data['data'][0]['city_name']})

    except ValueError as e:
        print("Error in prediction:", str(e))
        return JsonResponse({'error': 'Prediction failed', 'details': str(e)}, status=500)

    return JsonResponse({'status': 'not ok', 'val': 'Landslide','weather_data':weather_data})
