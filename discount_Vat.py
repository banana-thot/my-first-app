import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
p = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
per = st.number_input("กรอกส่วนลด (%):", min_value=0.0 , max_value=100.0 , value=0.0)
per = per/100
all_per = per * p
st.write(f"• ส่วนลด ({per}%): -**{all_per:.2f}** บาท")
pr = p - all_per
st.write(f"• ราคาหลังหักส่วนลด: **{pr:.2f}** บาท")
vat = pr * 0.07
st.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): +**{vat:.2f}** บาท")
all_p = vat + pr
st.header(f"• ราคาสุทธิที่ต้องจ่าย: {all_p:.2f} บาท")
st.divider()
st.write("นางสาวชนิดาภา สุขจันทร์ เลขที่ 39  ม.4/5")
