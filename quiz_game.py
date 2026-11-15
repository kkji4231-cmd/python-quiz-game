from quiz_data import get_default_quizzes


class QuizGame:
    def __init__(self):
        self.quizzes = get_default_quizzes()
        self.best_score = None

    def show_menu(self):
        print()
        print("=" * 40)
        print("       CNC · 품질 퀴즈 게임")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def get_menu_choice(self):
        while True:
            try:
                user_input = input("선택: ").strip()

                if not user_input:
                    print("⚠️ 입력값이 없습니다. 1~5 사이의 숫자를 입력하세요.")
                    continue

                choice = int(user_input)

                if 1 <= choice <= 5:
                    return choice

                print("⚠️ 1~5 사이의 숫자를 입력하세요.")

            except ValueError:
                print("⚠️ 숫자만 입력하세요.")

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_menu_choice()

            if choice == 1:
                print("퀴즈 풀기 기능은 다음 단계에서 구현합니다.")

            elif choice == 2:
                print("퀴즈 추가 기능은 다음 단계에서 구현합니다.")

            elif choice == 3:
                print("퀴즈 목록 기능은 다음 단계에서 구현합니다.")

            elif choice == 4:
                print("점수 확인 기능은 다음 단계에서 구현합니다.")

            elif choice == 5:
                print("퀴즈 게임을 종료합니다.")
                break