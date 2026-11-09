import matplotlib.pyplot as plt
import pandas as pd


def plot_hplc_chromatogram(csv_file):
  # Đọc dữ liệu sắc ký từ file CSV (Thời gian lưu vs Cường độ hấp thụ)
  data = pd.read_csv(csv_file)
  plt.figure(figsize=(8, 4))
  plt.plot(data['Retention_Time'], data['Intensity'], color='blue')
  plt.title('HPLC Chromatogram Analysis - HUS Lab')
  plt.xlabel('Retention Time (min)')
  plt.ylabel('Absorbance (mAU)')
  plt.grid(True)
  plt.savefig('hplc_result.png')
  print('Phân tích phổ sắc ký hoàn tất!')


if __name__ == '__main__':
  # Ví dụ xử lý số liệu mẫu
  plot_hplc_chromatogram('sample_hplc_data.csv')
