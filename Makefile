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