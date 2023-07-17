import streamlit as st
from PIL import Image

st.title("CS490U: Generative AI & Applications (Fall 2023)")
select_list = ['Generative AI', 'Text To Text', 'Text To Image', 'Text To Video', 'Text To Music', 'Text To Ad', 'etc']
want_parts = st.sidebar.multiselect("Select the part you want to see", select_list)
if len(want_parts) == 0:
    st.write("You can choose what you want to see in sidebar")
if 'Generative AI' in want_parts:
    st.header("1. Generative AI")
    st.write(
        "Google Cloud 학습 코스: [https://www.cloudskillsboost.google/journeys/118](https://www.cloudskillsboost.google/journeys/118)")
if 'Text To Text' in want_parts:
    st.header("2. Text To Text")
    ttt_list=['GPT-Model', 'ChatGPT']
    ttt_parts = st.multiselect("Select the part you want to see", ttt_list)
    if 'GPT-Model' in ttt_parts:
        st.header("GPT-Model")
        st.write("GPT-1부터 GPT-3까지의 model structure, data processing 관련 특징을 정리했다.")
        data=open("./pptx/cs490u_week2.pptx", "rb")
        GPT_ppt_down = st.download_button(label="Download GPT model ppt", data=data, file_name="cs490u_week2.pptx")
    if 'ChatGPT' in ttt_parts:
        st.header("ChatGPT")
        st.write("ChatGPT 파인튜닝 방법(Methods 참조): [https://openai.com/blog/chatgpt](https://openai.com/blog/chatgpt)")
        st.write(
            "GPT-3에서 ChatGPT까지의 차이점: [https://velog.io/@easter423/GPT-3-vs-GPT-3.5-vs-ChatGPT](https://velog.io/@easter423/GPT-3-vs-GPT-3.5-vs-ChatGPT)")
        st.write("GPT-4 모델크기/학습방법 비공개: [https://www.mk.co.kr/news/it/10685029](https://www.mk.co.kr/news/it/10685029)")
        GPT4_price_image = Image.open("./images/GPTPlus_price.PNG")
        st.image(GPT4_price_image, caption="GPTPLUS 한 달 이용가격")
        st.write("GPT-4를 무료로 사용하는 방법: [https://wrtn.ai/](https://wrtn.ai/)에서 GPT-4 채팅을 무료로 사용가능함")
        GPT4_wrtn_image = Image.open('./images/GPT4_wrtn.png')
        st.image(GPT4_wrtn_image, caption='GPT-4를 무료로 사용하는 방법')
if 'Text To Image' in want_parts:
    st.header("3. Text To Image")
    tti_list = ['Stable Diffusion', 'DALL-E 2', 'Midjourney', 'StyleGAN']
    tti_parts = st.multiselect("Select the part you want to see", tti_list)
    if 'Stable Diffusion' in tti_parts:
        st.header("Stable Diffusion")
        st.write("Stable Diffusion 개발사인 stability.ai에서 제공하는 DreamStudio서비스는 Credit이라는 유료재화를 이용하며 이는 이미지 한장 출력이 아닌 이미지 출력에 사용되는 컴퓨팅 파워이다.")
        st.write(
            "쓰는 모델, 생성 이미지의 크기, 생성 step 수에 따라 Credit소모량이 다르다")
        ds_price = Image.open("./images/DreamStudio_price.PNG")
        st.image(ds_price, caption='DreamStudio의 가격 정책 10$에 1000Credit')
        st.write(
            "Stable Diffusion의 web-ui Github repo: [https://github.com/AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)")
        st.write(
            "Stable Diffusion web-ui colab구동 버전: [colab link](https://tilnote.io/pages/63353b11cb80d43d62487011#Stable-Diffusion-%EC%8A%A4%ED%85%8C%EC%9D%B4%EB%B8%94-%EB%94%94%ED%93%A8%EC%A0%84)")
    if 'DALL-E 2' in tti_parts:
        st.header("DALL-E 2")
        st.write("DALL-E 2는 현재 무료 체험이 없기 때문에 15달러에 115개의 이미지를 생성하는 플랜을 이용해야 한다.")
        DALLE2_price=Image.open("./images/DALLE_2_price.PNG")
        st.image(DALLE2_price, caption="DALL E-2 price")
        st.write(
            "DALL-E 2 prompt 팁북: [file download link](https://dallery.gallery/wp-content/uploads/2022/07/The-DALL%C2%B7E-2-prompt-book-v1.02.pdf)")
        st.write(
            "DALL-E 2 무료 사용 가능 방법: [news link](https://www.itworld.co.kr/news/283363)에 따르면 bing image creator를 통해 DALL-E 2가 사용가능하다")
    if 'Midjourney' in tti_parts:
        st.header("Midjourney")
        st.write("Midjourney는 현재 무료 체험이 사용불가이다: [news link](https://www.aitimes.com/news/articleView.html?idxno=150269)")
        Midjourney_price_image = Image.open('./images/Midjourney_price.PNG')
        st.image(Midjourney_price_image, caption='Midjourney는 현재 무료 체험이 사용불가이다')
    if 'StyleGAN' in tti_parts:
        st.header("StyleGAN")
        st.write(
            "StyleGAN은 다른 text to image 모델들이 diffusion을 사용한 것과 달리 GAN를 중심으로 이미지 생성을 하며 mapping network를 통해 feature disentanglement를 하여 layer scale에 따라 독립적인 feature 학습을 한 모델이다(참조: [link](https://comlini8-8.tistory.com/11)).")
        st.write(
            "최신 StyleGAN인 StyleGAN3의 github repo(하드웨어 요구사항이 높음, 1–8 high-end NVIDIA GPUs with at least 12 GB of memory): [https://github.com/NVlabs/stylegan3](https://github.com/NVlabs/stylegan3)")
