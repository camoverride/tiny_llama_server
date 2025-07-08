# Tiny Llama Server

Exposes the tinyllama LLM as a Python flask-restful server.


## Hardware Notes

- Ubuntu: 24.04.2 LTS
- Kernel: 6.11.0-26-generic
- GPU: NVIDIA GeForce RTX 3050
- Cuda compiler: 12.0.140
- Nvidia driver: 550.144.03
- Torch: 2.7.1+cu126


## Install

- `git clone git@github.com:camoverride/tiny_llama_server.git`
- `cd tiny_llama_server`
- Download `TinyLlama-1.1B-Chat-v0.1` to `./`
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`


## Test

- `python server_test.py`


## Run



## Run as a systemd process


## Notes

