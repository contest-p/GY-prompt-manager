import json  # JSON 파일 다루기 위한 모듈

# ========================================
# 프롬프트 관리 프로그램
# 작성자: [박경연]
# ========================================

# 기본 프롬프트 데이터 (파일이 없을 때 사용)
default_prompts = [
    {
        "title": "블로그 글 작성",
        "category": "글쓰기",
        "content": "다음 주제로 블로그 글을 작성해줘: [주제]. SEO를 고려하여 작성해줘.",
        "tags": ["블로그", "SEO", "글쓰기"],
        "favorite": False,
        "views": 0
    },
    {
        "title": "코드 리뷰 요청",
        "category": "코딩",
        "content": "다음 코드를 리뷰해줘. 개선점과 버그를 찾아줘:\n[코드]",
        "tags": ["코드리뷰", "개발"],
        "favorite": True,
        "views": 0
    },
    {
        "title": "영어 번역",
        "category": "번역",
        "content": "다음 문장을 자연스러운 영어로 번역해줘: [문장]",
        "tags": ["번역", "영어"],
        "favorite": False,
        "views": 0
    }
]
# 실제 사용할 prompts 변수 (main에서 채워질 예정)
prompts=[]

# ========================================
# 기능 함수들 (아직 뼈대만)
# ========================================

def add_prompt():
    """프롬프트 추가"""
    print("\n" + "=" * 40)
    print("📝 새 프롬프트 추가")
    print("=" * 40)

    # 사용자 입력 받기
    title = input("제목: ")
    category = input("카테고리 (예: 글쓰기/코딩/번역): ")
    content = input("내용: ")
    tags_input = input("태그 (쉼표로 구분, 예: 블로그,SEO): ")

    # 태그 처리: "블로그, SEO" → ["블로그", "SEO"]
    tags = [tag.strip() for tag in tags_input.split(",")]

    # 새 프롬프트 딕셔너리 만들기
    new_prompt = {
        "title": title,
        "category": category,
        "content": content,
        "tags": tags,
        "favorite": False,
        "views": 0
    }

    # 리스트에 추가
    prompts.append(new_prompt)

    print(f"\n✅ '{title}' 프롬프트가 추가되었습니다!")
    print(f"   현재 총 {len(prompts)}개의 프롬프트가 있습니다.")

def show_list():
    """전체 목록 조회"""
    print("\n" + "=" * 50)
    print("📋 전체 프롬프트 목록")
    print("=" * 50)

    # 프롬프트가 없을 때 처리
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다. 먼저 추가해주세요! 📝")
        return

    # 목록 출력
    for i, prompt in enumerate(prompts):
        # 즐겨찾기 표시
        star = "⭐" if prompt["favorite"] else "  "
        
        # 번호는 1부터 보이도록 (i+1)
        print(f"{star} {i+1}. [{prompt['category']}] {prompt['title']}")
        print(f"      태그: {', '.join(prompt['tags'])} | 조회수: {prompt['views']}")
    
    print("=" * 50)
    print(f"총 {len(prompts)}개의 프롬프트가 있습니다.")


def show_by_category():
    """카테고리별 조회"""
    print("\n" + "=" * 50)
    print("📂 카테고리별 조회")
    print("=" * 50)

    # 프롬프트가 없을 때 처리
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다. 먼저 추가해주세요! 📝")
        return

    # 존재하는 카테고리 목록 뽑기 (중복 제거)
    categories = set()
    for prompt in prompts:
        categories.add(prompt["category"])

    # 카테고리 목록 보여주기
    print("사용 가능한 카테고리:")
    for cat in categories:
        print(f"  - {cat}")
    print("=" * 50)

    # 사용자 입력
    selected = input("조회할 카테고리를 입력하세요: ").strip()

    # 필터링 & 출력
    print(f"\n📂 [{selected}] 카테고리 프롬프트")
    print("-" * 50)

    count = 0
    for i, prompt in enumerate(prompts):
        if prompt["category"] == selected:
            star = "⭐" if prompt["favorite"] else "  "
            print(f"{star} {i+1}. {prompt['title']}")
            print(f"      태그: {', '.join(prompt['tags'])} | 조회수: {prompt['views']}")
            count += 1

    # 결과 요약
    print("-" * 50)
    if count == 0:
        print(f"⚠️ '{selected}' 카테고리에 해당하는 프롬프트가 없습니다.")
    else:
        print(f"총 {count}개의 프롬프트를 찾았습니다.")


