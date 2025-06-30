# qwen.py
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import sys

def run_inference(prompt):
    model_name = "Qwen/Qwen3-30B-A3B"
    
    # 加载模型和分词器（单例模式，避免重复加载）
    if not hasattr(run_inference, 'model'):
        run_inference.tokenizer = AutoTokenizer.from_pretrained(model_name)
        run_inference.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype="auto",
            device_map="auto"
        )
    
    # 编码输入
    inputs = run_inference.tokenizer(prompt, return_tensors="pt").to(run_inference.model.device)
    
    # 生成文本
    outputs = run_inference.model.generate(
        **inputs,
        max_new_tokens=200,
        do_sample=False,
        num_beams=1,
        temperature=1.0,
        top_k=0,
        top_p=1.0,
        repetition_penalty=1.0
    )
    
    return run_inference.tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    prompt = sys.argv[1]  # 通过命令行参数接收prompt
    result = run_inference(prompt)