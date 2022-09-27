build:
	docker build \
		--tag aht/dsf:latest \
		--target dev \
		.

run:
	docker run \
		-it \
		--volume $(shell pwd):/aht/dsf \
		aht/dsf:latest \
		/bin/bash

test:
	docker run \
		--volume $(shell pwd):/aht/dsf \
		aht/dsf:latest \
		python dsf_test.py

codestyle-check:
	docker run \
		--volume $(shell pwd):/aht/dsf \
		aht/dsf:latest \
		black --check --diff .


codestyle-fix:
	docker run \
		--volume $(shell pwd):/aht/dsf \
		aht/dsf:latest \
		black .