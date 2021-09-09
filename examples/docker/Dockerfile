FROM mcr.microsoft.com/mssql/server:2017-latest

RUN mkdir -p /ddaa/config
WORKDIR /uda/config

COPY config /uda/config

RUN chmod +x /uda/config/entrypoint.sh
RUN chmod +x /uda/config/setup.sh

ENTRYPOINT ["./entrypoint.sh"]
