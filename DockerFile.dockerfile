FROM python:3.11

ENV APP_HOME /personal_bot

WORKDIR $APP_HOME

COPY . .

RUN pip install poetry

EXPOSE 5000

ENTRYPOINT ["python", "personal_bot/Bot.py"]