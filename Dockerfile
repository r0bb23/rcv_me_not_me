FROM python:3.8

# Move data over
COPY ./rcv_mnm/ /code/rcv_mnm/
COPY ./pyproject.toml /code/
COPY ./poetry.lock /code/

# Install apps and packages
RUN apt-get update && apt-get -y install libgomp1 clang ffmpeg libsm6 libxext6
RUN pip --no-cache-dir install --upgrade pip
RUN pip --no-cache-dir install -U micropipenv[toml] libclang
RUN cd /code/ && micropipenv install -- --no-cache-dir
RUN export PATH=/code/rcv_mnm/main.py:$PATH

# Start streamlit and run app
WORKDIR /code/rcv_mnm
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "--server.maxUploadSize=5"]
CMD ["main.py"]