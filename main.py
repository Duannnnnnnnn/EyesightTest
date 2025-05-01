import time
from core.session import Session
from core.input_cv2key import CV2KeyInput
from ui.screen import Screen
import mi2s_asr as asr
if __name__ == '__main__':
    print("[系統] 視力測試開始")

    input_module = CV2KeyInput()
    session = Session(input_module=input_module)
    screen = Screen()
    recorder = asr.Recorder()
    dict = {
        "向上" : 0,
        "向右" : 1,
        "向下" : 2,
        "向左" : 3
    }
    while not session.finished:
        session.update()
        screen.show_prompt(stage=session.stage, direction=session.sign_direction)
        recorder.record()
        sentence = asr.main()
        direction = -1
        for i in dict :
            if i == sentence :
                direction = dict[i]
        print(direction)
        #direction = input_module.get_direction()  # 👈 等待使用者按 ↑ → ↓ ← 鍵
        session.answer(direction)                 # 👈 傳入使用者的方向來判斷對錯
        # print(f"[DEBUG] stage={session.stage}, direction={session.sign_direction}, user_input={direction}, result={'✔' if direction == session.sign_direction else '✘'}")

        #screen.show_feedback(session.stage, session.sign_direction, session.last_correct)

        time.sleep(1)


    screen.show_result(session.stage)
    print("[系統] 測試結束")
