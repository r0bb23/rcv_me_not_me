FROM python:3.8

COPY ./rbb-mnm/ /code/

COPY ./models/ /code/

#Install necessary packages from requirements.txt with no cache dir allowing for installation on machine with very little memory on board
RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt

#Exposing the default streamlit port
EXPOSE 8501

#Running the streamlit app
ENTRYPOINT ["streamlit", "run", "--server.maxUploadSize=5"]
CMD ["rcv_mnm/main.py"]