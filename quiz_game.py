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
    def get_answer(self):
        while True:
            try:
                user_input = input("정답 입력 (1-4): ").strip()

                if not user_input:
                    print("⚠️ 정답을 입력하세요.")
                    continue

                answer = int(user_input)

                if 1 <= answer <= 4:
                    return answer

                print("⚠️ 1~4 사이의 숫자를 입력하세요.")

            except ValueError:
                print("⚠️ 숫자만 입력하세요.")

    def play_quiz(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print()
        print(f"📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")

        score = 0

        for index, quiz in enumerate(self.quizzes, start=1):
            print()
            print("-" * 40)
            print(f"[문제 {index}]")

            quiz.display()

            user_answer = self.get_answer()

            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

        percentage = int((score / len(self.quizzes)) * 100)

        print()
        print("=" * 40)
        print(
            f"🏆 결과: {len(self.quizzes)}문제 중 "
            f"{score}문제 정답! ({percentage}점)"
        )
        print("=" * 40)
    def run(self):
        while True:
            self.show_menu()
            choice = self.get_menu_choice()

            if choice == 1:
                self.play_quiz()

            elif choice == 2:
                print("퀴즈 추가 기능은 다음 단계에서 구현합니다.")

            elif choice == 3:
                print("퀴즈 목록 기능은 다음 단계에서 구현합니다.")

            elif choice == 4:
                print("점수 확인 기능은 다음 단계에서 구현합니다.")

            elif choice == 5:
                print("퀴즈 게임을 종료합니다.")
                break