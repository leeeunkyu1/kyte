import random
#처음에 와일문을 한번만 주고 코드를 작성해서 게임이 끝나고 재시작을 안했다. 전체를 와일문으로 감싸주니 재시작 브레이크가 잘 걸렸다.
#처음에 게임을 할때마다 카운팅해주는 변수를 지정 안해주고 카운팅하려고 했다가 고생좀했다.
#

def guess_number_game():   # 랜덤게임함수모듈 
    while True:    # 첫번쨰 와일문 전체게임을 반복하기 위함
    
        answer = random.randint(1, 100)  #랜덤번호지정
        attempts = 0  #시도횟수를 0으로 셋팅

        while True:  #정답에 따른 게임반복문                  
            guess = int(input("1에서100까지의 숫자를 말해봐!$(15): "))  #플레이어로부터 입력값을 받기위함 그리고 입력받은 문자열을 숫자열로 변경
            attempts += 1     #시도횟수 카운팅
            
            
            
            if guess == answer:   # 정답일경우 
                if attempts <= 5:  #시도횟수가 5이하
                    print("오~ 촉 좋은데!? 귀신👻 잡겠어 정답🅾️")
                elif attempts <= 15: #시도횟수 15이하
                    print("잠들뻔 했네😪💤💤아무튼 정답🅾️")                   
                break  #정답일 경우 STOP
                
                
                
            elif guess > answer:   # 랜덤번호보다 입력값이 클경우
                print(f"down👎 ${attempts}")
            else: #아닐경우 = 랜덤번호보다 입력값이 작을경우
                print(f"up👍 ${attempts}")


            if attempts >= 15:  #시도횟수가 15번이상일 경우 정답을 알려주며 게임을 종료
                print(f"우우우우~~15 번의 기회 끝! 정답은 {answer}입니다!")
                break
                
                
        play_again = input("게임을 다시 하시겠습니까? (y/n):")   #재시작 하는 문구를 출력하며 사용자에게 인풋으로 (y/n) 입력값 요구 
        if play_again.lower() != 'n':   # n이 아닌경우  다시 처음 와일문으로 돌아가 게임 스타트     
            print(f"이전 최고 시도횟수${attempts}") 
        elif play_again.lower() != 'y': # y가 아닌경우 게임종료
            print("게임을 종료합니다.")
            break

if __name__ == "__main__":       # __main__ 은 이 스크립트가 독립적으로 실행될 때의 특별한 변수. 직접 실행될경우에는 __main__ 이 아니라 True로 설정됨.
    guess_number_game()


### 