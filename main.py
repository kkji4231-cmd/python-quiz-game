from quiz_data import get_default_quizzes


def main():
    quizzes = get_default_quizzes()

    print("=== 기본 퀴즈 목록 ===")
    print(f"총 퀴즈 수: {len(quizzes)}개")

    for index, quiz in enumerate(quizzes, start=1):
        print(f"{index}. {quiz.question}")


if __name__ == "__main__":
    main()