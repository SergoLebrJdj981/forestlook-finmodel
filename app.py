import streamlit as st

st.set_page_config(page_title="FORESTLOOK: Финансовое моделирование", layout="wide")
st.title("💡 FORESTLOOK — Финансовое моделирование “А если...”")
st.markdown("Загрузите данные и проверьте: **можно ли тратить больше или нет**.")

# Ввод данных вручную
with st.sidebar:
    st.header("📥 Ввод параметров")
    current_profit = st.number_input("Чистая прибыль за месяц (₽)", value=300000)
    current_expense = st.number_input("Расходы за месяц (₽)", value=210000)
    st.markdown("---")
    st.subheader("🧠 Что ты хочешь сделать?")
    scenario = st.selectbox("Выбери действие", [
        "Нанять нового сотрудника",
        "Увеличить бюджет на рекламу",
        "Снять дополнительное помещение",
        "Увеличить бюджет на контент",
        "Другое"
    ])
    new_expense = st.number_input("Во сколько это обойдётся? (₽)", value=100000)

# Расчёт
st.markdown("## 📊 Результат моделирования")

total_new_expense = current_expense + new_expense
new_net_profit = current_profit - total_new_expense
roi = round((new_net_profit / total_new_expense) * 100, 2) if total_new_expense > 0 else 0

if new_net_profit < 0:
    st.error(f"❌ Не рекомендуется.\n\nПосле внедрения этого решения вы уйдёте в убыток: **{new_net_profit}₽**.")
    if roi < 10:
        st.warning("ROI упадёт ниже 10% — бизнес станет убыточным.")
    st.markdown("💡 Совет: отложи это решение или увеличь прибыль минимум на " +
                f"**{abs(new_net_profit)}₽**, чтобы остаться в нуле.")
else:
    st.success(f"✅ Разрешено. После внедрения останется чистыми: **{new_net_profit}₽**")
    st.markdown(f"📈 Новый ROI: **{roi}%**")

st.markdown("---")
st.caption("FORESTLOOK | Финансовая модель для принятия решений")
