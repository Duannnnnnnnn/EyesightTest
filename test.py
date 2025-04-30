from measure_gap import measure_gap_width

gap_px = measure_gap_width("assets/sign.png", save_path="highlighted_gap.png")
print(f"缺口寬度為：{gap_px} px")
