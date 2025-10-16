.PHONY: help clean-mac clean-windows

help:
	@echo ""
	@echo "Available global make commands:"
	@echo "  make help             			- Show this help message."
	@echo "  make clean-(mac/windows)       - Removes all build artifacts"

clean-mac:
	find . -type f \( -name "*.py[co]" -o -name ".DS_Store" \) -delete
	find . -type d -name "__pycache__" -delete

clean-windows:
	python -c "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__') if '.venv' not in p.parts]"

repo-labels:
	@echo "Fetching GitHub labels..."
	@gh label list || (echo "GitHub CLI not configured. Run 'gh auth login' first." && exit 1)