## ENVs
# basic
export PWD=`pwd`
# docker
export CONTAINER_NAME=pykyoupro
# dockerfileのあるディレクトリ
export DIR_DOCKER=./

export DOCKERFILE_NAME=Dockerfile
export CONTAINER_ID=`docker ps --format {{.ID}}`
# --------------------------------------------------------
br: ## build & run
	@make b
	@make r
b: ## build docker.
	docker build -f $(DIR_DOCKER)/$(DOCKERFILE_NAME) -t $(CONTAINER_NAME) .
r: ## run docker.
	docker run -it --rm -p 5000:5000 -v ${PWD}:/src/ \
	$(CONTAINER_NAME) /bin/bash
c: ## connect newest container
	docker exec -i -t $(CONTAINER_ID) /bin/bash
# --------------------------------------------------------
# docker commands
export NONE_DOCKER_IMAGES=`docker images -f dangling=true -q`
export STOPPED_DOCKER_CONTAINERS=`docker ps -a -q`
export RUNNING_DOCKER_CONTAINERS=`docker ps -f status=running -q`
rm: ## rm running container
	docker rm -f $(RUNNING_DOCKER_CONTAINERS)
clean: ## clean images/containers
	-@make clean-images
	-@make clean-containers
clean-images:
	docker rmi $(NONE_DOCKER_IMAGES) -f
clean-containers:
	docker rm -f $(STOPPED_DOCKER_CONTAINERS)
# help
help: ## this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
