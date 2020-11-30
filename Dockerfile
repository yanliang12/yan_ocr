#################################
FROM python:3.7

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y git 
RUN apt-get install -y curl

RUN pip install easyocr

RUN apt-get install -y libgl1-mesa-dev
RUN pip install pyyaml

RUN python -c "import easyocr;reader = easyocr.Reader(['en'])"
RUN python -c "import easyocr;reader = easyocr.Reader(['ch_sim'])"
RUN python -c "import easyocr;reader = easyocr.Reader(['ar'])"

WORKDIR /

RUN git clone https://github.com/yanliang12/yan_ocr.git

WORKDIR /yan_ocr/

CMD bash
#################################
