import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --------------------------
# 登录页面
# --------------------------
def login_page():
    st.markdown("## 🔒 请登录使用")
    username = st.text_input("用户名")
    password = st.text_input("密码", type="password")
    login_button = st.button("登录")

    if login_button:
        if username == "MAGO123" and password == "MAGO123":
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("❌ 用户名或密码错误，请重试！")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
    st.stop()

# --------------------------
# 初始化
# --------------------------
if "name" not in st.session_state:
    st.session_state.name = ""
if "student_id" not in st.session_state:
    st.session_state.student_id = ""
if "score1" not in st.session_state:
    st.session_state.score1 = 0
if "score2" not in st.session_state:
    st.session_state.score2 = 0
if "score3" not in st.session_state:
    st.session_state.score3 = 0
if "score4" not in st.session_state:
    st.session_state.score4 = 0
if "score5" not in st.session_state:
    st.session_state.score5 = 0

# --------------------------
# ✅ 云端永久有效中文设置（不用字体文件！）
# --------------------------
st.set_page_config(page_title="大学数学成绩查询", page_icon="📊", layout="wide")
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.unicode_minus"] = False

# --------------------------
# 侧边栏
# --------------------------
with st.sidebar:
    st.title("📚 成绩查询工具")
    st.markdown("---")
    if st.button("🔄 重置所有信息"):
        st.session_state.name = ""
        st.session_state.student_id = ""
        st.session_state.score1 = 0
        st.session_state.score2 = 0
        st.session_state.score3 = 0
        st.session_state.score4 = 0
        st.session_state.score5 = 0
        st.rerun()

# --------------------------
# 主页面
# --------------------------
st.title("🎓 大学数学成绩查询与分析")
col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input("👤 名字", key="name")
with col2:
    class_name = st.selectbox("🏫 班级", ["N1", "N2"])
with col3:
    student_id = st.text_input("🆔 学号", key="student_id")

st.markdown("---")

st.subheader("📝 成绩录入")
col4, col5 = st.columns(2)
with col4:
    score1 = st.number_input("线性代数", 0, 100, key="score1")
    score2 = st.number_input("微积分上", 0, 100, key="score2")
    score3 = st.number_input("微积分下", 0, 100, key="score3")
with col5:
    score4 = st.number_input("概率论与数理统计", 0, 100, key="score4")
    score5 = st.number_input("统计学原理", 0, 100, key="score5")

st.markdown("---")

# --------------------------
# 图表（中文100%正常）
# --------------------------
if st.session_state.name.strip() and st.session_state.student_id.strip():
    st.success(f"✅ {class_name} | {name} | 学号：{student_id}")

    subjects = ["线性代数", "微积分上", "微积分下", "概率论", "统计学原理"]
    scores = [score1, score2, score3, score4, score5]

    col_a, col_b = st.columns(2)
    with col_a:
        st.write("📊 成绩柱状图")
        fig1, ax1 = plt.subplots(figsize=(6,5))
        ax1.bar(subjects, scores, color=["#1f77b4","#2ca02c","#ff7f0e","#d62728","#9467bd"])
        ax1.set_ylim(0,105)
        plt.xticks(rotation=20)
        st.pyplot(fig1)

    with col_b:
        st.write("📈 成绩雷达图")
        N = len(subjects)
        angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
        values = scores + [scores[0]]
        angles += angles[:1]

        fig2, ax2 = plt.subplots(figsize=(6,5), subplot_kw=dict(polar=True))
        ax2.plot(angles, values)
        ax2.fill(angles, values, alpha=0.3)
        ax2.set_xticks(angles[:-1])
        ax2.set_xticklabels(subjects)
        ax2.set_ylim(0,100)
        st.pyplot(fig2)
else:
    st.warning("⚠️ 请输入姓名和学号")
