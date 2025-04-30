import cv2
import numpy as np


def measure_gap_width(image_path, save_path=None, visualize=True):
    img = cv2.imread(image_path)
    if img is None:
        print("[錯誤] 無法讀取圖片")
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 自動判斷是否需要反轉（二值化後白底應該是背景）
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    white_pct = np.mean(binary == 255)
    if white_pct < 0.5:
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    h, w = binary.shape

    # 缺口寬度 = 高度 / 5（根據標準 E 視力圖）
    gap_width_px = h // 5

    if visualize:
        highlight_img = img.copy()
        center_y = h // 2
        y1 = center_y - 5
        y2 = center_y + 5
        x1 = (w - gap_width_px) // 2
        x2 = x1 + gap_width_px

        cv2.rectangle(highlight_img, (x1, y1), (x2, y2), (0, 0, 255), 1)
        cv2.line(highlight_img, (0, center_y), (w - 1, center_y), (0, 255, 0), 1)

        if save_path:
            cv2.imwrite(save_path, highlight_img)
        else:
            cv2.imshow("Gap Highlight", highlight_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    return gap_width_px
