# Sharif-Wav2vec2
**This repo shows how to finetune the wav2vec2.0 model along with its prerequisites.**
----------------------------------------------------------------------------------------
In this repository, an attempt was made to examine all aspects of the wav2vec2 model.
## Table of Contents
1. [General Info](#general-info)
2. [How to Use](#how-to-use)
3. [Fine-tuned Model](#fine-tuned-model)
4. [Comparison](#comparison)
5. [Useful Links](#useful-links)
6. [Thanks to](#thanks-to)
## General Info
***

- Datasets: 
for fine-tuning the Sharif-Wav2vec2-v1 model we've used: [Mozilla Common Voice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)

  The main datasets used for fine-tuning the Sharif-Wav2vec2-v2 model consist of [BigFarsdat](https://catalogue.elra.info/en-us/repository/browse/ELRA-S0380/), [DeepMine](https://data.deepmine.ir/en/),
  [FarsSpon](https://asrgooyesh.com/fa/shop/%d8%af%d8%a7%d8%af%da%af%d8%a7%d9%86-farsspon/) & [Mozilla Common Voice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE) (AGP Dataset)
- Corpus : Most of our textual data was taken from [naab](https://github.com/Sharif-SLPL/t5-fa) corpus which is a Huge corpora of textual data in Farsi
- System Config: To fine-tune this model, [NVIDIA GeForce RTX 3060-12 GB](https://www.nvidia.com/nl-nl/geforce/graphics-cards/30-series/rtx-3060-3060ti/) is used

## How to Use
***
Order of use:
1. Preprocessing
2. Fine-tuning
3. MakingLM
4. Test Model
5. client
## Fine-tuned Model
***
- :hugs: You can find fine-tuned models at these addresses:

- https://huggingface.co/SaraSadeghi/Sharif-Wav2vec2
- https://huggingface.co/SLPL/Sharif-wav2vec2

## Comparison
***
Several models were fine-tuned in this process, so this is the reason for the discrepancy between the code results. You insert your own route model.
In order to make a fair comparison between the existing wav2vec2 models, we prepared a standard test set including various and appropriate data, which will soon be included with our paper.
|Model|WER|Dataset|LM|
|-----|--|------|------|
|[m3hrdadfi/wav2vec2-large-xlsr-persian-v3](https://huggingface.co/m3hrdadfi/wav2vec2-large-xlsr-persian-v3)||[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)|no
|[m3hrdadfi/wav2vec2-large-xlsr-persian](https://huggingface.co/m3hrdadfi/wav2vec2-large-xlsr-persian)||[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)|no
|[m3hrdadfi/wav2vec2-large-xlsr-persian-v2](https://huggingface.co/m3hrdadfi/wav2vec2-large-xlsr-persian-v2)||[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)|no
|[m3hrdadfi/wav2vec2-large-xlsr-persian-shemo](https://huggingface.co/m3hrdadfi/wav2vec2-large-xlsr-persian-shemo)||[shEMO](https://www.kaggle.com/datasets/mansourehk/shemo-persian-speech-emotion-detection-database)|no
|[wav2vec2-xlsr-multilingual-53-fa](https://huggingface.co/masoudmzb/wav2vec2-xlsr-multilingual-53-fa)||[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)+ Personal Data|no
|[Sharif-Wav2vec2-v1](https://huggingface.co/Kamtera/persian-tts-female-tacotron2)||[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)|no
|[Sharif-Wav2vec2-v2](https://huggingface.co/Kamtera/persian-tts-female-Hifigan)||[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)+ [AGP](https://github.com/asr-gooyesh-pardaz) Dataset|no
|[Sharif-Wav2vec2-v1](https://huggingface.co/Kamtera/persian-tts-female-tacotron2)||[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)|yes
|[Sharif-Wav2vec2-v2](https://huggingface.co/Kamtera/persian-tts-female-Hifigan)||[Mozilla_CommonVoice](https://commonvoice.mozilla.org/en?gclid=CjwKCAjw67ajBhAVEiwA2g_jEN4oRBq-KiWJxb0gxbtXYKjm2IbKVvLyKnZasu8TAo-NiKeC1N-ODhoCGLMQAvD_BwE)+ [AGP](https://github.com/asr-gooyesh-pardaz) Dataset|yes

## Useful Links
***
- Base Model:https://huggingface.co/facebook/wav2vec2-large-xlsr-53
- Base Paper: https://arxiv.org/abs/2006.13979
- Language Model: https://github.com/kpu/kenlm https://kheafield.com/code/kenlm/
- Other Wav2vec2 Models info: https://github.com/facebookresearch/fairseq/tree/main/examples/wav2vec#wav2vec-20
- Our Standard Farsi Testset : Loading ....	:hourglass_flowing_sand:
## Thanks to
***

Thanks to [Sadra Sabouri](https://github.com/sadrasabouri) for his collaboration:handshake::handshake:

Also, I would like to thank [Mehrdad Farahani](https://github.com/m3hrdadfi) for his normalizer and dictionary :handshake:
***

:star:**Give us a star if you found this repo useful.**

🙋‍♀️ **Open an issue if you have any comments about them.**

:smiling_face_with_three_hearts: **Feel free to open a pull request addding your feature. We'll be more than happy to accept them.**

