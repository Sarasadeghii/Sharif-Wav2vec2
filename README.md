# Sharif-Wav2vec2
**This repo shows how to finetune the wav2vec2.0 model along with its prerequisites.**
----------------------------------------------------------------------------------------
In this repository, an attempt was made to examine all aspects of the wav2vec2 model
## Table of Contents
1. [General Info](#general-info)
2. [How to use](#how-to-use)
3. [Fine-tuned Model](#fine-tuned-model)
4. [Comparison](#comparison)
5. [Useful links](#useful-links)
6. [Thanks to](#thanks-to)
## General Info
***
Write down general information about your project. It is a good idea to always put a project status in the readme file. This is where you can add it. 
- Datasets:
- Syestem Config:

## How to use
***
Order of use:
1. Preprocessing
2. Fine-tuning
3. MakingLM
4. Test Model
5. client
## Fine-tuned Model
***
- :hugs: You can find finetuned models at these addresses:

- https://huggingface.co/SaraSadeghi/Sharif-Wav2vec2
- https://huggingface.co/SLPL/Sharif-wav2vec2

## Comparison
***
Several models were finetuned in this process, so this is the reason for the discrepancy between the code results. You insert your own route model.
In order to make a fair comparison between the existing wav2vec2 models, we prepared a standard test set including various and appropriate data, which will soon be included with our paper.
|Model|WER|Dataset|LM|
|-----|--|------|------|
|[m3hrdadfi/wav2vec2-large-xlsr-persian-v3](https://huggingface.co/Kamtera/persian-tts-female-vits)|12%|[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)|no
|[m3hrdadfi/wav2vec2-large-xlsr-persian](https://huggingface.co/m3hrdadfi/wav2vec2-large-xlsr-persian)|12%|[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)|no
|[m3hrdadfi/wav2vec2-large-xlsr-persian-v2](https://huggingface.co/m3hrdadfi/wav2vec2-large-xlsr-persian-v2)|12%|[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)|no
|[m3hrdadfi/wav2vec2-large-xlsr-persian-shemo](https://huggingface.co/m3hrdadfi/wav2vec2-large-xlsr-persian-shemo)|12%|[shEMO](https://www.kaggle.com/datasets/mansourehk/shemo-persian-speech-emotion-detection-database)|no
|[wav2vec2-xlsr-multilingual-53-fa](https://huggingface.co/masoudmzb/wav2vec2-xlsr-multilingual-53-fa)|12%|[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)+ Personal Data|no
|[Sharif-Wav2vec2-v1](https://huggingface.co/Kamtera/persian-tts-female-tacotron2)|12%|[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)|no
|[Sharif-Wav2vec2-v2](https://huggingface.co/Kamtera/persian-tts-female-Hifigan)|12%|[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)+ [AGP](https://github.com/asr-gooyesh-pardaz) Data|no
|[Sharif-Wav2vec2-v1](https://huggingface.co/Kamtera/persian-tts-female-tacotron2)|12%|[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)|yes
|[Sharif-Wav2vec2-v2](https://huggingface.co/Kamtera/persian-tts-female-Hifigan)|12%|[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)+ [AGP](https://github.com/asr-gooyesh-pardaz) Data|yes

## Useful links
***
- Base Model:https://huggingface.co/facebook/wav2vec2-large-xlsr-53
- Base Paper: https://arxiv.org/abs/2006.13979
- Language Model: https://github.com/kpu/kenlm https://kheafield.com/code/kenlm/
- Other Wav2vec2 Models info: https://github.com/facebookresearch/fairseq/tree/main/examples/wav2vec#wav2vec-20
## Thanks to
***

Thanks to @sadrasabouri for his collaboration:handshake::handshake:

Also, I would like to thank @m3hrdadfi for using part of normalized data and dictionary :handshake:




