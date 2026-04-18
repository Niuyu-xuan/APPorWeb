import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --------------------------
# 初始化会话状态
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
# 页面设置
# --------------------------
st.set_page_config(
    page_title="📚 大学数学成绩查询",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# --------------------------
# 侧边栏
# --------------------------
with st.sidebar:
    st.title("📚 大学数学成绩工具")
    st.markdown("---")
    st.info("💡 功能说明：\n- 输入个人信息\n- 录入各科成绩\n- 自动生成柱状图+雷达图")
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
st.markdown("输入你的个人信息和各科成绩，系统自动生成可视化图表~")
st.markdown("---")

# --------------------------
# 信息输入
# --------------------------
col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input("👤 你的名字：", key="name")
with col2:
    class_name = st.selectbox("🏫 你的班级：", ["N1", "N2"])
with col3:
    student_id = st.text_input("🆔 你的学号：", key="student_id")

st.markdown("---")

# --------------------------
# 成绩输入
# --------------------------
st.subheader("📝 各科成绩录入（满分100分）")
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
# 图表展示
# --------------------------
if st.session_state.name.strip() and st.session_state.student_id.strip():
    st.subheader("📊 个人成绩可视化")
    st.success(f"✅ {class_name} | {st.session_state.name} | 学号：{st.session_state.student_id}")

    subjects = ["线性代数", "微积分上", "微积分下", "概率论", "统计学原理"]
    scores = [
        st.session_state.score1,
        st.session_state.score2,
        st.session_state.score3,
        st.session_state.score4,
        st.session_state.score5
    ]

    # ==============================================
    # 左图：柱状图
    # ==============================================
    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.write("📊 柱状图")
        fig1, ax1 = plt.subplots(figsize=(6, 5))
        colors = ["#1f77b4", "#2ca02c", "#ff7f0e", "#d62728", "#9467bd"]
        bars = ax1.bar(subjects, scores, color=colors, edgecolor="white", linewidth=1.2)
        
        for bar in bars:
            h = bar.get_height()
            ax1.text(bar.get_x()+bar.get_width()/2., h+1, f"{h}", ha="center", fontsize=10, fontweight="bold")
        
        ax1.set_ylim(0, 105)
        ax1.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=20, fontsize=9)
        st.pyplot(fig1)

    # ==============================================
    # 右图：雷达图（你要加的！）
    # ==============================================
    with col_chart2:
        st.write("📈 雷达图")
        N = len(subjects)
        angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
        scores_plot = scores.copy()
        angles += angles[:1]
        scores_plot += scores_plot[:1]

        fig2, ax2 = plt.subplots(figsize=(6, 5), subplot_kw=dict(polar=True))
        ax2.plot(angles, scores_plot, color="#ff6b6b", linewidth=2, label="分数")
        ax2.fill(angles, scores_plot, color="#ff6b6b", alpha=0.3)
        ax2.set_xticks(angles[:-1])
        ax2.set_xticklabels(subjects, fontsize=10)
        ax2.set_ylim(0, 100)
        ax2.set_title("成绩雷达分布", pad=20)
        st.pyplot(fig2)

else:
    st.warning("⚠️ 请先完整输入姓名和学号！")