def search_prompt():
    """검색 (제목 또는 태그에서 키워드 검색)"""
    print("\n" + "=" * 50)
    print("🔎 프롬프트 검색")
    print("=" * 50)

    # 프롬프트가 없을 때 처리
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다. 먼저 추가해주세요! 📝")
        return

    # 사용자 입력
    keyword = input("검색할 키워드를 입력하세요: ").strip()

    # 빈 검색어 방어
    if keyword == "":
        print("⚠️ 검색어를 입력해주세요!")
        return

    # 대소문자 무시 검색을 위해 소문자로 변환
    keyword_lower = keyword.lower()

    # 검색 결과 출력
    print(f"\n🔎 '{keyword}' 검색 결과")
    print("-" * 50)

    count = 0
    for i, prompt in enumerate(prompts):
        # 제목에 있는지 확인 (대소문자 무시)
        in_title = keyword_lower in prompt["title"].lower()

        # 태그에 있는지 확인 (각 태그를 소문자로 만들어 비교)
        tags_lower = [tag.lower() for tag in prompt["tags"]]
        in_tags = any(keyword_lower in tag for tag in tags_lower)

        # 제목 or 태그에 있으면 출력
        if in_title or in_tags:
            star = "⭐" if prompt["favorite"] else "  "
            print(f"{star} {i+1}. [{prompt['category']}] {prompt['title']}")
            print(f"      태그: {', '.join(prompt['tags'])}")
            count += 1

    # 결과 요약
    print("-" * 50)
    if count == 0:
        print(f"⚠️ '{keyword}' 에 대한 검색 결과가 없습니다.")
    else:
        print(f"총 {count}개의 프롬프트를 찾았습니다.")


def show_detail():
    """상세 보기"""
    print("\n" + "=" * 50)
    print("🔍 프롬프트 상세 보기")
    print("=" * 50)

    # 프롬프트가 없을 때 처리
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다. 먼저 추가해주세요! 📝")
        return

    # 목록 간단히 보여주기 (사용자가 번호 고르도록)
    for i, prompt in enumerate(prompts):
        print(f"  {i+1}. {prompt['title']}")
    print("=" * 50)

    # 사용자 입력 (예외 처리 포함)
    try:
        number = int(input("상세 보기할 번호를 입력하세요: "))
    except ValueError:
        print("⚠️ 숫자만 입력해주세요!")
        return

    # 번호 범위 검증
    if number < 1 or number > len(prompts):
        print(f"⚠️ 1 ~ {len(prompts)} 사이의 번호를 입력해주세요!")
        return

    # 인덱스는 0부터 시작하므로 -1
    prompt = prompts[number - 1]

    # 조회수 증가!
    prompt["views"] += 1

    # 상세 정보 출력
    star = "⭐" if prompt["favorite"] else ""
    print("\n" + "=" * 50)
    print(f"📌 {prompt['title']} {star}")
    print("=" * 50)
    print(f"📂 카테고리: {prompt['category']}")
    print(f"🏷️  태그: {', '.join(prompt['tags'])}")
    print(f"👁️  조회수: {prompt['views']}")
    print("-" * 50)
    print("📝 내용:")
    print(prompt['content'])
    print("=" * 50)


