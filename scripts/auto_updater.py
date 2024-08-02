import requests
import os
import zipfile
import shutil
from resource_path_getter import resource_path
class autoUpdater:
	def __init__(self):
		self.owner = "LukeYui"
		self.repo = "EldenRingSeamlessCoopRelease"


	def query_latest_release(self):
		# GitHub API endpoint for the latest release
		api_url = f"https://api.github.com/repos/{self.owner}/{self.repo}/releases/latest"
		
		# Get the latest release information
		response = requests.get(api_url)
		response.raise_for_status()

		release_data = response.json()

		version = release_data['tag_name']

		with open(os.path.join('text_resources','version'), 'r') as f:
			current_version = f.readline()



		return current_version == version

	def copy_previous_settings(self):
		ini_file_path = os.path.join('SeamlessCoop', 'ersc_settings.ini')
		temp_settings_path = os.path.join('text_resources', 'temp_settings.txt')

		# Read the contents of the ini file
		with open(ini_file_path, 'r') as file:
			lines = file.readlines()

		# Create a new file in text_resources and write the contents
		with open(temp_settings_path, 'w') as file:
			file.writelines(lines)
		
	def restore_previous_settings(self):
		ini_file_path = os.path.join('SeamlessCoop', 'ersc_settings.ini')
		temp_settings_path = os.path.join('text_resources', 'temp_settings.txt')

		# Read the contents of the ini file
		with open(temp_settings_path, 'r') as file:
			lines = file.readlines()

		# Write the updated contents back to the ini file
		with open(ini_file_path, 'w') as file:
			file.writelines(lines)

		# Remove the temp_settings file
		os.remove(temp_settings_path)
		


	def clear_prior_releases(self):
		# Remove the SeamlessCoop directory and its contents
		shutil.rmtree('SeamlessCoop', ignore_errors=True)
		
		# Remove the ersc_launcher.exe file
		if os.path.exists('ersc_launcher.exe'):
			os.remove('ersc_launcher.exe')



	def download_latest_release(self):
		# GitHub API endpoint for the latest release
		api_url = f"https://api.github.com/repos/{self.owner}/{self.repo}/releases/latest"
		
		# Get the latest release information
		response = requests.get(api_url)
		response.raise_for_status()  # Raise an exception for HTTP errors
		release_data = response.json()
		version = release_data['tag_name']
		# Get the download URL of the first asset (assuming it's the one you want)
		asset_url = release_data['assets'][0]['browser_download_url']
		
		# Download the asset
		asset_response = requests.get(asset_url)
		asset_response.raise_for_status()
		
		# Save the downloaded file as ersc.zip
		zip_filename = 'ersc.zip'
		with open(zip_filename, 'wb') as f:
			f.write(asset_response.content)
		
		print(f"Downloaded: {zip_filename}")
		
		# Unzip the file to the 'test' directory

		
		with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
			zip_ref.extractall(os.getcwd())

		with open(os.path.join('text_resources','version'), 'w') as f:
			f.write(version)

		os.remove('ersc.zip')
		print(f"Extracted to: main directory")

	
	def update_coop_password(self):


		ini_file_path = os.path.join('SeamlessCoop', 'ersc_settings.ini')
		
		# Read the contents of the ini file
		with open(ini_file_path, 'r') as file:
			lines = file.readlines()
		
		with open(os.path.join('text_resources','cooppassword'), "r") as cooppasswordfile:
			password = cooppasswordfile.readline()


		# Update the cooppassword line
		for i, line in enumerate(lines):
			if line.startswith('cooppassword ='):
				lines[i] = f'cooppassword = {password}\n'
				break
		
		# Write the updated contents back to the ini file
		with open(ini_file_path, 'w') as file:
			file.writelines(lines)




if __name__ == "__main__":
	updater = autoUpdater()
	print(updater.query_latest_release())

	updater.download_latest_release()
	updater.update_coop_password()
	updater.clear_prior_releases()