if 'Text To Video' in want_parts:
    st.header("4. Text To Video")
    st.header("Runway")
    st.write(
        "Runway는 현재 무료 이용은 가능하나 5-6개의 4초 영상만 만들 수 있음: [https://research.runwayml.com/gen2](https://research.runwayml.com/gen2)")
    Runway_price_image = Image.open('./images/Runway_price.PNG')
    st.image(Runway_price_image, caption='Runway price')
    st.write(
        "Runway tutorial: [https://www.youtube.com/watch?v=cqRTBynm2iM](https://www.youtube.com/watch?v=cqRTBynm2iM)")
    Runway_tutorial_image = Image.open('./images/Runway_tutorial.PNG')
    st.image(Runway_tutorial_image, caption='Runway tutorial')
    Gen2_video_file = open("./videos/Gen-2 A woman is drink win, 3998183122.mp4", "rb")
    Gen2_video_bytes = Gen2_video_file.read()
    st.video(Gen2_video_bytes)
if 'Text To Music' in want_parts:
    st.header("5. Text To Music")
    ttm_list = ['Boomy', 'Riffusion']
    ttm_parts = st.multiselect("Select the part you want to see", ttm_list)
    if 'Boomy' in ttm_parts:
        st.header("Boomy")
        Boomy_price=Image.open("./images/Boomy_price.PNG")
        st.image(Boomy_price)
        st.write("프롬프트 등으로 자유롭게 input을 넣는 것이 아니라 이미 있는 곡의 스타일을 고르는 것이 input이 되어 음악을 만드는 Generative AI. 생성 자체는 거의 무료이다.")
        st.write(
            "Boomy tutorial: [https://www.youtube.com/watch?v=I4MjW8QEchk](https://www.youtube.com/watch?v=I4MjW8QEchk)")
    if 'Riffusion' in ttm_parts:
        st.header("Riffusion")
        st.write("기존의 text to music AI들과 달리 diffusion모델을 이용하여 text에서 spectrogram 이미지를 만들고 이 spectrogram으로 음악을 만든다")
        st.write("Riffusion introduce: [https://www.riffusion.com/about](https://www.riffusion.com/about)")
        st.write(
            "Riffusion tutorial: [https://www.youtube.com/watch?v=l5KO2UyGPPE](https://www.youtube.com/watch?v=l5KO2UyGPPE)")
if 'Text To Ad' in want_parts:
    st.header("6. Text To Ad")
    st.header("AdCreative.ai")
    st.write("7일간의 무료체험을 제공하며 그 이후로는 무료플랜이 없음. 가장 싼 Startup Starter플랜도 월 21달러에 광고 10개 생성이 가능함.")
    Startup_price_image=Image.open("./images/Adcreative_Startup_price.PNG")
    Professional_price_image = Image.open("./images/Adcreative_Professional_price.PNG")
    Agency_price_image = Image.open("./images/Adcreative_Agency_price.PNG")
    st.image(Startup_price_image, caption="AdCreative.ai Startup Price Plan")
    st.image(Professional_price_image, caption="AdCreative.ai Professional Price Plan")
    st.image(Agency_price_image, caption="AdCreative.ai Agency Price Plan")
    st.write(
        "AdCreative.ai tutorial: [https://www.youtube.com/watch?v=NZPYi-hVhL8](https://www.youtube.com/watch?v=NZPYi-hVhL8)")
if 'etc' in want_parts:
    st.header("7. etc")
    st.header("Chatsonic")
    st.write(
        "Chatsonic은 GPT-4나 DALL-E 2/Stable Diffusion과 같은 특정 분야에 뛰어난 ai모델들을 어느정도 사용하며(GPT-4 powered) google search를 통해 실시간 정보까지 반영가능한 Ai 챗봇이라고 할 수 있다. 10,000word까지는 free trial로 이용이 가능하다.")
    st.write(
        "Chatsonic tutorial: [https://www.youtube.com/watch?v=iTx9fFHGIvk](https://www.youtube.com/watch?v=iTx9fFHGIvk)")
    Chatsonic_price=Image.open("./images/Chatsonic_price.PNG")
    st.image(Chatsonic_price, caption="Chatsonic price plan")
