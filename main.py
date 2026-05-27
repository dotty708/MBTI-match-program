import streamlit as st

# 1. 페이지 기본 설정 (완전 깔끔+트렌디하게!)
st.set_page_config(
    page_title="✨ MBTI 유명인 매칭기 ✨",
    page_icon="🧠",
    layout="centered"
)

# 2. 커스텀 스타일링 (MZ 감성 + 힙한 이미지 레이아웃 🎨)
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
    
    /* 유명인 프로필 카드 스타일링 ✨ */
    .celeb-container {
        text-align: center;
        padding: 15px;
        background: #f8fafc;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
        margin-bottom: 15px;
        transition: transform 0.2s ease-in-out;
    }
    .celeb-container:hover {
        transform: translateY(-5px);
    }
    .celeb-img {
        border-radius: 50%;
        width: 120px;
        height: 120px;
        object-fit: cover;
        border: 3px solid #764ba2;
        box-shadow: 0 4px 10px rgba(118, 75, 162, 0.2);
    }
    .celeb-name {
        font-weight: bold;
        font-size: 1.05rem;
        color: #1a202c;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. MBTI 데이터 세팅 (실제 고화질 유명인 이미지 링크 포함 📸)
mbti_data = {
    "INTJ": {
        "tag": "🐉 용의주도한 전략가",
        "desc": "이성적이면서도 두뇌 회전이 빠른 스마트 마인드의 소유자!",
        "celebs": [
            {"name": "손흥민", "img": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Son_Heung-min_2022.jpg"},
            {"name": "에스파 카리나", "img": "https://upload.wikimedia.org/wikipedia/commons/f/fc/230601_Karina_%28aespa%29.jpg"},
            {"name": "마크 저커버그", "img": "https://upload.wikimedia.org/wikipedia/commons/1/18/Mark_Zuckerberg_F8_2019_Keynote_%2831119226218%29_%28cropped%29.jpg"}
        ]
    },
    "INTP": {
        "tag": "💡 논리적인 사색가",
        "desc": "호기심 천국에 늘 새로운 아이디어를 갈망하는 분석가!",
        "celebs": [
            {"name": "기안84", "img": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Gian84_in_2023.jpg"},
            {"name": "빌 게이츠", "img": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Bill_Gates_2017_%28cropped%29.jpg"},
            {"name": "방탄소년단 진", "img": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Jin_at_a_press_conference_for_the_BBMAs_on_May_29%2C_2017.png"}
        ]
    },
    "ENTJ": {
        "tag": "👑 대담한 지도자",
        "desc": "비전을 가지고 남들을 이끄는 천생 보스형 캐릭터!",
        "celebs": [
            {"name": "스티브 잡스", "img": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Steve_Jobs_Headshot_2010-CROP2.jpg"},
            {"name": "백종원", "img": "https://upload.wikimedia.org/wikipedia/commons/c/ca/Paik_Jong-won_in_November_2019.png"},
            {"name": "고든 램지", "img": "https://upload.wikimedia.org/wikipedia/commons/0/02/Gordon_Ramsay_at_the_2017_VEGAS_UNCORK%27D_%28cropped%29.jpg"}
        ]
    },
    "ENTP": {
        "tag": "🔥 뜨거운 논쟁가",
        "desc": "지적 호기심이 폭발하는, 룰 브레이커이자 트렌드 세터!",
        "celebs": [
            {"name": "버락 오바마", "img": "https://upload.wikimedia.org/wikipedia/commons/8/8d/President_Barack_Obama.jpg"},
            {"name": "육성재", "img": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Yook_Sung-jae_at_a_fansign_on_June_25%2C_2022.jpg"},
            {"name": "한예슬", "img": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Han_Ye-seul_on_October_17%2C_2019.png"}
        ]
    },
    "INFJ": {
        "tag": "🔮 선의의 옹호자",
        "desc": "조용하고 신비로우며 샘솟는 영감으로 가득 찬 예술가!",
        "celebs": [
            {"name": "아이유", "img": "https://upload.wikimedia.org/wikipedia/commons/c/c3/IU_at_a_fansign_event_in_Sinchon_on_December_2019.jpg"},
            {"name": "차은우", "img": "https://upload.wikimedia.org/wikipedia/commons/2/23/Cha_Eun-woo_for_Marie_Claire_Korea_on_February_2022.jpg"},
            {"name": "소녀시대 태연", "img": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Taeyeon_at_the_SM_Town_Live_2022.jpg"}
        ]
    },
    "INFP": {
        "tag": "🦄 열정적인 중재자",
        "desc": "공감 능력 만렙! 마음이 따뜻하고 낭만이 넘치는 힐러!",
        "celebs": [
            {"name": "방탄소년단 정국", "img": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Jungkook_on_Melon_Music_Awards_2019.jpg"},
            {"name": "백예린", "img": "https://upload.wikimedia.org/wikipedia/commons/3/36/Yerin_Baek_in_2016.jpg"},
            {"name": "셰익스피어", "img": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Shakespeare.jpg"}
        ]
    },
    "ENFJ": {
        "tag": "🤝 정의로운 사회운동가",
        "desc": "넘치는 카리스마와 온화함으로 사람들을 사로잡는 인싸!",
        "celebs": [
            {"name": "유재석", "img": "https://upload.wikimedia.org/wikipedia/commons/b/be/Yoo_Jae-suk.jpg"},
            {"name": "오프라 윈프리", "img": "https://upload.wikimedia.org/wikipedia/commons/2/2c/Oprah_Winfrey_at_the_Golden_Globes_2018.jpg"},
            {"name": "임시완", "img": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Yim_Si-wan_at_the_MBC_Drama_Awards_on_December_30%2C_2017.jpg"}
        ]
    },
    "ENFP": {
        "tag": "🎈 재기발랄한 활동가",
        "desc": "긍정에너지 뿜뿜! 어디서든 분위기를 메이킹하는 자유로운 영혼!",
        "celebs": [
            {"name": "방탄소년단 뷔", "img": "https://upload.wikimedia.org/wikipedia/commons/0/0f/V_on_Melon_Music_Awards_2019.jpg"},
            {"name": "이효리", "img": "https://upload.wikimedia.org/wikipedia/commons/0/05/Lee_Hyo-ri_at_an_event_on_October_24%2C_2013.jpg"},
            {"name": "로버트 다우니 주니어", "img": "https://upload.wikimedia.org/wikipedia/commons/9/94/Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg"}
        ]
    },
    "ISTJ": {
        "tag": "📏 청렴결백한 논리주의자",
        "desc": "약속은 칼같이! 매사에 꼼꼼하고 믿음직한 정석 그 자체!",
        "celebs": [
            {"name": "워런 버핏", "img": "https://upload.wikimedia.org/wikipedia/commons/5/51/Warren_Buffett_KU_Visit.jpg"},
            {"name": "남궁민", "img": "https://upload.wikimedia.org/wikipedia/commons/8/87/Namkoong_Min_at_the_KBS_Drama_Awards_on_December_31%2C_2017.jpg"},
            {"name": "소녀시대 써니", "img": "https://upload.wikimedia.org/wikipedia/commons/0/04/Sunny_at_the_Golden_Disc_Awards_on_January_15%2C_2014.jpg"}
        ]
    },
    "ISFJ": {
        "tag": "🛡️ 용감한 수호자",
        "desc": "소중한 사람들을 조용히, 하지만 확실하게 지키는 수호천사!",
        "celebs": [
            {"name": "비욘세", "img": "https://upload.wikimedia.org/wikipedia/commons/1/17/Beyonc%C3%A9_at_the_2018_Wearable_Art_Gala_%28cropped%29.jpg"},
            {"name": "장도연", "img": "https://upload.wikimedia.org/wikipedia/commons/1/14/Jang_Do-yeon_in_2018.jpg"},
            {"name": "최강창민", "img": "https://upload.wikimedia.org/wikipedia/commons/3/30/Changmin_at_Incheon_International_Airport_on_August_17%2C_2017.jpg"}
        ]
    },
    "ESTJ": {
        "tag": "💼 엄격한 관리자",
        "desc": "체계적이고 현실적인 일 처리 능력을 자랑하는 든든한 조력자!",
        "celebs": [
            {"name": "헨리 포드", "img": "https://upload.wikimedia.org/wikipedia/commons/1/18/Henry_ford_1919.jpg"},
            {"name": "뉴진스 민지", "img": "https://upload.wikimedia.org/wikipedia/commons/c/cc/NewJeans_Minji_Shinhan_Sol.jpg"},
            {"name": "김구라", "img": "https://upload.wikimedia.org/wikipedia/commons/0/03/Kim_Gu-ra_in_2016.jpg"}
        ]
    },
    "ESFJ": {
        "tag": "🍰 사교적인 외교관",
        "desc": "친절하고 사근사근하며 주변 사람을 살뜰히 챙기는 따뜻함!",
        "celebs": [
            {"name": "테일러 스위프트", "img": "https://upload.wikimedia.org/wikipedia/commons/b/b5/191125_Taylor_Swift_at_the_2019_American_Music_Awards_%28cropped%29.jpg"},
            {"name": "아이브 장원영", "img": "https://upload.wikimedia.org/wikipedia/commons/1/13/Jang_Won-young_at_the_AAA_2022.jpg"},
            {"name": "박보검", "img": "https://upload.wikimedia.org/wikipedia/commons/1/14/Park_Bo-gum_at_the_KBS_Drama_Awards_on_December_31%2C_2016.jpg"}
        ]
    },
    "ISTP": {
        "tag": "🛠️ 만능 재주꾼",
        "desc": "말보다는 행동! 과묵하지만 도구를 다루는 데 천부적인 쿨가이!",
        "celebs": [
            {"name": "톰 크루즈", "img": "https://upload.wikimedia.org/wikipedia/commons/3/33/Tom_Cruise_by_Gage_Skidmore_2.jpg"},
            {"name": "박명수", "img": "https://upload.wikimedia.org/wikipedia/commons/9/91/Park_Myeong-su_in_2018.jpg"},
            {"name": "르세라핌 김채원", "img": "https://upload.wikimedia.org/wikipedia/commons/8/84/Kim_Chae-won_at_the_2022_MMA.jpg"}
        ]
    },
    "ISFP": {
        "tag": "🎨 호기심 많은 예술가",
        "desc": "따뜻하고 온화하며 삶의 모든 순간을 예술처럼 즐기는 사람!",
        "celebs": [
            {"name": "마이클 잭슨", "img": "https://upload.wikimedia.org/wikipedia/commons/3/31/Michael_Jackson_in_1984.jpg"},
            {"name": "방탄소년단 지민", "img": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Jimin_on_Melon_Music_Awards_2016.jpg"},
            {"name": "엑소 백현", "img": "https://upload.wikimedia.org/wikipedia/commons/3/32/Baekhyun_at_a_fansign_on_July_12%2C_2019.jpg"}
        ]
    },
    "ESTP": {
        "tag": "🐆 수완 좋은 활동가",
        "desc": "스릴 넘치는 모험을 즐기며, 트렌디함의 끝판왕인 현실파!",
        "celebs": [
            {"name": "도널드 트럼프", "img": "https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait_2017.jpg"},
            {"name": "경리", "img": "https://upload.wikimedia.org/wikipedia/commons/3/38/Gyeongree_at_Seoul_Fashion_Week_on_October_17%2C_2018.jpg"},
            {"name": "효린", "img": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Hyolyn_at_a_fansign_on_July_27%2C_2018.jpg"}
        ]
    },
    "ESFP": {
        "tag": "🎉 자유로운 영혼의 연예인",
        "desc": "인생은 파티처럼! 흥이 넘쳐나고 주위에 웃음꽃을 피우는 인간 비타민!",
        "celebs": [
            {"name": "마릴린 먼로", "img": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Marilyn_Monroe_in_1952.jpg"},
            {"name": "가수 비", "img": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Rain_at_a_press_conference_for_Sketch_on_May_24%2C_2018.jpg"},
            {"name": "세븐틴 승관", "img": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Seungkwan_at_Incheon_Airport_on_September_16%2C_2019.jpg"}
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
    
    # 3열(Columns)로 쪼개서 세련된 프로필 배치하기 🚀
    cols = st.columns(3)
    for index, celeb in enumerate(info['celebs']):
        with cols[index]:
            # onerror에 이니셜 아바타 API를 넣어 인터넷 연결이 끊겨도 예쁜 아이콘이 뜨도록 설계함 🛠️
            st.markdown(f"""
                <div class='celeb-container'>
                    <img class='celeb-img' src='{celeb['img']}' 
                         onerror="this.onerror=null; this.src='https://api.dicebear.com/7.x/initials/svg?seed={celeb['name']}';">
                    <div class='celeb-name'>{celeb['name']}</div>
                </div>
            """, unsafe_allow_html=True)

# 7. 푸터 영역
st.write("")
st.write("---")
st.caption("🔥 당곡고 멋쟁이 개발자가 제작함 | Made with Streamlit 🚀")
