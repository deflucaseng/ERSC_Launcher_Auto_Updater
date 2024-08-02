from auto_updater import autoUpdater
from setup import setup
from resource_path_getter import resource_path
import os


def is_file_empty(file_path):
	return os.stat(file_path).st_size == 0


if __name__ == "__main__":

	updater = autoUpdater()
	setup_script = setup()


	if(is_file_empty(os.path.join("text_resources", "version"))):
		setup_script.do_setup()

		updater.clear_prior_releases()
		updater.download_latest_release()

	if(not updater.query_latest_release()):
		updater.copy_previous_settings()
		updater.clear_prior_releases()
		updater.download_latest_release()
		updater.restore_previous_settings()


	updater.update_coop_password()
	#os.startfile("ersc_launcher.exe")
	exit()
