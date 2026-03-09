import streamlit as st
import pandas as pd
import plotly.express as px

# إعدادات الواجهة مع مراعاة المساحة
st.set_page_config(page_title="أشرف 2026 - التحليل الذكي", layout="wide")

# عرض البيانات والتحليل في سطر واحد لتوفير المساحة
col_title, col_seo = st.columns([2, 1])

with col_title:
    st.title("🚀 نظام التنبيه والـ SEO الذكي")

with col_seo:
    # محاكاة نصيحة SEO بناءً على البيانات
    st.success("✅ **نصيحة اليوم:** الكلمات المفتاحية لمشروع 'Zacky' تتصدر البحث، ركز على 'تحديثات الأدوات' هذا الأسبوع.")

st.markdown("---")

# الرسوم البيانية - استخدام تقنية "التداخل" لتوفير المساحة
tab1, tab2 = st.tabs(["📊 أداء الزيارات والبيئة", "📧 إعدادات التنبيهات"])

with tab1:
    chart_data = pd.DataFrame({
        'اليوم': ['السبت', 'الأحد', 'الاثنين', 'الثلاثاء', 'الأربعاء', 'الخميس', 'الجمعة'],
        'الزيارات': [450, 700, 1200, 900, 1100, 1500, 1300],
        'SEO_Score': [70, 75, 85, 80, 88, 92, 90]
    })
    
    # رسم بياني مدمج يوفر المساحة
    fig = px.line(chart_data, x='اليوم', y=['الزيارات', 'SEO_Score'], 
                  title="تطور الزيارات مقابل جودة الـ SEO",
                  template="plotly_dark", markers=True)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.write("⚙️ **إعدادات سريعة:**")
    email = st.text_input("بريدك الإلكتروني المستهدف:", value="ashraf@example.com")
    if st.button("تفعيل نظام التنبيهات الذكي"):
        st.write(f"سيتم إرسال تقرير SEO مختصر إلى: {email}")


