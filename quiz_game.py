import json

from quiz import Quiz
from quiz_data import get_default_quizzes


class QuizGame:
    def __init__(self):
        self.state_file = "state.json"
        self.quizzes = []
        self.best_score = None
        self.load_state()

    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score
        }

        try:
            with open(self.state_file, "w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

        except OSError as error:
            print(f"⚠️ 데이터 저장 중 오류가 발생했습니다: {error}")

    def load_state(self):
        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.quizzes = [
                Quiz.from_dict(quiz_data)
                for quiz_data in data.get("quizzes", [])
            ]

            self.best_score = data.get("best_score")

            print(
                f"📂 저장된 데이터를 불러왔습니다. "
                f"(퀴즈 {len(self.quizzes)}개)"
            )

        except FileNotFoundError:
            self.quizzes = get_default_quizzes()
            self.best_score = None
            self.save_state()

            print("📂 첫 실행입니다. 기본 퀴즈 데이터를 생성했습니다.")

        except (json.JSONDecodeError, KeyError, TypeError) as error:
            print(f"⚠️ 저장 파일이 손상되었습니다: {error}")
            print("기본 데이터로 복구합니다.")

            self.quizzes = get_default_quizzes()
            self.best_score = None
            self.save_state()

        except OSError as error:
            print(f"⚠️ 데이터 파일을 읽을 수 없습니다: {error}")

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

        if self.best_score is None or percentage > self.best_score:
            self.best_score = percentage
            self.save_state()
            print("🎉 새로운 최고 점수입니다!")

        print("=" * 40)

    def add_quiz(self):
        print()
        print("📌 새로운 퀴즈를 추가합니다.")

        while True:
            question = input("문제를 입력하세요: ").strip()

            if question:
                break

            print("⚠️ 문제를 입력하세요.")

        choices = []

        for index in range(1, 5):
            while True:
                choice = input(f"선택지 {index}: ").strip()

                if choice:
                    choices.append(choice)
                    break

                print("⚠️ 선택지를 입력하세요.")

        while True:
            try:
                answer_input = input("정답 번호 (1-4): ").strip()

                if not answer_input:
                    print("⚠️ 정답 번호를 입력하세요.")
                    continue

                answer = int(answer_input)

                if 1 <= answer <= 4:
                    break

                print("⚠️ 1~4 사이의 숫자를 입력하세요.")

            except ValueError:
                print("⚠️ 숫자만 입력하세요.")

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_state()

        print()
        print("✅ 퀴즈가 추가되었습니다!")
        print(f"현재 등록된 퀴즈: {len(self.quizzes)}개")

    def show_quiz_list(self):
        print()
        print("📋 등록된 퀴즈 목록")

        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"총 {len(self.quizzes)}개의 퀴즈가 등록되어 있습니다.")
        print("-" * 40)

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")

        print("-" * 40)

    def show_score(self):
        print()
        print("🏆 최고 점수 확인")

        if self.best_score is None:
            print("아직 퀴즈를 플레이하지 않았습니다.")
            return

        print(f"현재 최고 점수: {self.best_score}점")

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_menu_choice()

            if choice == 1:
                self.play_quiz()

            elif choice == 2:
                self.add_quiz()

            elif choice == 3:
                self.show_quiz_list()

            elif choice == 4:
                self.show_score()

            elif choice == 5:
                self.save_state()
                print("퀴즈 게임을 종료합니다.")
                break