from flask import Flask, request, Response

app = Flask(__name__)

# قائمة بالأسئلة العشرة الافتراضية للتحكم بالعدد في الخلفية
TOTAL_QUESTIONS = 10

HTML_INTERFACE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>نظام التقارير الموثقة للويب</title>
    <style>
        body { font-family: Tahoma, sans-serif; background-color: #f5f6fa; padding: 20px; direction: rtl; }
        .container { max-width: 700px; margin: 0 auto; background: white; padding: 25px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
        h2 { text-align: center; color: #2c3e50; margin-bottom: 5px; }
        p.subtitle { text-align: center; color: #7f8c8d; margin-bottom: 25px; font-size: 0.9em; }
        .form-group { margin-bottom: 15px; }
        label { font-weight: bold; color: #34495e; display: block; margin-bottom: 5px; }
        input[type="text"] { width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #bdc3c7; border-radius: 4px; }
        .box { border: 1px solid #dcdde1; padding: 15px; margin-bottom: 20px; border-radius: 6px; background: #fafafa; border-right: 5px solid #2980b9; }
        button { width: 100%; background: #27ae60; color: white; padding: 12px; border: none; border-radius: 6px; font-size: 16px; font-weight: bold; cursor: pointer; margin-top: 10px; }
        button:hover { background: #219653; }
    </style>
</head>
<body>
<div class="container">
    <h2>📋 لوحة تحكم تقارير العمل (10 أسئلة)</h2>
    <p class="subtitle">يمكنك تعديل نصوص الأسئلة أو تركها كما هي، ثم كتابة الإجابات والروابط</p>
    
    <form action="/generate" method="POST">
        <div class="form-group">
            <label>📝 العنوان العام للتقرير:</label>
            <input type="text" name="report_title" value="تقرير مراجعة العمل الدوري والالتزام التقني">
        </div>
        
        <div class="box">
            <div class="form-group">
                <label style="color: #2980b9;">السؤال 1:</label>
                <input type="text" name="question_0" value="هل تم التأكد من سلامة واكتمال النسخ الاحتياطي الدوري للبيانات؟">
            </div>
            <div class="form-group"><label>الإجابة:</label><input type="text" name="answer_0" placeholder="اكتب الإجابة هنا..."></div>
            <div class="form-group"><label>رابط الشاهد من السحابة أو النظام:</label><input type="text" name="link_0" placeholder="https://..." style="direction: ltr;"></div>
        </div>

        <div class="box">
            <div class="form-group">
                <label style="color: #2980b9;">السؤال 2:</label>
                <input type="text" name="question_1" value="هل جميع الأنظمة والملحقات محدثة بآخر رقع وتحديثات الأمان؟">
            </div>
            <div class="form-group"><label>الإجابة:</label><input type="text" name="answer_1" placeholder="اكتب الإجابة هنا..."></div>
            <div class="form-group"><label>رابط الشاهد:</label><input type="text" name="link_1" placeholder="https://..." style="direction: ltr;"></div>
        </div>

        <div class="box">
            <div class="form-group">
                <label style="color: #2980b9;">السؤال 3:</label>
                <input type="text" name="question_2" value="هل تم فحص سجلات الأخطاء والتحذيرات اليومية (Logs) وإغلاق التنبيهات؟">
            </div>
            <div class="form-group"><label>الإجابة:</label><input type="text" name="answer_2" placeholder="اكتب الإجابة هنا..."></div>
            <div class="form-group"><label>رابط الشاهد:</label><input type="text" name="link_2" placeholder="https://..." style="direction: ltr;"></div>
        </div>

        <div class="box">
            <div class="form-group">
                <label style="color: #2980b9;">السؤال 4:</label>
                <input type="text" name="question_3" value="هل جدار الحماية (Firewall) وأنظمة كشف الاختراق تعمل بكفاءة وبدون مشاكل؟">
            </div>
            <div class="form-group"><label>الإجابة:</label><input type="text" name="answer_3" placeholder="اكتب الإجابة هنا..."></div>
            <div class="form-group"><label>رابط الشاهد:</label><input type="text" name="link_3" placeholder="https://..." style="direction: ltr;"></div>
        </div>

        <div class="box">
            <div class="form-group">
                <label style="color: #2980b9;">السؤال 5:</label>
                <input type="text" name="question_4" value="هل تم التحقق من استقرار اتصال شبكة الإنترنت الداخلية والخارجية؟">
            </div>
            <div class="form-group"><label>الإجابة:</label><input type="text" name="answer_4" placeholder="اكتب الإجابة هنا..."></div>
            <div class="form-group"><label>رابط الشاهد:</label><input type="text" name="link_4" placeholder="https://..." style="direction: ltr;"></div>
        </div>

        <div class="box">
            <div class="form-group">
                <label style="color: #2980b9;">السؤال 6:</label>
                <input type="text" name="question_5" value="هل تم تفعيل ومراجعة صلاحيات وصول المستخدمين والموظفين الجدد؟">
            </div>
            <div class="form-group"><label>الإجابة:</label><input type="text" name="answer_5" placeholder="اكتب الإجابة هنا..."></div>
            <div class="form-group"><label>رابط الشاهد:</label><input type="text" name="link_5" placeholder="https://..." style="direction: ltr;"></div>
        </div>

        <div class="box">
            <div class="form-group">
                <label style="color: #2980b9;">السؤال 7:</label>
                <input type="text" name="question_6" value="هل سعة التخزين على الخوادم الرئيسية (Disk Space) في الحدود الآمنة؟">
            </div>
            <div class="form-group"><label>الإجابة:</label><input type="text" name="answer_6" placeholder="اكتب الإجابة هنا..."></div>
            <div class="form-group"><label>رابط الشاهد:</label><input type="text" name="link_6" placeholder="https://..." style="direction: ltr;"></div>
        </div>

        <div class="box">
            <div class="form-group">
                <label style="color: #2980b9;">السؤال 8:</label>
                <input type="text" name="question_7" value="هل تم عمل اختبار دوري سريع لخطة التعافي من الكوارث (DRP)؟">
            </div>
            <div class="form-group"><label>الإجابة:</label><input type="text" name="answer_7" placeholder="اكتب الإجابة هنا..."></div>
            <div class="form-group"><label>رابط الشاهد:</label><input type="text" name="link_7" placeholder="https://..." style="direction: ltr;"></div>
        </div>

        <div class="box">
            <div class="form-group">
                <label style="color: #2980b9;">السؤال 9:</label>
                <input type="text" name="question_8" value="هل شهادات التشفير والأمان للمواقع (SSL Certificates) سارية الصلاحية؟">
            </div>
            <div class="form-group"><label>الإجابة:</label><input type="text" name="answer_8" placeholder="اكتب الإجابة هنا..."></div>
            <div class="form-group"><label>رابط الشاهد:</label><input type="text" name="link_8" placeholder="https://..." style="direction: ltr;"></div>
        </div>

        <div class="box">
            <div class="form-group">
                <label style="color: #2980b9;">السؤال 10:</label>
                <input type="text" name="question_9" value="هل تم رصد ومتابعة تذاكر الدعم الفني المعلقة وحل المشكلات الحرجة؟">
            </div>
            <div class="form-group"><label>الإجابة:</label><input type="text" name="answer_9" placeholder="اكتب الإجابة هنا..."></div>
            <div class="form-group"><label>رابط الشاهد:</label><input type="text" name="link_9" placeholder="https://..." style="direction: ltr;"></div>
        </div>

        <button type="submit">📄 استخراج وتحميل التقرير الكامل</button>
    </form>
</div>
</body>
</html>
'''

@app.route('/')
def home():
    return HTML_INTERFACE

@app.route('/generate', methods=['POST'])
def generate():
    user_title = request.form.get('report_title', 'تقرير مراجعة العمل')
    html_body = ""
    
    for i in range(TOTAL_QUESTIONS):
        q_text = request.form.get(f'question_{i}', '').strip()
        a_text = request.form.get(f'answer_{i}', '').strip()
        l_text = request.form.get(f'link_{i}', '').strip()

        if not q_text: q_text = f"السؤال رقم {i+1}"
        if not a_text: a_text = "لم يتم تقديم إجابة."

        html_body += f'''
        <div style="background: #fff; border: 1px solid #e1e8ed; border-right: 5px solid #2980b9; border-radius: 5px; padding: 15px; margin-bottom: 20px;">
            <div style="font-size: 1.1em; font-weight: bold; color: #2c3e50; margin-bottom: 10px;">🔍 {q_text}</div>
            <div style="background: #f8f9fa; padding: 12px; border-radius: 4px; border: 1px solid #f1f2f6; color: #333; line-height: 1.6;">{a_text}</div>
        '''
        if l_text:
            if not l_text.startswith(('http://', 'https://')): l_text = 'https://' + l_text
            html_body += f'<div><a href="{l_text}" target="_blank" style="display:inline-block; background:#2ecc71; color:white; text-decoration:none; padding:6px 12px; border-radius:4px; font-size:0.85em; margin-top:8px; font-weight:bold;">🔗 رابط الشاهد والمستند</a></div>'
        else:
            html_body += '<div style="font-size:0.85em; color:#95a5a6; font-style:italic; margin-top:8px;">⚠️ لا يوجد شاهد مرفق.</div>'
        html_body += '</div>'

    final_html = f'''<!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>{user_title}</title>
        <style>
            body {{ font-family: Tahoma, sans-serif; background: #f5f6fa; padding: 40px; }}
            .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
            h1 {{ text-align: center; color: #2c3e50; margin-bottom: 30px; border-bottom: 2px solid #2980b9; padding-bottom: 15px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 {user_title}</h1>
            {html_body}
        </div>
    </body>
    </html>'''

    return Response(
        final_html,
        mimetype="text/html",
        headers={"Content-disposition": "attachment; filename=final_report.html"}
    )

if __name__ == '__main__':
    app.run(debug=True)