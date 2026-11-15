from quiz_game import QuizGame


def main():
    game = QuizGame()

    try:
        game.run()

    except KeyboardInterrupt:
        print()
        print("⚠️ Ctrl+C가 입력되었습니다.")
        print("데이터를 저장하고 안전하게 종료합니다.")
        game.save_state()

    except EOFError:
        print()
        print("⚠️ 입력 스트림이 종료되었습니다.")
        print("데이터를 저장하고 안전하게 종료합니다.")
        game.save_state()


if __name__ == "__main__":
    main()