import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

model = AutoModelForSeq2SeqLM.from_pretrained("Jayyydyyy/m2m100_418m_tokipona")
tokenizer = AutoTokenizer.from_pretrained("facebook/m2m100_418M")
device = "cuda:0" if torch.cuda.is_available() else "cpu"
LANG_CODES = {
    "English":"en",
    "toki pona":"tl"
}

def translate(text, src_lang, tgt_lang, candidates:int):
    """
    Translate the text from source lang to target lang
    """

    src = LANG_CODES.get(src_lang)
    tgt = LANG_CODES.get(tgt_lang)

    tokenizer.src_lang = src
    tokenizer.tgt_lang = tgt

    ins = tokenizer(text, return_tensors='pt').to(device)

    gen_args = {
            'return_dict_in_generate': True,
            'output_scores': True,
            'output_hidden_states': True,
            'length_penalty': 0.0,  # don't encourage longer or shorter output,
            'num_return_sequences': candidates,
            'num_beams':candidates,
            'forced_bos_token_id': tokenizer.lang_code_to_id[tgt]
        }
    

    outs = model.generate(**{**ins, **gen_args})
    output = tokenizer.batch_decode(outs.sequences, skip_special_tokens=True)

    return '\n'.join(output)

with gr.Blocks() as app:
    markdown="""
    # An English / toki pona Neural Machine Translation App!
    
    ### toki a! 💬

    This is an english to toki pona / toki pona to english neural machine translation app.

    Input your text to translate, a source language and target language, and desired number of return sequences! 

    ### Grammar Regularization
    An interesting quirk of training a many-to-many translation model is that pseudo-grammar correction 
    can be achieved by translating *from* **language A** *to* **language A**
    
    Remember, this can ***approximate*** grammaticality, but it isn't always the best.
    
    For example, "mi li toki e toki pona" (Source Language: toki pona & Target Language: toki pona) will result in: 
    - ['mi toki e toki pona.', 'mi toki pona.', 'mi toki e toki pona']
    - (Thus, the ungrammatical "li" is dropped)

    ### Model and Data
    This app utilizes a fine-tuned version of Facebook/Meta AI's M2M100 418M param model. 
    
    By leveraging the pretrained weights of the massively multilingual M2M100 model, 
    we can jumpstart our transfer learning to accomplish machine translation for toki pona!
    
    The model was fine-tuned on the English/toki pona bitexts found at [https://tatoeba.org/](https://tatoeba.org/)
    
    ### This app is a work in progress and obviously not all translations will be perfect. 
    In addition to parameter quantity and the hyper-parameters used while training, 
    the *quality of data* found on Tatoeba directly influences the perfomance of projects like this! 

    If you wish to contribute, please add high quality and diverse translations to Tatoeba!
    """

    with gr.Row():
        gr.Markdown(markdown)
        with gr.Column():
            input_text = gr.components.Textbox(label="Input Text", value="Raccoons are fascinating creatures, but I prefer opossums.")
            source_lang = gr.components.Dropdown(label="Source Language", value="English", choices=list(LANG_CODES.keys()))
            target_lang = gr.components.Dropdown(label="Target Language", value="toki pona", choices=list(LANG_CODES.keys()))
            return_seqs = gr.Slider(label="Number of return sequences", value=3, minimum=1, maximum=12, step=1)
            
            inputs=[input_text, source_lang, target_lang, return_seqs]
            outputs = gr.Textbox()

            translate_btn = gr.Button("Translate! | o ante toki!")
            translate_btn.click(translate, inputs=inputs, outputs=outputs)

            gr.Examples(
                [
                    ["Hello! How are you?", "English", "toki pona", 3],
                    ["toki a! ilo pi ante toki ni li pona!", "toki pona", "English",  3],
                    ["mi li toki e toki pona", "toki pona", "toki pona", 3],
                ],
                inputs=inputs
            )

app.launch()