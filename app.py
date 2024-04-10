from flask import Flask, render_template, request


app = Flask(__name__)



# صفحة البداية
@app.route('/')
def index():
    return render_template('index.html')

#صفحة المعالجة
@app.route('/family')
def process():
    # استخراج القيم من الحقول
    return render_template('family.html')
    
    



    

if __name__ == '__main__':
    app.run(debug=True)