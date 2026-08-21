import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Cấu hình trang
st.set_page_config(
    page_title="Máy tính BMI",
    page_icon="🩺",
    layout="centered"
)


def ve_bieu_do_bmi(bmi_nguoi_dung):
    fig, ax = plt.subplots(figsize=(10, 2.2))

    # Bốn vùng phân loại với màu tương ứng
    vung = [
        (15, 18.5, "#FF9800", "Thiếu cân"),
        (18.5, 25, "#4CAF50", "Bình thường"),
        (25, 30, "#FF9800", "Thừa cân"),
        (30, 40, "#F44336", "Béo phì"),
    ]

    for x_start, x_end, mau, nhan in vung:
        ax.add_patch(patches.Rectangle(
            (x_start, 0), x_end - x_start, 1,
            facecolor=mau, edgecolor="white", linewidth=1.5, alpha=0.85
        ))
        ax.text(
            (x_start + x_end) / 2, 0.5, nhan,
            ha="center", va="center",
            fontsize=10, fontweight="bold", color="white"
        )

    # Điểm đánh dấu BMI của người dùng
    bmi_hien_thi = max(15, min(40, bmi_nguoi_dung))
    ax.plot(bmi_hien_thi, 1.15, marker="v", markersize=18,
            color="#212121", markeredgecolor="white", markeredgewidth=2)
    ax.text(bmi_hien_thi, 1.45, f"BMI của bạn: {bmi_nguoi_dung}",
