.PHONY: full base status

full:
	@echo "Switching to full.sh..."
	@sed -i \
		-e 's|source: "bootstrap/base.sh", destination: "/tmp/bootstrap.sh"|source: "bootstrap/full.sh", destination: "/tmp/bootstrap.sh"|g' \
		Vagrantfile
	@echo "Done. Now using full_bootstrap.sh"

base:
	@echo "Switching to base_bootstrap.sh..."
	@sed -i \
		-e 's|source: "bootstrap/full.sh", destination: "/tmp/bootstrap.sh"|source: "bootstrap/base.sh", destination: "/tmp/bootstrap.sh"|g' \
		Vagrantfile
	@echo "Done. Now using base_bootstrap.sh"

status:
	@echo "Current bootstrap script configuration:"
	@grep -n "source:" Vagrantfile | grep -E "full|base" || echo "No bootstrap script found"

version:
	@echo "Setup k8s version..."
	@sed -i \
		-e 's|K8S_VERSION="1.35"|source: "bootstrap/base.sh", destination: "/tmp/base_bootstrap.sh"|g' \
		bootstrap/base.sh
	@echo "Done. Now using base_bootstrap.sh"
