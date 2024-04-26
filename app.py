from flask import Flask, render_template, request, redirect, url_for
from dateutil.relativedelta import relativedelta
import datetime
import webbrowser



malecount = []
femalecount = []
healthmessagecount = []
coronamessagecount = []
diseasemessagecount = []
nummaleover18=[]
nummalemin6month =[]
nummalebet612month=[]
nummalebet1324month=[]
nummalebet2559month=[]
nummalebet518year=[]
   
numfmaleover18=[]
numfmalemin6month =[]
numfmalebet612month=[]
numfmalebet1324month=[]
numfmalebet2559month=[]
numfmalebet518year=[]

sa=[]
na=[]
aa=[]
########################################################متحولات الرسائل
m1=[]
m2=[]
m3=[]
m4=[]
m5=[]
m6=[]
m7=[]
m8=[]
m9=[]

##############################################################متحول الاعاقة
ea=[]

#############################################متحولات مواك
muacmale=[]
muacfmale=[]
################################حامل /مرضع

ha=[]
mo=[]

app = Flask(__name__)
@app.route('/')
def base():
    return render_template('base.html')


# صفحة تسجيل الدخول
@app.route('/family', methods=['GET', 'POST'])
def family():
    
     
         
    if request.method == 'POST':
        
        a1 = request.form['a2']
        a2=request.form['year']
        a3=request.form['month']
        a4=request.form['day']
        print(a1)
        
            
        ###############حساب الذكور بجميع الفئات
        if a1 == 'ذكر':
                    
                
            if a3=='' and a4=='':
                        
                
                malecount.append('1')
                nummaleover18 .append('1')
                
            else:
                birthday=str(str(a2)+"-"+str(a3)+"-"+str(a4))

                birthday1=datetime.datetime.strptime(birthday,"%Y-%m-%d").date()
                current=datetime.datetime.now()
                info=relativedelta(current,birthday1)
                num_month=info.years*12+info.months
                num_day=info.days
                    
                if num_month<5 or (num_month==5 and num_day==0):
                    malecount.append('1')
                    nummalemin6month.append('1')
                elif num_month<12 or (num_month==12 and num_day==0):
                    malecount.append('1')
                    nummalebet612month.append('1')
                elif num_month<24 or (num_month==24 and num_day==0):
                    malecount.append('1')
                    nummalebet1324month.append('1')
                elif num_month<59 or (num_month==59 and num_day==0):
                    malecount.append('1')
                    nummalebet2559month.append('1')
                elif num_month<216 or (num_month==216 and num_day==0):
                    malecount.append('1')
                    nummalebet518year.append('1')
                else :
                    malecount.append('1')
                    nummaleover18.append('1')
        
        
        ##########################عدد الاناث في كل فئة  
        elif a1== 'أنثى':
            if a3=='' and a4=='':
                femalecount.append('1')
                numfmaleover18 .append('1')
                
            elif  a3!='' and a4!='':
                birthday=str(str(a2)+"-"+str(a3)+"-"+str(a4))

                birthday1=datetime.datetime.strptime(birthday,"%Y-%m-%d").date()
                current=datetime.datetime.now()
                info=relativedelta(current,birthday1)
                num_month=info.years*12+info.months
                num_day=info.days
                    
                if num_month<5 or (num_month==5 and num_day==0):
                    femalecount.append('1')
                    numfmalemin6month.append('1')
                elif num_month<12 or (num_month==12 and num_day==0):
                    femalecount.append('1')
                    numfmalebet612month.append('1')
                elif num_month<24 or (num_month==24 and num_day==0):
                    femalecount.append('1')
                    numfmalebet1324month.append('1')
                elif num_month<59 or (num_month==59 and num_day==0):
                    femalecount.append('1')
                    numfmalebet2559month.append('1')
                elif num_month<216 or (num_month==216 and num_day==0):
                    femalecount.append('1')
                    numfmalebet518year.append('1')
                else :
                    femalecount.append('1')
                    numfmaleover18.append('1')
        
        
        
    return render_template('family.html')
        # إعادة التوجيه إلى صفحة عرض المعلومات
        

  
  
  
  
  
@app.route('/messages',methods=['GET', 'POST'])  
def messages():
    if request.method == 'POST':
        
        ms=request.form.getlist('messages')
        for i in ms:
            if i == 'تغذية الرضع':
                m1.append('1')
                   
            elif i == 'تغذية الاطفال الصفار':
                m2.append('1')
                    
            elif i == 'الغذاء الصحي':
                m3.append('1')
                        
            elif i == 'تغذية الحامل والمرضع':
                m4.append('1')
                        
            elif i == 'الصحة الانجابية والحماية':
                m5.append('1')
                
            elif i == 'الامراض المنتقلة':
                m6.append('1')
                
            elif i == 'كورونا':
                m7.append('1')
                        
            elif i == 'رعاية المعاقين':
                m8.append('1')
            elif i == 'الامراض غير المنتقله':
                m9.append('1')
        
        
    return render_template('messages.html')




@app.route('/child',methods=['GET', 'POST'])  
def child():
    if request.method == 'POST':
        
        b1=request.form['ch1']
        if b1=='ذكر':
            muacmale.append('1')
        elif b1=='أنثى':
            muacfmale.append('1')
        
        
    return render_template('childmuac.html')






@app.route('/eaa',methods=['GET', 'POST'])  
def eaa():
    if request.method == 'POST':
        
        ak1=request.form['ak']
        if ak1=='نعم':
            ea.append('1')
        
        
    return render_template('eaa.html')


@app.route('/state',methods=['GET', 'POST'])  
def state():
    if request.method == 'POST':
        
        st=request.form['st1']
        if st=='سكان أصليين':
            sa.append('1')
        
        elif st=='عائدين':
            aa.append('1')
        elif st=='نازحين':
            na.append('1')
    return render_template('state.html')





@app.route('/hamo',methods=['GET', 'POST'])  
def hamo():
    if request.method == 'POST':
        
        p11=request.form['p1']
        if p11=='حامل':
            ha.append('1')
        elif p11=='مرضع':
            mo.append('1')
        
        
    return render_template('hamo.html')



# صفحة عرض المعلومات




@app.route('/display')
def display():
    # username = request.args.get('username')
    # password = request.args.get('password')
    # هنا يمكنك استخدام المعلومات المستلمة لعرضها في صفحة HTML
    
    
    return render_template('display.html',sar=len(sa),nar=len(na),aar=len(aa),malecountr=len(malecount),nummalemin6monthr=len(nummalemin6month),nummalebet612monthr=len(nummalebet612month),nummalebet1324monthr=len(nummalebet1324month),nummalebet2559monthr=len(nummalebet2559month),
    nummalebet518yearr=len(nummalebet518year),nummaleover18r=len(nummaleover18),fmalecountr=len(femalecount),
    numfmalemin6monthr=len(numfmalemin6month),numfmalebet612monthr=len(numfmalebet612month),
    numfmalebet1324monthr=len(numfmalebet1324month),numfmalebet2559monthr=len(numfmalebet2559month),
    numfmalebet518yearr=len(numfmalebet518year),numfmaleover18r=len(numfmaleover18),m1r=len(m1), m2r=len(m2),
    m3r=len(m3),m4r=len(m4), m5r=len(m5), m6r=len(m6), m7r=len(m7),m8r=len(m8), m9r=len(m9),ear=len(ea), har=len(ha),mor=len(mo))

if __name__ == '__main__':
    app.run()
