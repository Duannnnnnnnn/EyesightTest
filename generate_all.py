import os
from scale_and_generate import generate_stages_from_base

# 預設參數
BASE_IMG_PATH = "assets/sign.png"      # 基準圖（缺口為 13px）
BASE_GAP_PX = 13                         # 基準圖實際缺口像素
PPM = 3.64                               # 螢幕像素密度 px/mm（MacBook Air）
DISTANCE_MM = 1000                       # 視力測試距離 1 公尺
OUTPUT_DIR = "scaled_signs"             # 輸出資料夾

# 建立 stage → logMAR 對照（stage 0~14）
stage_to_logmar = {i: 1.0 - i * 0.1 for i in range(15)}

if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generate_stages_from_base(
        base_path=BASE_IMG_PATH,
        base_gap_px=BASE_GAP_PX,
        ppm=PPM,
        distance_mm=DISTANCE_MM,
        stage_to_logmar=stage_to_logmar,
        output_dir=OUTPUT_DIR
    )
    print("✅ 所有 stage 視力圖已生成完畢！")
