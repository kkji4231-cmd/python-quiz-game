from quiz import Quiz


def get_default_quizzes():
    return [
        Quiz(
            "CNC의 의미는 무엇인가?",
            [
                "Computer Numerical Control",
                "Central Network Controller",
                "Computer Network Code",
                "Control Number Computer"
            ],
            1
        ),
        Quiz(
            "MCT에서 주로 절삭공구를 회전시키는 장치는 무엇인가?",
            [
                "테이블",
                "주축(Spindle)",
                "칩 컨베이어",
                "ATC 매거진"
            ],
            2
        ),
        Quiz(
            "공작기계에서 백래시(Backlash)의 의미로 가장 적절한 것은?",
            [
                "주축의 회전 속도",
                "이송 방향 전환 시 발생하는 기계적 유격",
                "절삭유의 압력",
                "공구의 수명"
            ],
            2
        ),
        Quiz(
            "가공품의 치수와 형상을 정밀하게 측정하는 장비는?",
            [
                "CMM",
                "ATC",
                "APC",
                "PLC"
            ],
            1
        ),
        Quiz(
            "품질관리에서 불량의 근본 원인을 찾는 활동과 가장 관련 있는 것은?",
            [
                "Root Cause Analysis",
                "Port Mapping",
                "Version Control",
                "Container Build"
            ],
            1
        )
    ]
