import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="أداة أشرف لتحليل SEO", layout="centered")

# 2. تنسيق الواجهة (تم تصحيح المعلمة هنا)
st.markdown("""
<style>
    .stApp { background-color: #000000; }
    h1 { color: #D4AF37; text-align: center; font-family: 'Arial'; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 10px; width: 100%; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: white; border: 1px solid #D4AF37; }
    label { color: #D4AF37 !important; } /* تلوين نصوص العناوين بالذهبي */
</style>
""", unsafe_allow_html=True)

st.title("🚀 أداة تحليل الكلمات المفتاحية 2026")
st.write("---")

# 3. مدخلات المستخدم
keyword_input = st.text_input("أدخل النص أو الكلمات المفتاحية لتحليلها:")

if st.button("بدء التحليل الذكي"):
    if keyword_input:
        # عملية تحليل بسيطة
        words = keyword_input.split()
        if len(words) > 0:
            word_count = pd.Series(words).value_counts().reset_index()
            word_count.columns = ['الكلمة', 'التكرار']
            
            st.success("تم التحليل بنجاح!")
            st.subheader("نتائج الكلمات الأكثر تكراراً:")
            st.dataframe(word_count, use_container_width=True) # تحسين عرض الجدول
        else:
            st.error("النص المدخل غير صالح.")
    else:
        st.warning("من فضلك أدخل بعض الكلمات أولاً.")

st.sidebar.info("تم التطوير بواسطة منصة أشرف الإبداعية")
