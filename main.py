import streamlit as st

# 1. 페이지 기본 설정 (완전 깔끔+트렌디하게!)
st.set_page_config(
    page_title="✨ MBTI 유명인 매칭기 ✨",
    page_icon="🧠",
    layout="centered"
)

# 2. 커스텀 스타일링 (MZ 감성 한 스푼 추가 🥄)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }
    .main-title {
        font-size: 2.8rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 1.1rem;
        text-align: center;
        color: #666666;
        margin-bottom: 30px;
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        transition: transform 0.2s ease-in-out;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .badge {
        background: #764ba2;
        color: white;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. MBTI 데이터 세팅 (유명인 & 키워드 매칭)
mbti_data = {
    "INTJ": {
        "tag": "🐉 용의주도한 전략가",
        "desc": "이성적이면서도 두뇌 회전이 빠른 스마트 마인드의 소유자!",
        "celebs": ["손흥민", "강동원", "크리스토퍼 놀란", "마크 저커버그", "에스파 카리나"]
    },
    "INTP": {
        "tag": "💡 논리적인 사색가",
        "desc": "호기심 천국에 늘 새로운 아이디어를 갈망하는 분석가!",
        "celebs": ["기안84", "방탄소년단 진", "빌 게이츠", "르세라핌 사쿠라", "적재"]
    },
    "ENTJ": {
        "tag": "👑 대담한 지도자",
        "desc": "비전을 가지고 남들을 이끄는 천생 보스형 캐릭터!",
        "celebs": ["백종원", "지코", "스티브 잡스", "고든 램지", "여진구"]
    },
    "ENTP": {
        "tag": "🔥 뜨거운 논쟁을 즐기는 변론가",
        "desc": "지적 호기심이 폭발하는, 룰 브레이커이자 트렌드 세터!",
        "celebs": ["육성재", "제시", "한예슬", "버락 오바마", "곽튜브"]
    },
    "INFJ": {
        "tag": "🔮 선의의 옹호자",
        "desc": "조용하고 신비로우며 샘솟는 영감으로 가득 찬 예술가!",
        "celebs": ["아이유", "소녀시대 태연", "남주혁", "차은우", "베네딕트 컴버배치"]
    },
    "INFP": {
        "tag": "🦄 열정적인 중재자",
        "desc": "공감 능력 만렙! 마음이 따뜻하고 낭만이 넘치는 힐러!",
        "celebs": ["방탄소년단 정국", "백예린", "조이(레드벨벳)", "기리보이", "키드밀리"]
    },
    "ENFJ": {
        "tag": "🤝 정의로운 사회운동가",
        "desc": "넘치는 카리스마와 온화함으로 사람들을 사로잡는 인싸!",
        "celebs": ["유재석", "임시완", "EXO 수호", "세븐틴 민규", "오프라 윈프리"]
    },
    "ENFP": {
        "tag": "🎈 재기발랄한 활동가",
        "desc": "긍정에너지 뿜뿜! 어디서든 분위기를 메이킹하는 자유로운 영혼!",
        "celebs": ["방탄소년단 뷔", "이효리", "조세호", "로버트 다우니 주니어", "미연((여자)아이들)"]
    },
    "ISTJ": {
        "tag": "📏 청렴결백한 논리주의자",
        "desc": "약속은 칼같이! 매사에 꼼꼼하고 믿음직한 정석 그 자체!",
        "celebs": ["소녀시대 써니", "남궁민", "차태현", "워런 버핏", "성시경"]
    },
    "ISFJ": {
        "tag": "🛡️ 용감한 수호자",
        "desc": "소중한 사람들을 조용히, 하지만 확실하게 지키는 수호천사!",
        "celebs": ["안영미", "장도연", "최강창민", "비욘세", "세븐틴 정한"]
    },
    "ESTJ": {
        "tag": "💼 엄격한 관리자",
        "desc": "체계적이고 현실적인 일 처리 능력을 자랑하는 든든한 조력자!",
        "celebs": ["한채영", "김구라", "데프콘", "존 D. 록펠러", "뉴진스 민지"]
    },
    "ESFJ": {
        "tag": "🍰 사교적인 외교관",
        "desc": "친절하고 사근사근하며 주변 사람을 살뜰히 챙기는 따뜻함!",
        "celebs": ["혜리", "황광희", "박보검", "테일러 스위프트", "아이브 장원영"]
    },
    "ISTP": {
        "tag": "🛠️ 만능 재주꾼",
        "desc": "말보다는 행동! 과묵하지만 도구를 다루는 데 천부적인 쿨가이!",
        "celebs": ["한혜진", "김종민", "박명수", "톰 크루즈", "르세라핌 김채원"]
    },
    "ISFP": {
        "tag": "🎨 호기심 많은 예술가",
        "desc": "따뜻하고 온화하며 삶의 모든 순간을 예술처럼 즐기는 사람!",
        "celebs": ["방탄소년단 지민", "레드벨벳 슬기", "엑소 백현", "마이클 잭슨", "트와이스 지효"]
    },
    "ESTP": {
        "tag": "🐆 수완 좋은 활동가",
        "desc": "스릴 넘치는 모험을 즐기며, 트렌디함의 끝판왕인 현실파!",
        "celebs": ["효린", "이유비", "경리", "도널드 트럼프", "NCT 재현"]
    },
    "ESFP": {
        "tag": "🎉 자유로운 영혼의 연예인",
        "desc": "인생은 파티처럼! 흥이 넘쳐나고 주위에 웃음꽃을 피우는 인간 비타민!",
        "celebs": ["가수 비", "개리", "마릴린 먼로", "지효(트와이스)", "세븐틴 승관"]
    }
}

# 4. 헤더 영역
st.markdown("<div class='main-title'>⚡️ MBTI Soulmate Finder</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>나랑 같은 MBTI를 가진 힙한 셀럽들은 누가 있을까? 👀</div>", unsafe_allow_html=True)

# 5. MBTI 선택 셀렉트박스
st.write("---")
selected_mbti = st.selectbox(
    "🧐 너의 MBTI는 뭐야? 선택해봐!",
    options=list(mbti_data.keys()),
    index=0
)

# 6. 결과 화면 보여주기
if selected_mbti:
    info = mbti_data[selected_mbti]
    
    st.write("")
    st.write("")
    
    # 트렌디한 카드 레이아웃 적용
    st.markdown(f"""
        <div class='card'>
            <span class='badge'>{selected_mbti}</span>
            <h3 style='margin: 5px 0 10px 0; color: #1E1E1E;'>{info['tag']}</h3>
            <p style='color: #4a5568; font-size: 0.95rem; line-height: 1.6;'>"{info['desc']}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 같은 MBTI를 가진 유명인들 보여주기
    st.write("#### 🌟 동족 발견! 이 분들이 너랑 같은 MBTI야:")
    
    # 2열로 깔끔하게 배치하기
    cols = st.columns(2)
    for index, celeb in enumerate(info['celebs']):
        col_index = index % 2
        with cols[col_index]:
            st.info(f"✨ **{celeb}**")

# 7. 푸터 영역
st.write("")
st.write("---")
st.caption("🔥 당곡고 멋쟁이 개발자가 제작함 | Made with Streamlit 🚀")
