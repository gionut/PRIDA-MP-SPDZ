# Use the base image
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Install system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
                automake \
                build-essential \
                clang-11 \
                cmake \
                git \
                libboost-dev \
                libboost-thread-dev \
                libclang-dev \
                libgmp-dev \
                libntl-dev \
                libsodium-dev \
                libssl-dev \
                libtool \
                vim \
                gdb \
                valgrind \
        && rm -rf /var/lib/apt/lists/*


# Set the working directory
WORKDIR /workspaces/${localWorkspaceFolderBasename}

# Optional: Install Python dependencies directly here
COPY requirements.txt /workspaces/${localWorkspaceFolderBasename}/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
