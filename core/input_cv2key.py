import cv2

class CV2KeyInput:
    def __init__(self):
        self.key_map = {
            0 : None,   #上
            1 : None,   #右
            2 : None,   #下
            3 : None    #左
        }
        # print("請按 ↑ → ↓ ← esc 校正")
        # self.keyboard_correction()

    # def get_direction(self):
    #     print("[輸入] 請在畫面中按 ↑ ↓ ← → 鍵選擇方向")
    #     while True:
    #         key = cv2.waitKeyEx(0)
    #         print(f"[DEBUG] 按鍵 keycode = {key}")
    #         if key == self.key_map[4]:
    #             print("[系統] 按下 ESC，結束測試")
    #             exit()
    #         for i in self.key_map:
    #             if self.key_map[i] == key :
    #                 return i
    #         print(f"[無效鍵碼] key={key}")
    
    # def keyboard_correction(self):
    #     cv2.namedWindow('calib')
    #     for i in range(5):
    #         self.key_map[i]=cv2.waitKeyEx(0)
    #         print(self.key_map[i])
    #     cv2.destroyWindow('calib')
