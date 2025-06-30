# run_prompts.py
import os
import subprocess
import time
import torch

# 初始化计数器文件
COUNTER_FILE = "prompt_counter.txt"
if not os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "w") as f:
        f.write("0")

# 待处理的prompt列表
prompts = [
    "Explain the concept of attention mechanisms in transformers.",
    "How does a large language model generate coherent text?",
    "Compare supervised and unsupervised learning in NLP."
]

def update_counter():
    """读取并更新计数器"""
    with open(COUNTER_FILE, "r+") as f:
        count = int(f.read().strip())
        count += 1
        f.seek(0)
        f.write(str(count))
        f.truncate()
    return count

def process_prompt(prompt, i):
    """处理单个prompt"""
    # 创建输出文件夹
    output_dir = f"/workspace/mnt/data/prompt_{i}"
    os.makedirs(output_dir, exist_ok=True)
    
    #创建decode阶段的.pt文件
    empty_tensor = torch.tensor([])  # 创建空张量
    torch.save(empty_tensor, f"/workspace/mnt/data/prompt_{i}/decode_info.pt")
    
    # 调用qwen.py并捕获输出
    start_time = time.time()
    result = subprocess.run(
        ["python", "qwen_func.py", prompt]
    )
    elapsed = time.time() - start_time
    
    print(f"Processed prompt_{i} in {elapsed:.2f}s")

def main():
    for prompt in prompts:
        i = update_counter()
        process_prompt(prompt, i)

if __name__ == "__main__":
    main()