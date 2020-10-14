#################################
FROM python:3.7

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y git 
RUN apt-get install -y curl

RUN pip install easyocr

RUN  apt-get install -y libgl1-mesa-dev

RUN wget https://raw.githubusercontent.com/yanliang12/yan_ocr/main/yan_ocr_download_model.py

RUN python yan_ocr_download_model.py

RUN apt-get install -y tar

RUN git clone https://github.com/yanliang12/yan_ocr.git

WORKDIR /yan_ocr/

CMD bash
#################################
