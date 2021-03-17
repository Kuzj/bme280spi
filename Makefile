SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run mypy bme280spi
	poetry run flake8 .

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report
