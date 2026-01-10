ARG BUILD_FROM
FROM $BUILD_FROM

MAINTAINER micmoc95 <mic.morat@gmail.com>

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update && apt-get install -y --no-install-recommends android-sdk-platform-tools android-tools-adb adb

COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
