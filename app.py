import streamlit as st
import pandas as pd
from weasyprint import HTML
import io

# 1️⃣ إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="لوحة تحكم التقارير الذكية",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2️⃣ عنوان التطبيق الرئيسي
st.title("📊 لوحة تحكم التقارير الذكية")
st.subheader("تقرير الأداء الدوري للمنصة والمشاريع الرقمية")
st.markdown("---")

# 3️⃣ قسم الإحصائيات السريعة (Cards)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="إجمالي التقارير", value="1,248", delta="+12%")
with col2:
    st.metric(label="المشاريع النشطة", value="42", delta="3 مشاريع جديدة")
with col3:
    st.metric(label="معدل النجاح العام", value="98.4%", delta="+0.4%")

st.markdown("---")

# 4️⃣ رسم بياني للأداء
st.markdown("### 📈 نظرة عامة على البيانات")
chart_data = pd.DataFrame(
    [10, 20, 15, 30, 25, 40],
    columns=['معدل الإنتاجية اليومي']
)
st.line_chart(chart_data)

st.markdown("---")

# 5️⃣ جدول التقارير التفاعلي الذكي (Pandas Dataframe)
st.markdown("### 📋 أحدث التقارير الصادرة والروابط التفاعلية")

data = {
    "معرف التقرير": ["#REP-001", "#REP-002", "#REP-003"],
    "اسم المشروع": ["تطبيق لوحة التحكم المالي", "مستودع الأكواد المركزي", "بوابة الدفع الإلكتروني"],
    "الحالة": ["🟢 مكتمل", "🟢 مكتمل", "🟡 قيد المراجعة"],
    "رابط المعاينة السريعة": [
        "https://my-report-app-amj9.onrender.com/", 
        "https://github.com", 
        "https://render.com"
    ],
    "نص الرابط": ["معاينة التطبيق الحقيقي", "الانتقال إلى GitHub", "فحص خادم Render"]
}

df = pd.DataFrame(data)

st.data_editor(
    df,
    column_config={
        "رابط المعاينة السريعة": st.column_config.LinkColumn(
            "رابط المعاينة (نشط)",
            help="اضغط على الرابط لفتح الصفحة مباشرة",
            display_text=df["نص الرابط"]
        ),
        "نص الرابط": None
    },
    hide_index=True,
    use_container_width=True
)

st.markdown("---")

# 6️⃣ 🖨️ ميزة توليد وطباعة تقرير PDF احترافي يدعم العربية
st.markdown("### 🖨️ خيارات التصدير والطباعة")

# بناء قالب الـ HTML المخصص للـ PDF لضمان مظهر منسق ومحاذة من اليمين إلى اليسار
html_template = """
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <style>
        @page { size: A4; margin: 20mm 15mm; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #333; line-height: 1.6; }
        .header { border-bottom: 3px solid #007bff; padding-bottom: 10px; margin-bottom: 25px; }
        .header h1 { margin: 0 0 5px 0; font-size: 22pt; }
        .header p { color: #6c757d; margin: 0; font-size: 11pt; }
        .section-title { font-size: 14pt; color: #007bff; border-right: 4px solid #007bff; padding-right: 8px; margin-top: 25px; margin-bottom: 15px; }
        .metrics-table { width: 100%; border-collapse: separate; border-spacing: 12px 0; margin-bottom: 25px; }
        .metric-card { background-color: #f8f9fa; border: 1px solid #dee2e6; border-radius: 6px; padding: 15px; text-align: center; width: 33.33%; }
        .metric-label { font-size: 10pt; color: #6c757d; }
        .metric-value { font-size: 18pt; font-weight: bold; color: #212529; }
        .data-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        .data-table th { background-color: #f1f3f5; text-align: right; padding: 10px; font-size: 10pt; border-bottom: 2px solid #dee2e6; }
        .data-table td { padding: 12px 10px; font-size: 10pt; border-bottom: 1px solid #dee2e6; }
        .badge { padding: 3px 8px; border-radius: 4px; font-size: 9pt; }
        .badge-success { background-color: #d4edda; color: #155724; }
        .badge-warning { background-color: #fff3cd; color: #856404; }
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 لوحة تحكم التقارير الذكية</h1>
        <p>تقرير الأداء الدوري للمنصة والمشاريع الرقمية</p>
    </div>
    
    <div class="section-title">📊 الملخص التنفيذي والإحصائيات</div>
    <table class="metrics-table">
        <tr>
            <td class="metric-card">
                <div class="metric-label">إجمالي التقارير</div>
                <div class="metric-value">1,248 (▲ +12%)</div>
            </td>
            <td class="metric-card">
                <div class="metric-label">المشاريع النشطة</div>
                <div class="metric-value">42 (3 جديدة)</div>
            </td>
            <td class="metric-card">
                <div class="metric-label">معدل النجاح العام</div>
                <div class="metric-value">98.4% (▲ +0.4%)</div>
            </td>
        </tr>
    </table>

    <div class="section-title">📋 تفاصيل أحدث التقارير والمشاريع</div>
    <table class="data-table">
        <thead>
            <tr>
                <th>معرف التقرير</th>
                <th>اسم المشروع</th>
                <th>الحالة</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>#REP-001</td>
                <td>تطبيق لوحة التحكم المالي</td>
                <td><span class="badge badge-success">مكتمل</span></td>
            </tr>
            <tr>
                <td>#REP-002</td>
                <td>مستودع الأكواد المركزي</td>
                <td><span class="badge badge-success">مكتمل</span></td>
            </tr>
            <tr>
                <td>#REP-003</td>
                <td>بوابة الدفع الإلكتروني</td>
                <td><span class="badge badge-warning">قيد المراجعة</span></td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""

# دالة لتوليد ملف الـ PDF وحفظه في الذاكرة لتنزيله فوراً
def generate_pdf(html_in):
    pdf_buffer = io.BytesIO()
    HTML(string=html_in).write_pdf(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer

# زر التحميل في Streamlit
st.download_button(
    label="📥 تحميل التقرير النهائي كـ PDF",
    data=generate_pdf(html_template),
    file_name="تقرير_الأداء_النهائي.pdf",
    mime="application/pdf"
)
