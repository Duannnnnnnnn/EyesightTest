def get_monitor_ppm():
    try:
        width_px = int(input("請輸入螢幕解析度寬度（px）: "))
        width_mm = float(input("請輸入螢幕實體寬度（mm）: "))
        ppm = width_px / width_mm
        print(f"[系統] 計算結果：螢幕像素密度為 {ppm:.2f} px/mm")
        return ppm
    except Exception as e:
        print("[錯誤] 輸入格式錯誤：", e)
        return None