def manage_favorite():
    """즐겨찾기 관리 (⭐ 추가/제거 토글)"""
    print("\n" + "=" * 50)
    print("⭐ 즐겨찾기 관리")
    print("=" * 50)

    # 프롬프트가 없을 때 처리
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다. 먼저 추가해주세요! 📝")
        return

    # 목록 보여주기 (현재 즐겨찾기 상태 표시)
    for i, prompt in enumerate(prompts):
        star = "⭐" if prompt["favorite"] else "  "
        print(f"{star} {i+1}. {prompt['title']}")
    print("=" * 50)

    # 사용자 입력 (예외 처리)
    try:
        number = int(input("즐겨찾기를 변경할 번호를 입력하세요: "))
    except ValueError:
        print("⚠️ 숫자만 입력해주세요!")
        return

    # 번호 범위 검증
    if number < 1 or number > len(prompts):
        print(f"⚠️ 1 ~ {len(prompts)} 사이의 번호를 입력해주세요!")
        return

    # 해당 프롬프트 선택
    prompt = prompts[number - 1]

    # 즐겨찾기 토글! (핵심 한 줄)
    prompt["favorite"] = not prompt["favorite"]

    # 결과 출력
    if prompt["favorite"]:
        print(f"\n✅ '{prompt['title']}' 이(가) 즐겨찾기에 추가되었습니다! ⭐")
    else:
        print(f"\n✅ '{prompt['title']}' 이(가) 즐겨찾기에서 제거되었습니다.")


def show_favorites():
    """즐겨찾기 목록 (⭐ 표시된 것만 보기)"""
    print("\n" + "=" * 50)
    print("💖 즐겨찾기 목록")
    print("=" * 50)

    # 프롬프트가 없을 때 처리
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다. 먼저 추가해주세요! 📝")
        return

    # 즐겨찾기만 필터링해서 출력
    count = 0
    for i, prompt in enumerate(prompts):
        if prompt["favorite"]:  # 즐겨찾기인 것만!
            print(f"⭐ {i+1}. [{prompt['category']}] {prompt['title']}")
            print(f"      태그: {', '.join(prompt['tags'])}")
            count += 1

    print("=" * 50)

    # 결과 요약
    if count == 0:
        print("💡 아직 즐겨찾기한 프롬프트가 없습니다.")
        print("   메뉴 6번(즐겨찾기 관리)에서 추가해보세요!")
    else:
        print(f"총 {count}개의 즐겨찾기 프롬프트가 있습니다. 💖")

def save_to_json():
    """프롬프트 데이터를 JSON 파일로 저장"""
    try:
        with open("prompts.json", "w", encoding="utf-8") as f:
            json.dump(prompts, f, ensure_ascii=False, indent=2)
        print(f"\n💾 데이터가 'prompts.json' 파일에 저장되었습니다! ({len(prompts)}개)")
    except Exception as e:
        print(f"\n⚠️ 저장 중 오류 발생: {e}")

def load_from_json():
    """JSON 파일에서 프롬프트 데이터를 불러옵니다."""
    try:
        with open('prompts.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"📂 '{len(data)}개'의 프롬프트를 불러왔습니다!")
        return data
    except FileNotFoundError:
        print("📁 저장된 파일이 없어 기본 데이터로 시작합니다.")
        return None
    except Exception as e:
        print(f"⚠️ 불러오기 중 오류 발생: {e}")
        return None
# ========================================
# 메뉴 시스템
# ========================================

def show_menu():
    """메뉴 출력"""
    print("\n" + "=" * 40)
    print("      🤖 프롬프트 관리 프로그램")
    print("=" * 40)
    print("1. 프롬프트 추가")
    print("2. 전체 목록 조회")
    print("3. 카테고리별 조회")
    print("4. 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    print("=" * 40)


def main():
    """메인 실행 함수"""
    global prompts  # 전역 변수 사용 선언
    
    # JSON 파일에서 데이터 불러오기
    loaded_data = load_from_json()
    if loaded_data is not None:
        prompts = loaded_data
    else:
        prompts = default_prompts

    print("프로그램을 시작합니다! 👋")

    while True:
        show_menu()
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            manage_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            save_to_json()  # 종료 전 자동 저장! 💾
            print("\n프로그램을 종료합니다. 안녕히 가세요! 👋")
            break
        else:
            print("\n⚠️ 잘못된 입력입니다. 다시 선택해주세요.")


# 프로그램 시작
if __name__ == "__main__":
    main()