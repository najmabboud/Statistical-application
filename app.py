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
ms1=[]
ms2=[]
ms3=[]
ms4=[]
ms5=[]
ms6=[]
ms7=[]
ms8=[]
ms9=[]

##############################################################متحول الاعاقة
eak=[]

#############################################متحولات مواك
muacmale=[]
muacfmale=[]
################################حامل /مرضع

haa=[]
moo=[]





def age(a1,a2,a3,a4):
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
    









app = Flask(__name__)
@app.route('/')
def base():
    return render_template('base.html')



  
  
  
  







@app.route('/start',methods=['GET', 'POST'])  
def state():
    if request.method == 'POST':
        
        st=request.form['state']
        if st=='سكان أصليين':
            sa.append('1')
        
        elif st=='عائدين':
            aa.append('1')
        elif st=='نازحين':
            na.append('1')
            
        mal1=request.form['k1']
        y1=request.form['year1']
        m1=request.form['month1']
        d1=request.form['day1']
        age(mal1,y1,m1,d1)
        
        mal2=request.form['k2']
        y2=request.form['year2']
        m2=request.form['month2']
        d2=request.form['day2']
        age(mal2,y2,m2,d2)
        
        mal3=request.form['k3']
        y3=request.form['year3']
        m3=request.form['month3']
        d3=request.form['day3']
        age(mal3,y3,m3,d3)
        
        mal4=request.form['k4']
        y4=request.form['year4']
        m4=request.form['month4']
        d4=request.form['day4']
        age(mal4,y4,m4,d4)
        
        numha =int(request.form['ha'])
        nummo=int(request.form['mo'])
        haa.append(numha)
        moo.append(nummo)
        
        numea=int(request.form['ea'])
        eak.append(numea)
        
        nummma=int(request.form['mma'])
        nummfam=int(request.form['mfam'])
        
        muacmale.append(nummma)
        muacfmale.append(nummfam)
        
        ms=request.form.getlist('messages')
        for i in ms:
            if i == 'تغذية الرضع':
                ms1.append("1")
                   
            elif i == 'تغذية الاطفال الصفار':
                ms2.append('1')
                    
            elif i == 'الغذاء الصحي':
                ms3.append('1')
                        
            elif i == 'تغذية الحامل والمرضع':
                ms4.append('1')
                        
            elif i == ' الصحة الانجابية والحماية':
                ms5.append('1')
                
            elif i == ' الامراض المنتقلة':
                ms6.append('1')
                
            elif i == 'كورونا':
                ms7.append('1')
                        
            elif i == 'رعاية المعاقين':
                ms8.append('1')
            elif i == ' الامراض غير المنتقلة':
                ms9.append('1')
        
        
        
        
            
        
    return render_template('start.html')








@app.route('/display')
def display():
    
    # username = request.args.get('username')
    # password = request.args.get('password')
    # هنا يمكنك استخدام المعلومات المستلمة لعرضها في صفحة HTML
    
    
    return render_template('display.html',sar=len(sa),nar=len(na),aar=len(aa),malecountr=len(malecount),nummalemin6monthr=len(nummalemin6month),nummalebet612monthr=len(nummalebet612month),nummalebet1324monthr=len(nummalebet1324month),nummalebet2559monthr=len(nummalebet2559month),
    nummalebet518yearr=len(nummalebet518year),nummaleover18r=len(nummaleover18),fmalecountr=len(femalecount),
    numfmalemin6monthr=len(numfmalemin6month),numfmalebet612monthr=len(numfmalebet612month),
    numfmalebet1324monthr=len(numfmalebet1324month),numfmalebet2559monthr=len(numfmalebet2559month),
    numfmalebet518yearr=len(numfmalebet518year),numfmaleover18r=len(numfmaleover18),m1r=len(ms1), m2r=len(ms2),
    m3r=len(ms3),m4r=len(ms4), m5r=len(ms5), m6r=len(ms6), m7r=len(ms7),m8r=len(ms8), m9r=len(ms9),ear=sum(eak), har=sum(haa),mor=sum(moo),muacm=sum(muacmale),muacf=sum(muacfmale))

if __name__ == '__main__':
    app.run()