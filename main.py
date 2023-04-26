import gradio as gr
from peft import PeftModel
from transformers import LlamaTokenizer, LlamaForCausalLM, GenerationConfig
import torch
from transformers.generation.utils import GreedySearchDecoderOnlyOutput
import textwrap

tokenizer = LlamaTokenizer.from_pretrained("model")

base_model = LlamaForCausalLM.from_pretrained(
    "model",
    load_in_8bit=False,
    device_map='auto',
)

PROMPT_TEMPLATE = f"""
Below is an instruction that describes a task. Write a response that appropriately completes the request.
 
### Instruction:
[INSTRUCTION]
 
### Response:
"""

DEVICE = "cpu"

def create_prompt(instruction: str) -> str:
    return PROMPT_TEMPLATE.replace("[INSTRUCTION]", instruction)
 
print(create_prompt("by 刘畅 https://github.com/bonnypro/GPT4try.git "))

def generate_response(prompt: str, model: PeftModel) -> GreedySearchDecoderOnlyOutput:
    encoding = tokenizer(prompt, return_tensors="pt")
    input_ids = encoding["input_ids"].to(DEVICE)
 
    generation_config = GenerationConfig(
        temperature=0.1,
        top_p=0.75,
        repetition_penalty=1.1,
    )
    with torch.inference_mode():
        return model.generate(
            input_ids=input_ids,
            generation_config=generation_config,
            return_dict_in_generate=True,
            output_scores=True,
            max_new_tokens=256,
        )
    
def format_response(response: GreedySearchDecoderOnlyOutput) -> str:
    decoded_output = tokenizer.decode(response.sequences[0])
    response = decoded_output.split("### Response:")[1].strip()
    return "\n".join(textwrap.wrap(response))    



def ask_alpaca(prompt: str, model: PeftModel = base_model) -> str:
    prompt = create_prompt(prompt)
    response = generate_response(prompt, model)
    print (format_response(response))
    return (format_response(response))


demo = gr.Interface(fn=ask_alpaca, inputs=gr.Textbox(lines=15, placeholder="Ask Here...",label ="you"), outputs=gr.Textbox(lines=15, placeholder="AI says..."))

demo.launch()   
