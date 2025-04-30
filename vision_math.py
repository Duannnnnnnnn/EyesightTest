import math

# 計算 logMAR 值對應的缺口視角（rad）
def logmar_to_angle(logmar):
    return 10 ** logmar

# 給定距離與 logMAR，反推應顯示的缺口實體寬度（mm）
def get_gap_mm_from_logmar(logmar, distance_mm):
    angle_rad = logmar_to_angle(logmar)
    gap_mm = math.tan(angle_rad) * distance_mm
    return gap_mm

# 根據 logMAR、距離與 ppm，計算應顯示幾像素

def get_gap_px_from_logmar(logmar, distance_mm, ppm):
    # 標準視角：5 分角 = 0.001454 rad
    theta = 0.001454 * (10 ** logmar)
    gap_mm = math.tan(theta) * distance_mm
    return gap_mm * ppm

# 已知 gap 實體寬度（mm）與距離，反推 logMAR 視力值
def estimate_logmar_from_gap_mm(gap_mm, distance_mm):
    angle_rad = math.atan(gap_mm / distance_mm)
    return math.log10(angle_rad)

# 已知 gap pixel + ppm + 距離，反推 logMAR
def estimate_logmar_from_gap(gap_px, ppm, distance_mm):
    gap_mm = gap_px / ppm
    return estimate_logmar_from_gap_mm(gap_mm, distance_mm)

# 可選：轉換 logMAR → decimal 視力值
def logmar_to_decimal(logmar):
    return round(10 ** (-logmar), 2)
