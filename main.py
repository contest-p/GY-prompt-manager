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
    print("\n📝 [프롬프트 추가] 기능 - 준비 중입니다.")


def show_list():
    """전체 목록 조회"""
    print("\n📋 [전체 목록 조회] 기능 - 준비 중입니다.")


def show_by_category():
    """카테고리별 조회"""
    print("\n📂 [카테고리별 조회] 기능 - 준비 중입니다.")


def search_prompt():
    """검색"""
    print("\n🔍 [검색] 기능 - 준비 중입니다.")


def show_detail():
    """상세 보기"""
    print("\n📖 [상세 보기] 기능 - 준비 중입니다.")


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