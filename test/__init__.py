import sys
import os

# 取得目前檔案(__init__.py)的目錄
current_dir = os.path.dirname(__file__)

# 取得專案根目錄的路徑
project_root = os.path.abspath(os.path.join(current_dir, ".."))  # 這假設專案根目錄在test目錄的上一層

# 將專案根目錄新增至模組搜尋路徑
src_dir = os.path.join(project_root, "src")
sys.path.append(src_dir)
