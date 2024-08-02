# Variables
PYTHON = python
PYINSTALLER = pyinstaller
MAIN_SCRIPT = scripts/launcher.py
EXECUTABLE_NAME = ersc_au_launcher.exe
ZIP_NAME = ersc_auto_update.zip

# Directories
IMAGE_DIR = assets
TEXT_DIR = text_resources
DIST_DIR = dist

# Directories to include in zip
DIRS = $(IMAGE_DIR) $(TEXT_DIR)
EXEC = $(DIST_DIR)/$(EXECUTABLE_NAME)

# Default target
all: executable zip_package

# Create executable using PyInstaller
executable:
	$(PYINSTALLER) --onefile --name $(EXECUTABLE_NAME) $(MAIN_SCRIPT)

# Create zip package
zip_package: $(ZIP_NAME)

$(ZIP_NAME): executable
	zip -r $(ZIP_NAME) $(DIRS)
	zip -j $(ZIP_NAME) $(EXEC)


# Clean up
clean:
	@echo "Current working directory:"
	@cd
	@if exist $(ZIP_NAME) del /Q $(ZIP_NAME)
	@if exist $(EXECUTABLE_NAME).spec del /Q $(EXECUTABLE_NAME).spec
	@if exist build rmdir /S /Q build
	@if exist dist rmdir /S /Q dist

.PHONY: all executable zip_package clean