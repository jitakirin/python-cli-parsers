temci_report_yaml = /tmp/temci.$(notdir $(CURDIR)).result.yaml

.PHONY: temci

temci:
	docker run -it --rm --volume=$(CURDIR):/src \
	  --env=SETUP='pip install -e .' \
	  --env=SERVE_REPORT=$(temci_report_yaml) \
	  jitakirin/temci exec \
	  --sleep \
	  --sleep_seconds 1 \
	  --no-nice \
	  --min_runs 500 \
	  --max_runs 5000 \
	  --no-cpuset_active \
	  --out $(temci_report_yaml) \
	  temci.yaml
