import os


"""
Get all directories
Directory name should be the prefix of all internal files
	<dir_name>_<filename>.txt
	<dir_name>_<subdir_name>
General file structure:
	<dir_name>_README.md
	<dir_name>_pieces.txt
	<dir_name>_sprites
		<dir_name>_<piece_type>.png
"""
dir_names = [x[0] for x in os.walk(os.getcwd())]


def make_pieces(dir):
	pass	
