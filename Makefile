REPO = https://github.com/spyboy-productions/ObfuXtreme.git
REPO_DIR = ObfuXtreme
URL = https:/raw.githubusercontent.com/Ilse-L/LLM-Deobfuscation-Research/main/obf_cli.py

all: 
	clone install fetch

clone:
	@if [ -d "$(REPO_DIR)" ]; then \
		echo "$(REPO_DIR) already exists, skipping clone."; \
	else \
		git clone $(REPO); \
	fi

install: clone
	pip install -r $(REPO_DIR)/requirements.txt
fetch:
	curl -L -o obf_cli.py $(URL)
clean:
	rm -rf $(REPO_DIR) ob_cli.py
