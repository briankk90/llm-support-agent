# LLM Customer Support Agent

## Setup
1. Install dependencies: 
2. Run training: 
3. Run evaluation: 
4. Deploy: Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
#0 building with "default" instance using docker driver

#1 [app internal] load build definition from Dockerfile
#1 transferring dockerfile: 200B done
#1 DONE 0.0s

#2 [app internal] load metadata for docker.io/library/python:3.10-slim
#2 ...

#3 [app auth] library/python:pull token for registry-1.docker.io
#3 DONE 0.0s

#2 [app internal] load metadata for docker.io/library/python:3.10-slim
#2 DONE 2.2s

#4 [app internal] load .dockerignore
#4 transferring context: 2B done
#4 DONE 0.0s

#5 [app internal] load build context
#5 DONE 0.0s

#6 [app 1/4] FROM docker.io/library/python:3.10-slim@sha256:57038683f4a259e17fcff1ccef7ba30b1065f4b3317dabb5bd7c82640a5ed64f
#6 resolve docker.io/library/python:3.10-slim@sha256:57038683f4a259e17fcff1ccef7ba30b1065f4b3317dabb5bd7c82640a5ed64f
#6 ...

#7 [app auth] library/python:pull token for registry-1.docker.io
#7 DONE 0.0s

#6 [app 1/4] FROM docker.io/library/python:3.10-slim@sha256:57038683f4a259e17fcff1ccef7ba30b1065f4b3317dabb5bd7c82640a5ed64f
#6 resolve docker.io/library/python:3.10-slim@sha256:57038683f4a259e17fcff1ccef7ba30b1065f4b3317dabb5bd7c82640a5ed64f 1.0s done
#6 DONE 1.0s

#5 [app internal] load build context
#5 transferring context: 6.74kB 0.0s done
#5 DONE 0.0s

#6 [app 1/4] FROM docker.io/library/python:3.10-slim@sha256:57038683f4a259e17fcff1ccef7ba30b1065f4b3317dabb5bd7c82640a5ed64f
#6 sha256:a102ca2561bb2ab259d7519e30d69459b1d75c9a65e7a6c7a2e7d93ee0e82d07 1.75kB / 1.75kB done
#6 sha256:b32fa0454ca185102d4d2e8c7097c1478dba51eab18215c4599479fb44bf3d63 5.31kB / 5.31kB done
#6 sha256:254e724d77862dc53abbd3bf0e27f9d2f64293909cdd3d0aad6a8fe5a6680659 0B / 28.23MB 0.1s
#6 sha256:92e5f9e5de64a1369423a10d83393bf1a3533dd76c039b32cb0251bffd7ae33d 0B / 3.51MB 0.1s
#6 sha256:765ef9c81879b3bfc7185726a38c8b3531b80fc48d6e54d8725a6cabf02c60e1 0B / 15.65MB 0.1s
#6 sha256:57038683f4a259e17fcff1ccef7ba30b1065f4b3317dabb5bd7c82640a5ed64f 9.13kB / 9.13kB done
#6 sha256:254e724d77862dc53abbd3bf0e27f9d2f64293909cdd3d0aad6a8fe5a6680659 11.53MB / 28.23MB 0.4s
#6 sha256:254e724d77862dc53abbd3bf0e27f9d2f64293909cdd3d0aad6a8fe5a6680659 16.78MB / 28.23MB 0.5s
#6 sha256:92e5f9e5de64a1369423a10d83393bf1a3533dd76c039b32cb0251bffd7ae33d 3.51MB / 3.51MB 0.5s
#6 sha256:254e724d77862dc53abbd3bf0e27f9d2f64293909cdd3d0aad6a8fe5a6680659 26.21MB / 28.23MB 0.6s
#6 sha256:92e5f9e5de64a1369423a10d83393bf1a3533dd76c039b32cb0251bffd7ae33d 3.51MB / 3.51MB 0.5s done
#6 sha256:d15668d6a1de27ac749c4d14e5aa7769b29e8853056f3f17e0678fa13aae1812 0B / 248B 0.6s
#6 sha256:254e724d77862dc53abbd3bf0e27f9d2f64293909cdd3d0aad6a8fe5a6680659 28.23MB / 28.23MB 0.7s
#6 sha256:765ef9c81879b3bfc7185726a38c8b3531b80fc48d6e54d8725a6cabf02c60e1 2.10MB / 15.65MB 0.7s
#6 sha256:765ef9c81879b3bfc7185726a38c8b3531b80fc48d6e54d8725a6cabf02c60e1 10.49MB / 15.65MB 0.9s
#6 sha256:d15668d6a1de27ac749c4d14e5aa7769b29e8853056f3f17e0678fa13aae1812 248B / 248B 0.9s
#6 sha256:254e724d77862dc53abbd3bf0e27f9d2f64293909cdd3d0aad6a8fe5a6680659 28.23MB / 28.23MB 1.0s done
#6 sha256:765ef9c81879b3bfc7185726a38c8b3531b80fc48d6e54d8725a6cabf02c60e1 14.68MB / 15.65MB 1.0s
#6 sha256:d15668d6a1de27ac749c4d14e5aa7769b29e8853056f3f17e0678fa13aae1812 248B / 248B 1.0s done
#6 extracting sha256:254e724d77862dc53abbd3bf0e27f9d2f64293909cdd3d0aad6a8fe5a6680659
#6 sha256:765ef9c81879b3bfc7185726a38c8b3531b80fc48d6e54d8725a6cabf02c60e1 15.65MB / 15.65MB 1.1s
#6 sha256:765ef9c81879b3bfc7185726a38c8b3531b80fc48d6e54d8725a6cabf02c60e1 15.65MB / 15.65MB 1.2s done
#6 extracting sha256:254e724d77862dc53abbd3bf0e27f9d2f64293909cdd3d0aad6a8fe5a6680659 1.3s done
#6 extracting sha256:92e5f9e5de64a1369423a10d83393bf1a3533dd76c039b32cb0251bffd7ae33d 0.1s
#6 extracting sha256:92e5f9e5de64a1369423a10d83393bf1a3533dd76c039b32cb0251bffd7ae33d 0.2s done
#6 extracting sha256:765ef9c81879b3bfc7185726a38c8b3531b80fc48d6e54d8725a6cabf02c60e1
#6 extracting sha256:765ef9c81879b3bfc7185726a38c8b3531b80fc48d6e54d8725a6cabf02c60e1 0.7s done
#6 extracting sha256:d15668d6a1de27ac749c4d14e5aa7769b29e8853056f3f17e0678fa13aae1812
#6 extracting sha256:d15668d6a1de27ac749c4d14e5aa7769b29e8853056f3f17e0678fa13aae1812 done
#6 DONE 6.3s

#8 [app 2/4] WORKDIR /app
#8 DONE 0.0s

#9 [app 3/4] COPY . .
#9 DONE 0.0s

#10 [app 4/4] RUN pip install -r requirements.txt
#10 1.848 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
#10 2.127 
#10 2.127 [notice] A new release of pip is available: 23.0.1 -> 25.1.1
#10 2.127 [notice] To update, run: pip install --upgrade pip
#10 DONE 2.3s

#11 [app] exporting to image
#11 exporting layers
#11 exporting layers 1.0s done
#11 writing image sha256:98fe25c72e3954150b0da2843f5055dde459f7cc5d361197529371489d568f39 done
#11 naming to docker.io/library/llm-customer-support-agent-app done
#11 DONE 1.0s

#12 [app] resolving provenance for metadata file
#12 DONE 0.0s
Attaching to app-1

## API
- POST : Send a customer query to get a response.
