import streamlit as st
import pandas as pd

# 1️⃣ إعدادات الصفحة الأساسية (العنوان والمظهر)
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

st.markdown("### 📈 نظرة عامة على البيانات")

# 4️⃣ رسم بياني تجريبي للأداء
chart_data = pd.DataFrame(
    [10, 20, 15, 30, 25, 40],
    columns=['معدل الإنتاجية اليومي']
)
st.line_chart(chart_data)

st.markdown("### 📋 أحدث التقارير الصادرة والروابط التفاعلية")

# 5️⃣ جدول التقارير التفاعلي (باستخدام روابط حقيقية قابلة للنقر)
st.markdown(
    """
    <table style="width:100%; border-collapse: collapse; text-align: right; font-family: sans-serif;">
        <thead>
            <tr style="background-color: #f8f9fa; border-bottom: 2px solid #dee2e6;">
                <th style="padding: 12px;">معرف التقرير</th>
                <th style="padding: 12px;">اسم المشروع</th>
                <th style="padding: 12px;">الحالة</th>
                <th style="padding: 12px;">رابط المعاينة السريعة (نشط)</th>
            </tr>
        </thead>
        <tbody>
            <tr style="border-bottom: 1px solid #dee2e6;">
                <td style="padding: 12px;">#REP-001</td>
                <td>تطبيق لوحة التحكم المالي</td>
                <td style="padding: 12px;"><span style="background-color: #d4edda; color: #155724; padding: 4px 8px; border-radius: 4px; font-size: 12px;">مكتمل</span></td>
                <td style="padding: 12px;"><a href="https://my-report-app-amj9.onrender.com/" target="_blank" style="color: #007bff; text-decoration: none; font-weight: bold;">معاينة التطبيق الحقيقي</a></td>
            </tr>
            <tr style="border-bottom: 1px solid #dee2e6;">
                <td style="padding: 12px;">#REP-002</td>
                <td>مستودع الأكواد المركزي</td>
                <td style="padding: 12px;"><span style="background-color: #d4edda; color: #155724; padding: 4px 8px; border-radius: 4px; font-size: 12px;">مكتمل</span></td>
                <td style="padding: 12px;"><a href="https://github.com" target="_blank" style="color: #007bff; text-decoration: none; font-weight: bold;">الانتقال إلى GitHub</a></td>
            </tr>
            <tr style="border-bottom: 1px solid #dee2e6;">
                <td style="padding: 12px;">#REP-003</td>
                <td>بوابة الدفع الإلكتروني</td>
                <td style="padding: 12px;"><span style="background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 12px;">قيد المراجعة</span></td>
                <td style="padding: 12px;"><a href="https://render.com" target="_blank" style="color: #007bff; text-decoration: none; font-weight: bold;">فحص خادم Render</a></td>
            </tr>
        </tbody>
    </table>
    """,
    unsafe_allow_html=True
)
# =========================================================
# 6️⃣ الجزء الخاص بميزة استخراج التقرير كـ PDF تفاعلي لويندوز
# =========================================================
st.markdown("---")

# زر الاستخراج الأزرق
st.markdown(
    """
    <div style="text-align: center; margin-top: 30px; margin-bottom: 30px;">
        <button onclick="window.print()" style="
            background-color: #2b6cb0;
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 300px;
        ">
            📊 استخراج التقرير (PDF)
        </button>
    </div>
    """,
    unsafe_allow_html=True
)

# كود التنسيق الذكي لإخفاء القوائم الجانبية وأدوات التحكم أثناء الطباعة
st.markdown(
    """
    <style>
    @media print {
        /* إخفاء أدوات Streamlit والقائمة الجانبية تماماً لتنظيف الملف */
        [data-testid="stSidebar"], 
        header, 
        footer, 
        .stDeployButton, 
        [data-testid="stToolbar"],
        button {
            display: none !important;
        }
        /* تمديد التقرير ليأخذ المساحة الكاملة لورقة الطباعة */
        .main .block-container {
            max-width: 100% !important;
            padding: 10mm !important;
            margin: 0 !important;
        }
        /* جعل الخلفية بيضاء ناصعة والخطوط واضحة */
        body, .main {
            background-color: white !important;
            color: black !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)
