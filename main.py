import streamlit as st
import urllib.parse

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="✨ MBTI Star Finder ✨",
    page_icon="🌙",
    layout="centered"
)

# 2. 🌌 밤하늘 감성 커스텀 스타일링 (별이 반짝이는 우주 무드!)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');
    
    /* 🌃 전체 배경: 깊은 밤하늘 그라데이션 */
    .stApp {
        background: linear-gradient(180deg, #0a0a2e 0%, #16213e 50%, #1a1a3e 100%);
        background-attachment: fixed;
    }
    
    /* ⭐ 반짝이는 별 효과 (CSS로 별 만들기!) */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, #ffffff, transparent),
            radial-gradient(2px 2px at 40px 70px, #ffffff, transparent),
            radial-gradient(1px 1px at 50px 160px, #ffffff, transparent),
            radial-gradient(1px 1px at 90px 40px, #ffffff, transparent),
            radial-gradient(2px 2px at 130px 80px, #ffffff, transparent),
            radial-gradient(1px 1px at 160px 120px, #ffffff, transparent),
            radial-gradient(2px 2px at 200px 50px, #fff4e6, transparent),
            radial-gradient(1px 1px at 250px 100px, #ffffff, transparent),
            radial-gradient(2px 2px at 300px 30px, #e6f0ff, transparent);
        background-size: 350px 200px;
        background-repeat: repeat;
        opacity: 0.6;
        animation: twinkle 5s ease-in-out infinite alternate;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes twinkle {
        0% { opacity: 0.3; }
        100% { opacity: 0.8; }
    }
    
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
        color: #ffffff;
    }
    
    /* 🌠 메인 타이틀: 별빛 그라데이션 */
    .main-title {
        font-size: 3rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #c9a8ff 0%, #ffd5e8 50%, #a8d8ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        text-shadow: 0 0 30px rgba(201, 168, 255, 0.3);
        position: relative;
        z-index: 1;
    }
    .sub-title {
        font-size: 1.1rem;
        text-align: center;
        color: #b8b8d4;
        margin-bottom: 30px;
        position: relative;
        z-index: 1;
    }
    
    /* 💫 MBTI 설명 카드: 우주 글래스모피즘 */
    .card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(201, 168, 255, 0.3);
        box-shadow: 0 8px 32px rgba(138, 43, 226, 0.2);
        margin-bottom: 25px;
        position: relative;
        z-index: 1;
    }
    .badge {
        background: linear-gradient(135deg, #c9a8ff 0%, #8b5cf6 100%);
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
    }
    
    /* ⭐ 유명인 카드: 별빛 글로우 효과 */
    .celeb-container {
        text-align: center;
        padding: 18px;
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(8px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 20px rgba(138, 43, 226, 0.15);
        margin-bottom: 20px;
        transition: all 0.3s ease-in-out;
        position: relative;
        z-index: 1;
    }
    .celeb-container:hover {
        transform: translateY(-8px);
        box-shadow: 0 8px 30px rgba(201, 168, 255, 0.4);
        border: 1px solid rgba(201, 168, 255, 0.5);
    }
    .celeb-img {
        border-radius: 50%;
        width: 130px;
        height: 130px;
        object-fit: cover;
        border: 3px solid #c9a8ff;
        box-shadow: 0 0 25px rgba(201, 168, 255, 0.6);
    }
    .celeb-name {
        font-weight: 900;
        font-size: 1.1rem;
        color: #ffffff;
        margin-top: 12px;
        text-shadow: 0 0 10px rgba(201, 168, 255, 0.5);
    }
    
    /* 🪐 셀렉트박스 다크모드 스타일 */
    .stSelectbox label {
        color: #c9a8ff !important;
        font-weight: bold;
    }
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.08) !important;
        color: white !important;
        border: 1px solid rgba(201, 168, 255, 0.4) !important;
    }
    
    /* 일반 텍스트 색상 */
    h1, h2, h3, h4, h5, h6, p {
        color: #ffffff !important;
        position: relative;
        z-index: 1;
    }
    .stCaption, [data-testid="stCaptionContainer"] {
        color: #8888aa !important;
    }
    hr {
        border-color: rgba(201, 168, 255, 0.2) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 💡 이미지 깨짐 완벽 방지! 프록시 서버 활용 함수
def get_safe_image_url(raw_url):
    encoded_url = urllib.parse.quote(raw_url, safe=':/')
    return f"https://images.weserv.nl/?url={encoded_url}&w=300&h=300&fit=cover"

# 3. MBTI 데이터 세팅 (실제 유명인 이미지!)
mbti_data = {
    "INTJ": {
        "tag": "🐉 용의주도한 전략가",
        "desc": "이성적이면서도 두뇌 회전이 빠른 스마트 마인드의 소유자!",
        "celebs": [
            {"name": "손흥민", "img": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Son_Heung-Min.jpg"},
            {"name": "에스파 카리나", "img": "https://upload.wikimedia.org/wikipedia/commons/0/07/Aespa_Karina_231111_Mini_Fanmeeting_01.png"},
            {"name": "마크 저커버그", "img": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Mark_Zuckerberg.jpg"}
        ]
    },
    "INTP": {
        "tag": "💡 논리적인 사색가",
        "desc": "호기심 천국에 늘 새로운 아이디어를 갈망하는 분석가!",
        "celebs": [
            {"name": "기안84", "img": "https://upload.wikimedia.org/wikipedia/commons/2/21/Gian84_in_2023.jpg"},
            {"name": "빌 게이츠", "img": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Bill_Gates_2017_%28cropped%29.jpg"},
            {"name": "방탄소년단 진", "img": "https://upload.wikimedia.org/wikipedia/commons/1/10/Jin_at_a_press_conference_for_the_BBMAs_on_May_29%2C_2017.png"}
        ]
    },
    "ENTJ": {
        "tag": "👑 대담한 지도자",
        "desc": "비전을 가지고 남들을 이끄는 천생 보스형 캐릭터!",
        "celebs": [
            {"name": "스티브 잡스", "img": "https://upload.wikimedia.org/wikipedia/commons/b/b9/Steve_Jobs_Headshot_2010-CROP.jpg"},
            {"name": "백종원", "img": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Paik_Jong-won_in_November_2019.png"},
            {"name": "고든 램지", "img": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Gordon_Ramsay_at_the_2017_VEGAS_UNCORK%27D_%28cropped%29.jpg"}
        ]
    },
    "ENTP": {
        "tag": "🔥 뜨거운 논쟁을 즐기는 변론가",
        "desc": "지적 호기심이 폭발하는, 룰 브레이커이자 트렌드 세터!",
        "celebs": [
            {"name": "버락 오바마", "img": "https://upload.wikimedia.org/wikipedia/commons/8/8d/President_Barack_Obama.jpg"},
            {"name": "육성재", "img": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Yook_Sung-jae_at_a_fansign_on_June_25%2C_2022.jpg"},
            {"name": "한예슬", "img": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Han_Ye-seul_on_October_17%2C_2019.png"}
        ]
    },
    "INFJ": {
        "tag": "🔮 선의의 옹호자",
        "desc": "조용하고 신비로우며 샘솟는 영감으로 가득 찬 예술가!",
        "celebs": [
            {"name": "아이유", "img": "https://upload.wikimedia.org/wikipedia/commons/a/a8/IU_at_a_fansign_event_in_Sinchon_on_December_2019.jpg"},
            {"name": "차은우", "img": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Cha_Eun-woo_for_Marie_Claire_Korea_on_February_2022.jpg"},
            {"name": "소녀시대 태연", "img": "https://upload.wikimedia.org/wikipedia/commons/2/25/Taeyeon_at_the_SM_Town_Live_2022.jpg"}
        ]
    },
    "INFP": {
        "tag": "🦄 열정적인 중재자",
        "desc": "공감 능력 만렙! 마음이 따뜻하고 낭만이 넘치는 힐러!",
        "celebs": [
            {"name": "방탄소년단 정국", "img": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Jungkook_on_Melon_Music_Awards_2019.jpg"},
            {"name": "백예린", "img": "https://upload.wikimedia.org/wikipedia/commons/7/73/Yerin_Baek_in_2016.jpg"},
            {"name": "셰익스피어", "img": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Shakespeare.jpg"}
        ]
    },
    "ENFJ": {
        "tag": "🤝 정의로운 사회운동가",
        "desc": "넘치는 카리스마와 온화함으로 사람들을 사로잡는 인싸!",
        "celebs": [
            {"name": "유재석", "img": "https://upload.wikimedia.org/wikipedia/commons/6/69/Yoo_Jae-suk.jpg"},
            {"name": "오프라 윈프리", "img": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Oprah_Winfrey_at_the_Golden_Globes_2018.jpg"},
            {"name": "임시완", "img": "https://upload.wikimedia.org/wikipedia/commons/8/84/Yim_Si-wan_at_the_MBC_Drama_Awards_on_December_30%2C_2017.jpg"}
        ]
    },
    "ENFP": {
        "tag": "🎈 재기발랄한 활동가",
        "desc": "긍정에너지 뿜뿜! 어디서든 분위기를 메이킹하는 자유로운 영혼!",
        "celebs": [
            {"name": "방탄소년단 뷔", "img": "https://upload.wikimedia.org/wikipedia/commons/7/7c/V_on_Melon_Music_Awards_2019.jpg"},
            {"name": "이효리", "img": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Lee_Hyo-ri_at_an_event_on_October_24%2C_2013.jpg"},
            {"name": "로버트 다우니 주니어", "img": "https://upload.wikimedia.org/wikipedia/commons/9/94/Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg"}
        ]
    },
    "ISTJ": {
        "tag": "📏 청렴결백한 논리주의자",
        "desc": "약속은 칼같이! 매사에 꼼꼼하고 믿음직한 정석 그 자체!",
        "celebs": [
            {"name": "워런 버핏", "img": "https://upload.wikimedia.org/wikipedia/commons/5/51/Warren_Buffett_KU_Visit.jpg"},
            {"name": "남궁민", "img": "https://upload.wikimedia.org/wikipedia/commons/4/41/Namkoong_Min_at_the_KBS_Drama_Awards_on_December_31%2C_2017.jpg"},
            {"name": "소녀시대 써니", "img": "https://upload.wikimedia.org/wikipedia/commons/6/66/Sunny_at_the_Golden_Disc_Awards_on_January_15%2C_2014.jpg"}
        ]
    },
    "ISFJ": {
        "tag": "🛡️ 용감한 수호자",
        "desc": "소중한 사람들을 조용히, 하지만 확실하게 지키는 수호천사!",
        "celebs": [
            {"name": "비욘세", "img": "https://upload.wikimedia.org/wikipedia/commons/0/04/Beyonc%C3%A9_at_the_2018_Wearable_Art_Gala_%28cropped%29.jpg"},
            {"name": "장도연", "img": "https://upload.wikimedia.org/wikipedia/commons/1/19/Jang_Do-yeon_in_2018.jpg"},
            {"name": "최강창민", "img": "https://upload.wikimedia.org/wikipedia/commons/0/00/Changmin_at_Incheon_International_Airport_on_August_17%2C_2017.jpg"}
        ]
    },
    "ESTJ": {
        "tag": "💼 엄격한 관리자",
        "desc": "체계적이고 현실적인 일 처리 능력을 자랑하는 든든한 조력자!",
        "celebs": [
            {"name": "헨리 포드", "img": "https://upload.wikimedia.org/wikipedia/commons/1/18/Henry_ford_1919.jpg"},
            {"name": "뉴진스 민지", "img": "https://upload.wikimedia.org/wikipedia/commons/e/e6/NewJeans_Minji_Shinhan_Sol.jpg"},
            {"name": "김구라", "img": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Kim_Gu-ra_in_2016.jpg"}
        ]
    },
    "ESFJ": {
        "tag": "🍰 사교적인 외교관",
        "desc": "친절하고 사근사근하며 주변 사람을 살뜰히 챙기는 따뜻함!",
        "celebs": [
            {"name": "테일러 스위프트", "img": "https://upload.wikimedia.org/wikipedia/commons/d/db/Taylor_Swift_at_the_2019_American_Music_Awards_%28cropped%29.jpg"},
            {"name": "아이브 장원영", "img": "https://upload.wikimedia.org/wikipedia/commons/9/94/Jang_Won-young_at_the_AAA_2022.jpg"},
            {"name": "박보검", "img": "https://upload.wikimedia.org/wikipedia/commons/c/c6/Park_Bo-gum_at_the_KBS_Drama_Awards_on_December_31%2C_2016.jpg"}
        ]
    },
    "ISTP": {
        "tag": "🛠️ 만능 재주꾼",
        "desc": "말보다는 행동! 과묵하지만 도구를 다루는 데 천부적인 쿨가이!",
        "celebs": [
            {"name": "톰 크루즈", "img": "https://upload.wikimedia.org/wikipedia/commons/3/33/Tom_Cruise_by_Gage_Skidmore_2.jpg"},
            {"name": "박명수", "img": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Park_Myeong-su_in_2018.jpg"},
            {"name": "르세라핌 김채원", "img": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Kim_Chae-won_at_the_2022_MMA.jpg"}
        ]
    },
    "ISFP": {
        "tag": "🎨 호기심 많은 예술가",
        "desc": "따뜻하고 온화하며 삶의 모든 순간을 예술처럼 즐기는 사람!",
        "celebs": [
            {"name": "마이클 잭슨", "img": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Michael_Jackson_in_1984.jpg"},
            {"name": "방탄소년단 지민", "img": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Jimin_on_Melon_Music_Awards_2016.jpg"},
            {"name": "엑소 백현", "img": "https://upload.wikimedia.org/wikipedia/commons/5/51/Baekhyun_at_a_fansign_on_July_12%2C_2019.jpg"}
        ]
    },
    "ESTP": {
        "tag": "🐆 수완 좋은 활동가",
        "desc": "스릴 넘치는 모험을 즐기며, 트렌디함의 끝판왕인 현실파!",
        "celebs": [
            {"name": "도널드 트럼프", "img": "https://upload.wikimedia.org/wikipedia/commons/8/87/Donald_Trump_official_portrait_2017.jpg"},
            {"name": "경리", "img": "https://upload.wikimedia.org/wikipedia/commons/f/f9/Gyeongree_at_Seoul_Fashion_Week_on_October_17%2C_2018.jpg"},
            {"name": "효린", "img": "https://upload.wikimedia.org/wikipedia/commons/9/95/Hyolyn_at_a_fansign_on_July_27%2C_2018.jpg"}
        ]
    },
    "ESFP": {
        "tag": "🎉 자유로운 영혼의 연예인",
        "desc": "인생은 파티처럼! 흥이 넘쳐나고 주위에 웃음꽃을 피우는 인간 비타민!",
        "celebs": [
            {"name": "마릴린 먼로", "img": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Marilyn_Monroe_in_1952.jpg"},
            {"name": "가수 비", "img": "https://upload.wikimedia.org/wikipedia/commons/d/d2/Rain_at_a_press_conference_for_Sketch_on_May_24%2C_2018.jpg"},
            {"name": "세븐틴 승관", "img": "https://upload.wikimedia.org/wikipedia/commons/7/73/Seungkwan_at_Incheon_Airport_on_September_16%2C_2019.jpg"}
        ]
    }
}

# 4. 헤더 영역
st.markdown("<div class='main-title'>🌙 MBTI Star Finder ✨</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>밤하늘의 별처럼 빛나는, 나랑 같은 MBTI 셀럽은 누굴까? 🌌</div>", unsafe_allow_html=True)

# 5. MBTI 선택 셀렉트박스
st.write("---")
selected_mbti = st.selectbox(
    "🌠 너의 MBTI 별자리를 선택해봐!",
    options=list(mbti_data.keys()),
    index=0
)

# 6. 결과 화면 보여주기
if selected_mbti:
    info = mbti_data[selected_mbti]
    
    st.write("")
    
    # 트렌디한 카드 레이아웃 적용
    st.markdown(f"""
        <div class='card'>
            <span class='badge'>{selected_mbti}</span>
            <h3 style='margin: 5px 0 10px 0; color: #ffffff;'>{info['tag']}</h3>
            <p style='color: #d8d8ec; font-size: 0.95rem; line-height: 1.6;'>"{info['desc']}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 같은 MBTI를 가진 유명인들 보여주기
    st.markdown("#### ⭐ 같은 별자리 셀럽 발견! 🔭")
    
    # 3열로 깔끔하게 배치
    cols = st.columns(3)
    for index, celeb in enumerate(info['celebs']):
        with cols[index]:
            safe_url = get_safe_image_url(celeb['img'])
            st.markdown(f"""
                <div class="celeb-container">
                    <img class="celeb-img" src="{safe_url}" 
                         onerror="this.onerror=null; this.src='https://api.dicebear.com/7.x/initials/svg?seed={celeb['name']}';">
                    <div class="celeb-name">{celeb['name']}</div>
                </div>
            """, unsafe_allow_html=True)

# 7. 푸터 영역
st.write("")
st.write("---")
st.caption("🌙 당곡고 멋쟁이 개발자가 제작함 | Made with Streamlit ✨")
