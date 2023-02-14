#!/usr/bin/make
#

all: buildout

help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: setup
setup:  ## Setups environment
	# if command -v python2 >/dev/null && command -v virtualenv; then virtualenv -p python2 . ; elif command -v virtualenv-2.7; then virtualenv-2.7 . ;fi
	if command -v virtualenv-2.7; then virtualenv-2.7 . ; elif command -v python2 >/dev/null && command -v virtualenv; then virtualenv -p python2 . ; fi
	./bin/pip install --upgrade pip
	./bin/pip install -r requirements.txt

.PHONY: buildout
buildout:  ## Runs setup and buildout
	rm -f .installed.cfg .mr.developer.cfg
	if ! test -f bin/buildout;then make setup;fi
	bin/buildout -t 5

.PHONY: cleanall
cleanall:  ## Cleans all installed buildout files
	rm -fr bin include lib local share develop-eggs downloads eggs parts .installed.cfg
