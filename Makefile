#!/usr/bin/make
# pyenv is a requirement
# plone parameter must be passed to create environment
SHELL:=/bin/bash
ifeq (, $(shell which pyenv))
  $(error "pyenv command not found! Aborting")
endif
plones=4.3 5.2 6.0
ifeq ($(plone),4.3)
  python=2.7
else
  python=3.7
endif
ifeq ($(plone),6.0)
  python=3.10
endif

all: buildout

help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.python-version:  ## Setups pyenv version
	@pyenv local `pyenv versions |grep "  $(python)" |xargs`
	@echo "Local pyenv version is `cat .python-version`"

bin/buildout: oneof-plone .python-version  ## Setups environment
	virtualenv .
	./bin/pip install --upgrade pip
	./bin/pip install -r requirements.txt

.PHONY: setup
setup: cleanall bin/buildout ## Setups environment

.PHONY: buildout
buildout: bin/buildout  ## Runs setup and buildout
	rm -f .installed.cfg .mr.developer.cfg
	# if ! test -f bin/buildout;then make setup;fi
	bin/buildout -t 5

.PHONY: cleanall
cleanall:  ## Cleans all installed buildout files
	rm -fr bin include lib local share develop-eggs downloads eggs parts .installed.cfg .mr.developer.cfg .python-version pyvenv.cfg

.PHONY: guard-%
guard-%:
	@ if [ "${${*}}" = "" ]; then \
			echo "You must give a value for variable '$*' : like $*=xxx"; \
			exit 1; \
	fi

.PHONY: oneof-%
oneof-%:
	@ if ! echo "${${*}s}" | tr " " '\n' |grep -Fqx "${${*}}"; then echo "Invalid '$*' parameter ('${${*}}') : must be one of '${${*}s}'"; exit 1; fi
