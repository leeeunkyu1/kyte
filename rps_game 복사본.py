import random


def rps_game():
    total_games = 0
    user_win = 0
    user_losing = 0
    Draw = 0

    while True:
        total_games += 1
        user_choices = input("가위, 바위, 보 중 하나만 입력하세요:")
        choices = ["가위", "바위", "보"]
        Ai_choices = random.choice(choices)

        if user_choices not in choices:
            print("잘못된 입력 입니다. 가위, 바위, 보 중 하나만 입력해주세요")
            continue

        print(f"당신의 선택은 {user_choices}입니다 ")
        print(f"AI의 선택은 {Ai_choices}입니다 ")

        if user_choices == Ai_choices:
            print("비겼습니다.")
            Draw += 1

        elif (user_choices == "가위" and Ai_choices == "보") or (user_choices == "바위" and Ai_choices == "가위") or (user_choices == "보" and Ai_choices == "바위"):
            print("당신이 이겼습니다")
            user_win += 1

        else:
            print("당신이 졌습니다")
            user_losing += 1

        if user_win >= 3 or user_losing >= 3:
            print("축하드립니다 완전히 이겨버렸습니다!")
            break

    # play_again = str(input("게임을 다시 하시겠습니까? (y/n):"))
    # if play_again.lower() != 'y':
    #     print("즐거운 승부였어요. 잘가요!")

        # 재시작 하는 문구를 출력하며 사용자에게 인풋으로 (y/n) 입력값 요구
        play_again = input("게임을 다시 하시겠습니까? (y/n):")
        if play_again.lower() != 'n':   # n이 아닌경우  다시 처음 와일문으로 돌아가 게임 스타트
            print(f"승:{user_win} 패:{user_losing} 무:{Draw}")
        elif play_again.lower() != 'y':  # y가 아닌경우 게임종료
            print("게임을 종료합니다.")
            break


if __name__ == "__main__":
    rps_game()


# 에러1 : 게임이 안끝남. == break가 안걸림  그래서 while 문을 한번 더 걸어줬는데 그것도 안됌. 다시 와일문 하나로 오류수정중.
# 에러2 : 시작할때 잘못된 입력 입니다. 라는 위에 프린트도 같이 출력됨.
# 에러3 : 변수지정을 각 이프 엘즈 문법 하나하나당에 카운팅 해줄수 있다는걸 완전히 이해함
# 에러1 : 와일문을 하나로 합치고 들여쓰기 다시해서 해결!

# 에러4 : 자꾸 게임이 단판으로 끝나고 y 로 재시작해도 게임이 종료됨;;;
# 에러 4: 조건문 문법 위치 수정
# 에러 5: 조건문 안에서 자꾸 브레이크가 걸려버림.
# 에러 5수정전:if user_win or user+losing >=:  수정후 if user_win >= 3 or user_losing >= 3:
# 에러 *: 이프문 수정후 승패무를 출력해주는 프린트문을 밑으로 빼고 업다운게임에 적용하듯 이프 엘리프로 n y 값 아닌경우를 다 줘버렸더니 해결.
