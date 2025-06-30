import os
import shutil
import time

def backup_path(path):
    if os.path.exists(path):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        backup_path = f"{path}.backup.{timestamp}"
        print(f"备份存在的路径：{path} -> {backup_path}")
        shutil.move(path, backup_path)

def create_symlink(source_path, link_path):
    try:
        backup_path(link_path)
        os.symlink(source_path, link_path)
        print(f"成功创建软链接: {link_path} -> {source_path}")
    except OSError as e:
        print(f"创建软链接失败: {link_path}, 错误: {e}")

def batch_create_symlinks(symlink_map):
    """
    symlink_map: dict，键是软链接路径，值是目标源路径
    """
    for link_path, source_path in symlink_map.items():
        create_symlink(source_path, link_path)

if __name__ == "__main__":
    # 例子：字典里的键是软链接，值是源路径
    symlinks = {
        "/usr/local/lib/python3.12/dist-packages/transformers/models/qwen3_moe/modeling_qwen3_moe.py": "./softlink_module/softlink.py",
    }

    batch_create_symlinks(symlinks)
