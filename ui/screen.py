import cv2
import numpy as np
import os
import oled
from aiy.voice.audio import play_wav
class Screen:
    def __init__(self):
        self.width = 720
        self.height = 480
        self.center = (self.width // 2, self.height // 2)
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.radius_white = 150

    def get_scaled_rotated_sign(self, stage, direction):
        path = os.path.join("scaled_signs", f"stage_{stage}.png")
        img = cv2.imread(path)
        if img is None:
            print(f"[錯誤] 無法讀取圖卡：{path}")
            return None

        # 根據方向旋轉圖像
        if direction == 0:
            img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        elif direction == 2:
            img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        elif direction == 3:
            img = cv2.rotate(img, cv2.ROTATE_180)

        return img

    def show_prompt(self, stage, direction=None):
        screen = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        screen[:] = (0, 0, 0)

        # 畫中心白圈
        screen = cv2.circle(screen, self.center, self.radius_white, (255, 255, 255), -1)

        # 加入對應 stage 的 E 字圖
        if direction is not None:
            sign_img = self.get_scaled_rotated_sign(stage, direction)
            if sign_img is not None:
                h, w = sign_img.shape[:2]
                y1 = self.center[1] - h // 2
                y2 = y1 + h
                x1 = self.center[0] - w // 2
                x2 = x1 + w
                if 0 <= x1 and y1 >= 0 and y2 <= self.height and x2 <= self.width:
                    screen[y1:y2, x1:x2] = sign_img

        cv2.imshow("Eyesight Test", screen)
        cv2.waitKey(1)
    # def show_feedback(self, stage, direction, correct):
    #     pass  # 答題後不再顯示正確與否畫面

    def show_result(self, stage):
        from vision_math import logmar_to_decimal
        logmar = 1.0 - 0.1 * stage
        score = logmar_to_decimal(logmar)
        # oled.display_text(f"視力檢測結果:{score:.2f}")
        print("===== 測驗結果統計 =====")
        print(f"Decimal 視力（Stage {stage}）→ LogMAR {logmar:.2f} → Decimal {score:.2f}")
        try:
            from vision_math import logmar_to_decimal
            for i in range(15):
                logmar = 1.0 - 0.1 * i
                print(f"Stage {i:2d} → LogMAR {logmar:>4.1f} → Decimal {logmar_to_decimal(logmar):.2f}")
        except:
            print("[警告] 無法列出標準對照（缺 vision_math 模組）")
        print("======================")
        img = np.ones((self.height, self.width, 3), dtype=np.uint8) * 255
        text = f"Your result: {score:.2f}"
        text_size, _ = cv2.getTextSize(text, self.font, 2, 4)
        text_x = self.center[0] - text_size[0] // 2
        text_y = self.center[1] + text_size[1] // 2
        cv2.putText(img, text, (text_x, text_y), self.font, 2, (0, 0, 0), 4)
        cv2.imshow("Eyesight Test", img)
        if score >= 1.0 :
            play_wav("MVP.wav")
        else :
            play_wav("tellme.wav")
        oled.display_text(f"視力檢測結果:{score:.2f}")
        # if score >= 1.0 :
        #     play_wav("MVP.wav")
        # else :
        #     play_wav("回答我.wav")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
        play_wav("MVP.wav")
