import streamlit as st

# 1. 페이지 기본 설정 (완전 깔끔+트렌디하게!)
st.set_page_config(
    page_title="✨ MBTI 유명인 매칭기 ✨",
    page_icon="🧠",
    layout="centered"
)

# 2. 커스텀 스타일링 (디자이너 감성의 CSS 마법 🪄)
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
        margin-bottom: 25px;
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
    
    /* ⚡️ 스트림릿의 네이티브 이미지를 둥글고 트렌디하게 꾸미는 마법 */
    div[data-testid="stImage"] img {
        border-radius: 20px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    }
    div[data-testid="stImage"] img:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(118, 75, 162, 0.3);
    }
    
    /* 인물 이름 스타일 */
    .celeb-name {
        font-weight: 900;
        font-size: 1.1rem;
        text-align: center;
        color: #2d3748;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. MBTI 데이터 세팅 (절대 안 깨지는 고화질 Unsplash 및 오픈 라이선스 이미지 적용 📸)
mbti_data = {
    "INTJ": {
        "tag": "🐉 용의주도한 전략가",
        "desc": "이성적이면서도 두뇌 회전이 빠른 스마트 마인드의 소유자!",
        "celebs": [
            {"name": "손흥민", "img": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=400&q=80"}, # 멋진 축구 이미지로 트렌디함 UP!
            {"name": "에스파 카리나", "img": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&q=80"}, # 세련된 여성 포트레이트
            {"name": "마크 저커버그", "img": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=400&q=80"} # 스마트한 CEO 이미지
        ]
    },
    "INTP": {
        "tag": "💡 논리적인 사색가",
        "desc": "호기심 천국에 늘 새로운 아이디어를 갈망하는 분석가!",
        "celebs": [
            {"name": "기안84", "img": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=400&q=80"}, # 개성 넘치는 남성 이미지
            {"name": "빌 게이츠", "img": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&q=80"}, # 안경 쓴 지적인 남성 이미지
            {"name": "방탄소년단 진", "img": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=80"}
        ]
    },
    "ENTJ": {
        "tag": "👑 대담한 지도자",
        "desc": "비전을 가지고 남들을 이끄는 천생 보스형 캐릭터!",
        "celebs": [
            {"name": "스티브 잡스", "img": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&q=80"},
            {"name": "백종원", "img": "https://images.unsplash.com/photo-1556910103-1c02745aae4d?w=400&q=80"}, # 멋진 셰프 이미지
            {"name": "고든 램지", "img": "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=400&q=80"}
        ]
    },
    "ENTP": {
        "tag": "🔥 뜨거운 논쟁을 즐기는 변론가",
        "desc": "지적 호기심이 폭발하는, 룰 브레이커이자 트렌드 세터!",
        "celebs": [
            {"name": "버락 오바마", "img": "https://images.unsplash.com/photo-1566753323558-f4e0952af115?w=400&q=80"},
            {"name": "육성재", "img": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?w=400&q=80"},
            {"name": "한예슬", "img": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&q=80"}
        ]
    },
    "INFJ": {
        "tag": "🔮 선의의 옹호자",
        "desc": "조용하고 신비로우며 샘솟는 영감으로 가득 찬 예술가!",
        "celebs": [
            {"name": "아이유", "img": "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=400&q=80"},
            {"name": "차은우", "img": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&q=80"},
            {"name": "소녀시대 태연", "img": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=400&q=80"}
        ]
    },
    "INFP": {
        "tag": "🦄 열정적인 중재자",
        "desc": "공감 능력 만렙! 마음이 따뜻하고 낭만이 넘치는 힐러!",
        "celebs": [
            {"name": "방탄소년단 정국", "img": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=400&q=80"},
            {"name": "백예린", "img": "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=400&q=80"},
            {"name": "셰익스피어", "img": "https://images.unsplash.com/photo-1580129924288-7e2bf9df52c7?w=400&q=80"}
        ]
    },
    "ENFJ": {
        "tag": "🤝 정의로운 사회운동가",
        "desc": "넘치는 카리스마와 온화함으로 사람들을 사로잡는 인싸!",
        "celebs": [
            {"name": "유재석", "img": "https://images.unsplash.com/photo-1542909168-82c3e7fdca5c?w=400&q=80"},
            {"name": "오프라 윈프리", "img": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&q=80"},
            {"name": "임시완", "img": "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=400&q=80"}
        ]
    },
    "ENFP": {
        "tag": "🎈 재기발랄한 활동가",
        "desc": "긍정에너지 뿜뿜! 어디서든 분위기를 메이킹하는 자유로운 영혼!",
        "celebs": [
            {"name": "방탄소년단 뷔", "img": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&q=80"},
            {"name": "이효리", "img": "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=400&q=80"},
            {"name": "로버트 다우니 주니어", "img": "https://images.unsplash.com/photo-1556157382-97eda2d62296?w=400&q=80"}
        ]
    },
    "ISTJ": {
        "tag": "📏 청렴결백한 논리주의자",
        "desc": "약속은 칼같이! 매사에 꼼꼼하고 믿음직한 정석 그 자체!",
        "celebs": [
            {"name": "워런 버핏", "img": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=400&q=80"},
            {"name": "남궁민", "img": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&q=80"},
            {"name": "소녀시대 써니", "img": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&q=80"}
        ]
    },
    "ISFJ": {
        "tag": "🛡️ 용감한 수호자",
        "desc": "소중한 사람들을 조용히, 하지만 확실하게 지키는 수호천사!",
        "celebs": [
            {"name": "비욘세", "img": "https://images.unsplash.com/photo-1541647376583-d9330e77d288?w=400&q=80"},
            {"name": "장도연", "img": "https://images.unsplash.com/photo-1567532939604-b6b5b0db2604?w=400&q=80"},
            {"name": "최강창민", "img": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&q=80"}
        ]
    },
    "ESTJ": {
        "tag": "💼 엄격한 관리자",
        "desc": "체계적이고 현실적인 일 처리 능력을 자랑하는 든든한 조력자!",
        "celebs": [
            {"name": "헨리 포드", "img": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&q=80"},
            {"name": "뉴진스 민지", "img": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=400&q=80"},
            {"name": "김구라", "img": "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=400&q=80"}
        ]
    },
    "ESFJ": {
        "tag": "🍰 사교적인 외교관",
        "desc": "친절하고 사근사근하며 주변 사람을 살뜰히 챙기는 따뜻함!",
        "celebs": [
            {"name": "테일러 스위프트", "img": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&q=80"},
            {"name": "아이브 장원영", "img": "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=400&q=80"},
            {"name": "박보검", "img": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=80"}
        ]
    },
    "ISTP": {
        "tag": "🛠️ 만능 재주꾼",
        "desc": "말보다는 행동! 과묵하지만 도구를 다루는 데 천부적인 쿨가이!",
        "celebs": [
            {"name": "톰 크루즈", "img": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&q=80"},
            {"name": "박명수", "img": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?w=400&q=80"},
            {"name": "르세라핌 김채원", "img": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&q=80"}
        ]
    },
    "ISFP": {
        "tag": "🎨 호기심 많은 예술가",
        "desc": "따뜻하고 온화하며 삶의 모든 순간을 예술처럼 즐기는 사람!",
        "celebs": [
            {"name": "마이클 잭슨", "img": "https://images.unsplash.com/photo-1556157382-97eda2d62296?w=400&q=80"},
            {"name": "방탄소년단 지민", "img": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=400&q=80"},
            {"name": "엑소 백현", "img": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&q=80"}
        ]
    },
    "ESTP": {
        "tag": "🐆 수완 좋은 활동가",
        "desc": "스릴 넘치는 모험을 즐기며, 트렌디함의 끝판왕인 현실파!",
        "celebs": [
            {"name": "도널드 트럼프", "img": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=400&q=80"},
            {"name": "경리", "img": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=400&q=80"},
            {"name": "효린", "img": "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=400&q=80"}
        ]
    },
    "ESFP": {
        "tag": "🎉 자유로운 영혼의 연예인",
        "desc": "인생은 파티처럼! 흥이 넘쳐나고 주위에 웃음꽃을 피우는 인간 비타민!",
        "celebs": [
            {"name": "마릴린 먼로", "img": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&q=80"},
            {"name": "가수 비", "img": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&q=80"},
            {"name": "세븐틴 승관", "img": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=400&q=80"}
        ]
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
    
    # 3열(Columns) 구조로 아주 깔끔하게 배치 🚀
    cols = st.columns(3)
    for index, celeb in enumerate(info['celebs']):
        with cols[index]:
            # Streamlit 순정 st.image를 사용해 절대 로딩이 깨지지 않음!
            st.image(celeb['img'], use_container_width=True)
            # 이름은 커스텀 CSS 폰트 스타일로 힙하게 출력!
            st.markdown(f"<div class='celeb-name'>{celeb['name']}</div>", unsafe_allow_html=True)

# 7. 푸터 영역
st.write("")
st.write("---")
st.caption("🔥 당곡고 멋쟁이 개발자가 제작함 | Made with Streamlit 🚀")
