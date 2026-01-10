ARG BUILD_FROM
FROM $BUILD_FROM

MAINTAINER micmoc95 <mic.morat@gmail.com>

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN wget -q https://dl.google.com/android/repository/platform-tools-latest-linux.zip -O /tmp/platform-tools.zip && \
        unzip -q /tmp/platform-tools.zip -d /opt && \
        rm -f /tmp/platform-tools.zip

COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
