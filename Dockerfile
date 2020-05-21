FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

# Install everything else
RUN set -x \
	&& pip install -U pip \
	&& pip install -e .

CMD alembic -x data=1 upgrade head && \
    python manage.py

EXPOSE 5000