# Sharif-Wav2vec2
**This repo shows how to finetune the wav2vec2.0 model along with its prerequisites.**
----------------------------------------------------------------------------------------
In this repository, an attempt was made to examine all aspects of the wav2vec2 model
## Contents
-We selected the appropriate dataset for fine-tuning the model and performed the necessary processing on it
-We defined a wav2vec2 model
-We built a language model using textual data
-We taught the model to add and test language models
-We designed a service based on wav2vec2
-These materials are the result of our studies over a year
## Comparison
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
## Fine-tuned Model
- :hugs: You can find finetuned models at these addresses:

- https://huggingface.co/SaraSadeghi/Sharif-Wav2vec2
- https://huggingface.co/SLPL/Sharif-wav2vec2

## Thanks to
thanks to @sadrasabouri 

Also, I would like to thank @m3hrdadfi for using part of normalized data and dictionary
## How to use
The order of using the codes:
1.Preprocessing
2. Fine-tuning
3.MakingLM
4. Test Model
5. client
## Useful links
- Base Model:
- Base Paper:
- Language Model:
- 
