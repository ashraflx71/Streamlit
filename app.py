import streamlit as st
import pandas as pd

# إعدادات الصفحة بلمسة أشرف الإبداعية (أسود وذهبي)
st.set_page_config(page_title="أداة أشرف لتحليل SEO", layout="centered")

# تنسيق الواجهة باستخدام CSS داخلي
st.markdown("""
    <style>
    .main { background-color: #000000; }
    h1 { color: #D4AF37; text-align: center; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 10px; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: white; border: 1px solid #D4AF37; }
    </style>
    """, unsafe_allow_password=True)

st.title("🚀 أداة تحليل الكلمات المفتاحية 2026")
st.write("---")

# مدخلات المستخدم
keyword_input = st.text_input("أدخل النص أو الكلمات المفتاحية لتحليلها:")

if st.button("بدء التحليل الذكي"):
    if keyword_input:
        # عملية تحليل بسيطة (يمكن تطويرها لاحقاً بذكاء اصطناعي)
        words = keyword_input.split()
        word_count = pd.Series(words).value_counts().reset_index()
        word_count.columns = ['الكلمة', 'التكرار']
        
        st.success("تم التحليل بنجاح!")
        st.subheader("نتائج الكلمات الأكثر تكراراً:")
        st.dataframe(word_count) # عرض جدول البيانات
    else:
        st.warning("من فضلك أدخل بعض الكلمات أولاً.")

st.sidebar.info("تم التطوير بواسطة منصة أشرف الإبداعية")
