from quiz import Quiz


def main():
    quiz = Quiz(
        "CNC의 의미는 무엇인가?",
        [
            "Computer Numerical Control",
            "Central Network Controller",
            "Computer Network Code",
            "Control Number Computer"
        ],
        1
    )

    quiz.display()

    print()
    print("정답 확인 테스트")
    print(quiz.check_answer(1))


if __name__ == "__main__":
    main()