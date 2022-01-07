FROM python:3.8

# Install apps and packages
RUN apt-get update && apt-get -y install libgomp1 clang ffmpeg libsm6 libxext6
RUN pip --no-cache-dir install --upgrade pip
RUN pip --no-cache-dir install -U micropipenv[toml] libclang
COPY ./pyproject.toml /code/
COPY ./poetry.lock /code/
RUN cd /code/ && micropipenv install -- --no-cache-dir
RUN pip uninstall -y micropipenv[toml]

# Move code over
COPY ./rcv_mnm/ /code/rcv_mnm/
RUN export PATH=/code/rcv_mnm/main.py:$PATH

# Start streamlit and run app
WORKDIR /code/rcv_mnm
EXPOSE 8080
ENTRYPOINT ["streamlit", "run", "--server.port=8080", "--server.enableCORS=false", "--server.maxUploadSize=5"]
CMD ["main.py"]