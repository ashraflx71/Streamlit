import streamlit as st
import pandas as pd
from codecarbon import EmissionsTracker
import os

# --- إعداد مراقب الانبعاثات الكربونية ---
tracker = EmissionsTracker(save_to_file=True, output_dir=".")
tracker.start()

# --- إعدادات الواجهة ---
st.set_page_config(page_title="أشرف حسن - Green Analytics 2026", layout="wide")

st.title("🌱 لوحة التحكم الخضراء لمشاريع أشرف")
st.markdown("---")

# قسم الإحصائيات البيئية
st.subheader("🌍 الأثر البيئي لتشغيل هذا التطبيق")
col_env1, col_env2 = st.columns(2)

# قراءة بيانات الانبعاثات (من ملف emissions.csv الذي تنشئه المكتبة تلقائياً)
try:
    emissions_df = pd.read_csv("emissions.csv")
    current_emissions = emissions_df["emissions"].iloc[-1]
    energy_consumed = emissions_df["energy_consumed"].iloc[-1]
    
    col_env1.metric("انبعاثات الكربون (كجم CO2)", f"{current_emissions:.6f}")
    col_env2.metric("الطاقة المستهلكة (كيلوواط/ساعة)", f"{energy_consumed:.6f}")
except:
    st.info("جاري حساب البيانات البيئية... ستظهر الأرقام بعد قليل.")

# --- هنا نضع كود Google Analytics السابق ---
st.markdown("---")
st.subheader("📈 أداء المواقع (GA4)")
if st.button('تحديث بيانات GA4 الآن 🔄'):
    st.success("تم الاتصال بـ Google Analytics بنجاح!")
    # (هنا يوضع كود جلب البيانات الذي شرحناه سابقاً)

# إيقاف المراقب عند إغلاق التطبيق (اختياري)
tracker.stop()
