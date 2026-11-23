
import streamlit as st

st.set_page_config(page_title="자가호흡기질환 검사앱", page_icon="🫁")
st.title("🫁 자가호흡기질환 검사앱")
st.write("현재 본인의 상태와 수면 시간을 입력해 주세요.")

# 1. 상태 선택
symptom = st.selectbox(
    "현재 상태를 선택하세요:",
    ["몸이 춥고 떨림", "기침과 콧물", "미열증상", "해당없음"]
)

# 2. 수면 시간 입력
sleeptime = st.slider(
    "어젯밤 수면 시간(시간):",
    min_value=0,
    max_value=24,
    value=7
)

# 3. 상태별 감점 기준
symptom_scores = {
    "몸이 춥고 떨림": -30,
    "기침과 콧물": -40,
    "미열증상": -50,
    "해당없음": 0
}

# 4. 상태별 대처법
condition = {
    "몸이 춥고 떨림": [
        "따뜻하게 보온 유지하기",
        "체온 측정 및 변화 확인하기",
        "고열 동반 시 병원 방문하기"
    ],
    "기침과 콧물": [
        "마스크 착용하기",
        "따뜻한 물 자주 마시기",
        "증상 지속 시 진료받기"
    ],
    "미열증상": [
        "충분한 휴식과 수면 취하기",
        "수시로 체온 체크하기",
        "수분 충분히 섭취하기"
    ],
    "해당없음": [
        "손 씻기 생활화하기",
        "하루 2~3번 실내 환기하기",
        "규칙적인 생활로 면역력 유지하기"
    ]
}

# 5. 위험도 확인 함수
def check_risk(condition, sleeptime):
    score = 100
    score += symptom_scores[condition]

    if sleeptime <= 5:
        score -= 10

    score = max(0, score)
    return score

# 6. 검사 결과 출력
if st.button("검사 결과 확인하기"):
    st.divider()

    # 점수 출력
    total_score = check_risk(symptom, sleeptime)

    st.subheader(f"💯 총 건강 점수: {total_score}점")
    st.progress(total_score / 100)

    # 경고 메시지 출력
    if total_score <= 50:
        st.error("🚨 건강 점수가 낮습니다. 의료진의 진료를 받아보세요.")
    elif total_score <= 70:
        st.warning("⚠️ 무리하지 말고 충분한 휴식을 취하세요.")
    else:
        st.success("✅ 건강관리에 신경 써주세요!")

    # 수면 상태 경고
    if sleeptime <= 5:
        st.warning("💤 수면 시간이 5시간 이하입니다. 충분한 수면을 취하세요.")

    # 7. 대처법을 표 형태로 출력
    st.subheader(f"📋 '{symptom}' 대처법")

    data = []
    for i, action in enumerate(condition[symptom], start=1):
        data.append({
            "번호": i,
            "대처법": action
        })

    st.table(data)

st.caption("※ 참고용 프로그램이며, 정확한 진단은 병원을 이용해 주세요.")
