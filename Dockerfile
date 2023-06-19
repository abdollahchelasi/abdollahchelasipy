FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# streamlit-specific commands
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

# exposing default port for streamlit
EXPOSE 8501

COPY . .

CMD [ "streamlit", "run", "app.py"]