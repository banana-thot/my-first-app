import streamlit as st
st.markdown("# :violet[คำนวณค่าดัชนีมวลกาย BMI🩺]")
st.write("กรอกข้อมูล น้ำหนัก ส่วนสูง ของคุณ เพื่อตรวจสุขภาพเบื่องต้น")
w = st.number_input("กรอกน้ำหนัก (กิโลกรัม):", min_value=0.0 , value=0.0)
h_cm = st.number_input("กรอกส่วนสูง (เซนติเมตร):", min_value=0.0 , value=0.0)

if st.button("คำนวณค่า BMI"):
  h_m = h_cm / 100
  bmi = w / (h_m **2)
  st.write("---")
  st.header(f"ค่าBMI ของคุณ: **{bmi:.2f}**")
  if bmi < 18.5:
    st.warning("🍎 คุณมีน้ำหนักอยู่ในเกณฑ์ ผอม")
  elif 18.5 <= bmi < 23:
    st.success("🎉 คุณมีน้ำหนักอยู่ในเกณฑ์ ปกติ")
  elif 23 <= bmi < 25:
    st.info("⚠️ คุณมีน้ำหนักอยู่ในเกณฑ์ ท้วม")
  else:
    st.error("🚨 คุณมีน้ำหนักอยู่ในเกณฑ์ อ้วน ควรระวังเรื่องสุขภาพ 🚨")




st.divider()
st.write("นางสาว ชนิดาภา สุขจันทร์ เลขที่39 ม.4/5")
