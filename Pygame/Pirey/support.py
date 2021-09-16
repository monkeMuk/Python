#   ORIGINAL
#import pygame
#from os import walk


#def import_folder(path):
#    surface_list = []

#    for _,__,img_files in walk(path):
 #       for image in img_files:
#        image_surf = pygame.image.load(full_path).convert_alpha()
  #         full_path = path + '/' + image
 #           surface_list.append(image_surf)
#
 #   return surface_list
    #   REVISE THIS IDK WHAT THIS ALL MEAN

#def import_folder(path):
#    for information in walk(path):
#        print(information)
        # walk prints a bunch of file in a folder from top to bottom?

#import_folder("graphics/character/idle")

from os import walk
import pygame

def import_folder(path):
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

		return surface_list
