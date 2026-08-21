import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(page_title="Máy tính BMI", page_icon="🩺", layout="centered")


def ve_bieu_do_bmi(bmi_nguoi_dung):
    fig, ax = plt.subplots(figsize=(10, 2.2))

    vung = [
        (15, 18.5, "#FF9800", "Thiếu cân"),
        (18.5, 25, "#4CAF50", "Bình thường"),
        (25, 30, "#FF9800", "Thừa cân"),
        (30, 40, "#F44336", "Béo phì"),
    ]

    for x_start, x_end, mau, nhan in vung:
        rect = patches.Rectangle((x_start, 0), x_end - x_start, 1, facecolor=mau, edgecolor="white", linewidth=1.5, alpha=0.85)
        ax.add_patch(rect)
        ax.text((x_start + x_end) / 2, 0.5, nhan, ha="center", va="center", fontsize=10, fontweight="bold", color="white")

    bmi_hien_thi = max(15, min(40, bmi_nguoi_dung))
    ax.plot(bmi_hien_thi, 1.15, marker="v", markersize=18, color="#212121", markeredgecolor="white", markeredgewidth=2)
    ax.text(bmi_hien_thi, 1.45, f"BMI của bạn: {bmi_nguoi_dung}", ha="center", va="bottom", fontsize=11, fontweight="bold", color="#212121")

    ax.set_xlim(15, 40)
    ax.set_ylim(0, 1.9)
    ax.set_yticks([])
    ax.set_xticks([15, 18.5, 25, 30, 40])
    ax.set_xticklabels(["15", "18.5", "25", "30", "40"], fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("Chỉ số BMI", fontsize=11, fontweight="bold")

    plt.tight_layout()
    return fig


def tinh_bmi(can_nang, chieu_cao):
    chieu_cao_m = chieu_cao / 100
    bmi = round(can_nang / (chieu_cao_m ** 2), 1)

    if bmi < 18.5:
        phan_loai, mau = "Thiếu cân", "#FF9800"
    elif bmi < 25:
        phan_loai, mau = "Bình thường", "#4CAF50"
    elif bmi < 30:
        phan_loai, mau = "Thừa cân", "#FF9800"
    else:
        phan_loai, mau = "Béo phì", "#F44336"

    can_min = round(18.5 * (chieu_cao_m ** 2), 1)
    can_max = round(24.9 * (chieu_cao_m ** 2), 1)

    return bmi, phan_loai, mau, can_min, can_max


# ========== GIAO DIỆN ==========

st.title("🩺 Máy tính chỉ số BMI")
st.markdown("Nhập cân nặng và chiều cao để tính chỉ số khối cơ thể (BMI), xem phân loại theo tiêu chuẩn của Tổ chức Y tế Thế giới (WHO) và khoảng cân nặng lý tưởng tương ứng với chiều cao của bạn.")

st.divider()

col1, col2 = st.columns(2)
with col1:
    can_nang = st.slider("⚖️ Cân nặng (kg)", min_value=30.0, max_value=200.0, value=60.0, step=0.1)
with col2:
    chieu_cao = st.slider("📏 Chiều cao (cm)", min_value=100.0, max_value=220.0, value=165.0, step=0.1)

nut_tinh = st.button("Tính BMI", type="primary", use_container_width=True)

if nut_tinh:
    bmi, phan_loai, mau, can_min, can_max = tinh_bmi(can_nang, chieu_cao)

    st.divider()

    col_bmi, col_phan_loai = st.columns([1, 2])
    with col_bmi:
        st.metric(label="Chỉ số BMI", value=f"{bmi}")
    with col_phan_loai:
        st.markdown(f'<div style="text-align:center; padding:16px; border-radius:12px; background-color:{mau}; color:white; font-size:22px; font-weight:bold; box-shadow: 0 2px 6px rgba(0,0,0,0.15); margin-top: 8px;">{phan_loai}</div>', unsafe_allow_html=True)

    st.markdown(f'<div style="text-align:center; padding:14px; border-radius:12px; background-color:#E3F2FD; color:#0D47A1; font-size:16px; border: 1px solid #BBDEFB; margin-top: 16px;"><b>Khoảng cân nặng lý tưởng</b> với chiều cao {chieu_cao:.0f} cm:<br><span style="font-size:20px; font-weight:bold;">{can_min} kg – {can_max} kg</span></div>', unsafe_allow_html=True)

    st.markdown("### 📊 Vị trí BMI của bạn trên thang phân loại")
    st.pyplot(ve_bieu_do_bmi(bmi))

st.divider()
st.markdown('<div style="text-align:center; color:#757575; font-size:13px; font-style:italic; padding:10px;">⚠️ <b>Miễn trừ trách nhiệm:</b> Công cụ này chỉ mang tính chất tham khảo, không thay thế cho tư vấn, chẩn đoán hoặc điều trị y tế chuyên nghiệp. Chỉ số BMI không phản ánh đầy đủ tình trạng sức khỏe (không tính đến tỉ lệ mỡ – cơ, độ tuổi, giới tính, chủng tộc). Vui lòng tham khảo ý kiến bác sĩ hoặc chuyên gia dinh dưỡng để có đánh giá chính xác về sức khỏe cá nhân.</div>', unsafe_allow_html=True)
