# ========================================
# 프롬프트 관리 프로그램
# 작성자: [박경연]
# ========================================

# 프롬프트 데이터 (리스트 안에 딕셔너리)
prompts = [
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
    """검색"""
    print("\n🔍 [검색] 기능 - 준비 중입니다.")


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
    """즐겨찾기 관리"""
    print("\n⭐ [즐겨찾기 관리] 기능 - 준비 중입니다.")


def show_favorites():
    """즐겨찾기 목록"""
    print("\n💖 [즐겨찾기 목록] 기능 - 준비 중입니다.")


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
            print("\n프로그램을 종료합니다. 안녕히 가세요! 👋")
            break
        else:
            print("\n⚠️ 잘못된 입력입니다. 다시 선택해주세요.")


# 프로그램 시작
if __name__ == "__main__":
    main()