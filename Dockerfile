FROM ghcr.io/prefix-dev/pixi:latest

LABEL org.opencontainers.image.description="SmartNote is a release note generation tool aimed at generating release notes personalized to your project domain and audience type."
LABEL org.opencontainers.image.licenses="Mulan PSL v2"
LABEL org.opencontainers.image.source="https://github.com/osslab-pku/SmartNote/"
LABEL org.opencontainers.image.title="SmartNote"
LABEL org.opencontainers.image.url="https://github.com/osslab-pku/SmartNote/"
LABEL org.opencontainers.image.version="v2"

# copy pixi.toml and pixi.lock to the container
COPY ./pixi.toml ./pixi.lock /app/
WORKDIR /app
# run the `install` command (or any other). This will also install the dependencies into `/app/.pixi`
# assumes that you have a `prod` environment defined in your pixi.toml
RUN pixi install && rm -rf ~/.cache/rattler
# Create the shell-hook bash script to activate the environment
RUN pixi shell-hook > /shell-hook.sh
# RUN echo 'export LOGURU_COLORIZE="NO"' >> /shell-hook.sh
# extend the shell-hook script to run the command passed to the container
RUN echo 'exec "$@"' >> /shell-hook.sh

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git curl \
    && rm -rf /var/lib/apt/lists/*

# Copy huggingface and tiktoken models
COPY ./.cache/hub/ /app/.cache/hub/
COPY ./.cache/modules/ /app/.cache/modules/
COPY ./.cache/tiktoken/ /app/.cache/tiktoken/
# Copy classifier models
COPY ./models/gte_xgb_cls_model.json /app/models/
COPY ./models/gte_xgb_flt_model.json /app/models/
# Copy required files to the final image
COPY ./settings.toml config.py /app/
COPY ./smartnote/ /app/smartnote/

# Require environment variables
ENV SMARTNOTE_GITHUB__TOKEN=""
ENV SMARTNOTE_OPENAI__API_KEY=""
ENV SMARTNOTE_OPENAI__BASE_URL="https://api.openai.com/v1"
ENV HF_ENDPOINT="https://hf-mirror.com"
ENV HF_HOME="/app/.cache/"
ENV TIKTOKEN_CACHE="/app/.cache/tiktoken"

# Run the shell-hook script
ENTRYPOINT ["/bin/bash", "/shell-hook.sh", "python3", "-m", "smartnote.generator"]
