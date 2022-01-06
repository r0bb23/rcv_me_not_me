# rcv_me_not_me

## What I did

I created a streamlit app that uses a facial recognition model using transfer learning. More on that in the model_creation section within the ipython notbook. The app lets you upload or randomly upload an image from a web search to try and match the face in the picture with one of the faces trained in the model. If it matches my face it will return a link to my resume.

## Code Usage

### Docker

Once the above is killed, you can either use [docker](https://www.docker.com/get-started) via the below commands. This will create a docker container for you with the deps and boot the streamlit app.

#### Build Dockerfile Container

```bash
docker build -t rbb-mnm .
```

#### Run Container Interactively

```bash
docker container run -p 8501:8501 -it rbb-mnm:latest
```

**Note:** I do this interactively so you can monitor and kill it easier.

### Poetry

You can also use poetry if you don't want to deal with docker.

**Note:** The docker version doesn't use poetry directly. It uses the poetry lock file to install the dependencies using micropipenv. So its really a pick your poison virtual environment. I'm personally a bigger fan of using docker for things like this. Its just a bit more guaranteed that you will have fewer environment issues that could cause the code to fail to run.

#### Poetry Install

```bash
pip install poetry
```

**Note:** This is not the recommended way to install poetry according to poetry's website. However, this way is much easier and I find works better. The only issue I've had with this method is you can't update poetry with poetry. But you can use pip, which isn't a big deal.

#### Poetry Environment Setup

From within the code directory which contains the 'pyproject.toml':

```bash
poetry install
```

### Poetry Run Command

Then to run code within the virtual environment you just have to run the code as you usually would but with `poetry run` in front of your calls.

For instance, below is how you would run the streamlit app.

```bash
poetry run python3 main.py
```

**Robert Beatty**