FROM alpine:latest AS build-image

# Install Python and build dependencies
RUN apk add --no-cache python3 py3-pip

RUN python3 -m venv /opt/venv
COPY requirements.txt /root/requirements.txt
WORKDIR /root

# Use pip to install dependencies into the venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip setuptools wheel && pip install -r requirements.txt

FROM alpine:latest

# Install Python and runtime dependencies
RUN apk add --no-cache python3 ca-certificates

ARG UNAME=smutil
ARG UID=1500
ARG GNAME=smutil
ARG GID=1500
ARG WORKDIR=/opt/smutil

# Activate virtualenv
ENV PATH="/opt/venv/bin:$PATH"

COPY --from=build-image /opt/venv /opt/venv
RUN addgroup -g ${GID} -S ${GNAME} && adduser -u ${UID} -G ${GNAME} -S -H ${UNAME}

RUN mkdir -p ${WORKDIR}
COPY --chown=${UNAME}:${UNAME} src/ ${WORKDIR}/src/
COPY --chown=${UNAME}:${UNAME} v0/ ${WORKDIR}/v0/
COPY --chown=${UNAME}:${UNAME} templates/ ${WORKDIR}/templates/

USER ${UID}

WORKDIR ${WORKDIR}
EXPOSE 8080
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "src.app:app"]