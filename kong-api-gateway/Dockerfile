FROM kong:3.8.0

# USER root
# COPY ./plugins/external-auth /custom-plugins/external-auth
# WORKDIR /custom-plugins/external-auth
# RUN luarocks install lua-resty-http
# RUN luarocks make
# USER kong
# WORKDIR /

COPY --chmod=+x wait-for-it.sh /usr/local/kong/wait-for-it.sh
COPY --chmod=+x run_kong.sh /usr/local/kong/run_kong.sh

CMD ["bash", "/usr/local/kong/run_kong.sh"]
