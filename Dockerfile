FROM python:3.9.6-slim-buster as base

ENV \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # use this version
    POETRY_VERSION=1.2.0 \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:/aht/dsf/.venv/bin:$PATH"

# Install dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    build-essential \
    jq \
    curl
    #yq

# Add a user
RUN useradd --uid 1000 --create-home python

# Install poetry
RUN curl -sSL https://install.python-poetry.org/ | python -
# Allow all users to run poetry
RUN ls "$POETRY_HOME"
RUN chmod +x "$POETRY_HOME/bin/poetry"

# Copy code
COPY . /aht/dsf
WORKDIR /aht/dsf


FROM base as dev

# install dependencies
RUN poetry install

#EXPOSE 8000
CMD ["python", "dsf.py"]
#CMD ["uvicorn", "--debug", "--reload", "--host", "0.0.0.0", "aht.powergrid-analyzer.backend.webservice:app"]

#FROM base as prod
#
## install dependencies
#RUN poetry install --no-dev
#ENV AHT_NG911_ENV=prod
#EXPOSE 8000
#CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "aht.powergrid-analyzer.backend.webservice:app"]
