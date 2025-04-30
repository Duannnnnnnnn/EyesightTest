import cv2
import numpy as np
import csv
from vision_math import get_gap_px_from_logmar, logmar_to_decimal


def scale_sign_image(base_path, base_gap_px, target_logmar, ppm, distance_mm, save_path):
    # 計算目標缺口像素
    target_gap_px = get_gap_px_from_logmar(target_logmar, distance_mm, ppm)
    scale_ratio = target_gap_px / base_gap_px

    # 載入原圖並縮放
    base_img = cv2.imread(base_path)
    if base_img is None:
        print("[錯誤] 無法讀取基準圖")
        return False, target_gap_px

    h, w = base_img.shape[:2]
    new_w = int(w * scale_ratio)
    new_h = int(h * scale_ratio)

    if new_w <= 0 or new_h <= 0:
        print(f"[跳過] logMAR {target_logmar:.2f} 對應圖像太小（{new_w}x{new_h}），已略過")
        return False, target_gap_px

    resized = cv2.resize(base_img, (new_w, new_h), interpolation=cv2.INTER_AREA)
    cv2.imwrite(save_path, resized)
    print(f"[完成] 已產出縮放後圖檔：{save_path}")
    return True, target_gap_px


def generate_stages_from_base(base_path, base_gap_px, ppm, distance_mm, stage_to_logmar, output_dir):
    rows = [("stage", "logMAR", "decimal", "gap_px", "filename")]

    for stage, logmar in stage_to_logmar.items():
        save_path = f"{output_dir}/stage_{stage}.png"
        success, gap_px = scale_sign_image(base_path, base_gap_px, logmar, ppm, distance_mm, save_path)
        if success:
            decimal = logmar_to_decimal(logmar)
            rows.append((stage, round(logmar, 2), decimal, round(gap_px, 2), save_path))

    # 寫入報表
    csv_path = f"{output_dir}/stage_summary.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"📄 已產出報表：{csv_path}")
