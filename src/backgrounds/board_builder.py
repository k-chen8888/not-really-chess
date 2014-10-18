# Parses a document for background info
def get_field_info(infile):
	f = open(infile)
	
	board_info = {}
	board_info['board_dim'] = []
	board_info['tile_imgs'] = []
	
	for line in f:
		if 'Dimensions: ' in line:
			# Pull map dimensions out of the file
			# Assumed to be in form <width, height>
			temp = [int(s) for s in str.split() if s.isdigit()]
			
			# Minimum map size is 200 tiles by 200 tiles
			board_info['board_dim'].append( temp[0] if temp[0] > 200 else 200)
			board_info['board_dim'].append( temp[1] if temp[1] > 200 else 200)
		
		elif 'World: ' in line:
			# Pull background for entire map
			# Assumed to be at least 25600px by 25600px
			board_info['world_img'] = [s for s in str.split() if '.png' in s][0]
		
		elif 'Tile: ' in line:
			# Pull tile coordinates out of the file
			temp = [int(s) for s in str.split() if s.isdigit()]
			
			# Pull tile background image out of the file
			# Assumed to be 128px by 128px
			board_info['tile_imgs'].append([ [ temp[0], temp[1] ], [s for s in str.split() if '.png' in s][0] ])
			
			# Pull tile elevation out of the file
			# If no such information is pulled, assume it is 0 (ground level)
			board_info['tile_imgs'].append(temp[2] if len(temp) > 3 else 0)
		
		else:
			# All other types of lines are comments
			pass
	
	f.close()
	
	return board_info


# Processes board_info dictionary
# Calculations should be done by finding where the upper left corner of the image belongs
# Draw onto windowSurfaceObj
def load_bg(board_info):
	return Board(board_info)
