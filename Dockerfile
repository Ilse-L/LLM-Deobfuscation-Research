FROM debian:12-slim

# Prevent interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# Create working directory
WORKDIR /workspace

ENV VENV_PATH=/opt/venv

# install dependencies
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3.11-venv \
    python3-pip \
    git \
    unzip \
    tar \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3.11 -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install notebook pandas lizard "datasets<2.16" huggingface_hub && \
    pip install -r ObfuXtreme/requirements.txt

# Expose Jupyter Notebook port
EXPOSE 8888

# Default command: start Jupyter Notebook server
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
