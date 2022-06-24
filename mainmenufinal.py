#Riya Kommineni 
#final game!!!!
#yayyyyyy!!!!!!


import pygame, time,os,random, math, sys,datetime
from pygame.locals import * 
pygame.init()#initialize the pygame package

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
# TITLE_FONT = pygame.font.SysFont('comicsans', 40)
# MENU_FONT = pygame.font.SysFont('comicsans', 22)

os.system('clear')
WIDTH=700 #like constant
HEIGHT=700
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('freesansbold.ttf', WIDTH//25)
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window

#Define Lists and Dict
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),
"RED" : (255, 0, 0),
"GREEN" : (0, 255, 0),
"BLUE" : (0, 0,255),
# SHADES,
"BLACK" : (0, 0, 0),

"DIM_GREY" : (105, 105, 105),
"FREE_SPEECH_GREY" : (99, 86, 136),
"GREY57" : (145, 145, 145),
"GREY58" : (148, 148, 148),
"GREY59" : (150, 150, 150),
"GREY60" : (153, 153, 153),
"GREY61" : (156, 156, 156),
"GREY62" : (158, 158, 158),
"GREY63" : (161, 161, 161),
"GREY64" : (163, 163, 163),
"GREY65" : (166, 166, 166),
"GREY66" : (168, 168, 168),
"GREY67" : (171, 171, 171),
"GREY68" : (173, 173, 173),
"GREY69" : (176, 176, 176),
"GREY70" : (179, 179, 179),
"GREY71" : (181, 181, 181),
"GREY72" : (184, 184, 184),
"GREY73" : (186, 186, 186),
"GREY74" : (189, 189, 189),
"GREY75" : (191, 191, 191),
"GREY76" : (194, 194, 194),
"GREY77" : (196, 196, 196),
"GREY78" : (199, 199, 199),
"GREY79" : (201, 201, 201),
"GREY80" : (204, 204, 204),
"GREY81" : (207, 207, 207),
"GREY82" : (209, 209, 209),
"GREY83" : (212, 212, 212),
"GREY84" : (214, 214, 214),
"GREY85" : (217, 217, 217),
"GREY86" : (219, 219, 219),
"GREY87" : (222, 222, 222),
"GREY88" : (224, 224, 224),
"GREY89" : (227, 227, 227),
"GREY90" : (229, 229, 229),
"GREY91" : (232, 232, 232),
"GREY92" : (235, 235, 235),
"GREY93" : (237, 237, 237),
"GREY94" : (240, 240, 240),
"GREY95" : (242, 242, 242),
"GREY96" : (245, 245, 245),
"GREY97" : (247, 247, 247),
"GREY98" : (250, 250, 250),
"GREY99" : (252, 252, 252),
"LIGHT_GREY" : (211, 211, 211),
"SLATE_GREY" : (112, 128, 144),
"SLATE_GREY_1" : (198, 226, 255),
"SLATE_GREY_2" : (185, 211, 238),
"SLATE_GREY_3" : (159, 182, 205),
"SLATE_GREY_4" : (108, 123, 139),
"VERY_LIGHT_GREY" : (205, 205, 205),
"WHITE" : (255, 255,255),
"ALICE_BLUE" : (240, 248, 255),
"AQUA" : (0, 255, 255),
"AQUAMARINE" : (127, 255, 212),
"AQUAMARINE_1" : (127, 255, 212),
"AQUAMARINE_2" : (118, 238, 198),
"AQUAMARINE_3" : (102, 205, 170),
"AQUAMARINE_4" : (69, 139, 116),
"AZURE" : (240, 255, 255),
"AZURE_1" : (240, 255, 255),
"AZURE_2" : (224, 238, 238),
"AZURE_3" : (193, 205, 205),
"AZURE_4" : (131, 139, 139),
"BLUE_VIOLET" : (138, 43, 226),
"CADET_BLUE" : (95, 159, 159),
"CADET_BLUE_1" : (1152, 245, 255),
"CADET_BLUE_2" : (142, 229, 238),
"CADET_BLUE_3" : (122, 197, 205),
# "CYAN" : (0, 255, 255),
# "CYAN_1" : (0, 255, 255),
# "CYAN_2" : (0, 238, 238),
# "CYAN_3" : (0, 205, 205),
# "CYAN_4" : (0, 139, 139),
# "DEEP_SKY_BLUE_1" : (0, 191, 255),
# "DEEP_SKY_BLUE_2" : (0, 178, 238),
# "DEEP_SKY_BLUE_3" : (0, 154, 205),
# "DEEP_SKY_BLUE_4" : (0, 104, 139),
# "DODGER_BLUE" : (30, 144, 255),
# "DODGER_BLUE_1" : (30, 144, 255),
# "DODGER_BLUE_2" : (28, 134, 238),
# "DODGER_BLUE_3" : (24, 116, 205),
# "DODGER_BLUE_4" : (16, 78, 139),
"FREE_SPEECH_BLUE" : (65, 86, 197),
"LIGHT_BLUE" : (173, 216, 230),
"LIGHT_BLUE_1" : (191, 239, 255),
"LIGHT_BLUE_2" : (178, 223, 238),
"LIGHT_BLUE_3" : (154, 192, 205),
"LIGHT_BLUE_4" : (104, 131, 139),
"LIGHT_CYAN" : (224, 255, 255),
"LIGHT_CYAN_1" : (224, 255, 255),
"LIGHT_CYAN_2" : (209, 238, 238),
"LIGHT_CYAN_3" : (180, 205, 205),
"LIGHT_CYAN_4" : (122, 139, 139),
"LIGHT_SKY_BLUE" : (135, 206, 250),
"LIGHT_SKY_BLUE_1" : (176, 226, 255),
"LIGHT_SKY_BLUE_2" : (164, 211, 238),
"LIGHT_SKY_BLUE_3" : (141, 182, 205),
"LIGHT_SKY_BLUE_4" : (96, 123, 139),
"LIGHT_SLATE_BLUE" : (132, 112, 255),
"LIGHT_STEEL_BLUE" : (176, 196, 222),
"LIGHT_STEEL_BLUE_1" : (202, 225, 255),
"LIGHT_STEEL_BLUE_2" : (188, 210, 238),
"LIGHT_STEEL_BLUE_3" : (162, 181, 205),
"LIGHT_STEEL_BLUE_4" : (110, 123, 139),
"MEDIUM_BLUE" : (0, 0, 205),
"MEDIUM_SLATE_BLUE" : (123, 104, 238),
"MEDIUM_TURQUOISE" : (72, 209, 204),
"MIDNIGHT_BLUE" : (25, 25, 112),
"NAVY" : (0, 0, 128),
"NAVY_BLUE" : (0, 0, 128),
"NEON_BLUE" : (77, 77, 255),
"NEW_MIDNIGHT_BLUE" : (0, 0, 156),
"PALE_TURQUOISE" : (187, 255, 255),
"PALE_TURQUOISE_1" : (187, 255, 255),
"PALE_TURQUOISE_2" : (174, 238, 238),
"PALE_TURQUOISE_3" : (150, 205, 205),
"PALE_TURQUOISE_4" : (102, 139, 139),
"POWDER_BLUE" : (176, 224, 230),
"RICH_BLUE" : (89, 89, 171),
"ROYAL_BLUE" : (65, 105, 225),
"ROYAL_BLUE_1" : (72, 118, 255),
"ROYAL_BLUE_2" : (67, 110, 238),
"ROYAL_BLUE_3" : (58, 95, 205),
"ROYAL_BLUE_4" : (39, 64, 139),
"ROYAL_BLUE_5" : (0, 34, 102),
"SKY_BLUE" : (135, 206, 235),
"SKY_BLUE_1" : (135, 206, 255),
"SKY_BLUE_2" : (126, 192, 238),
"SKY_BLUE_3" : (108, 166, 205),
"SKY_BLUE_4" : (74, 112, 139),
"SLATE_BLUE" : (131, 111, 255),
"SLATE_BLUE_1" : (122, 103, 238),
"SLATE_BLUE_2" : (122, 103, 238),
"SLATE_BLUE_3" : (105, 89, 205),
"SLATE_BLUE_4" : (71, 60, 139),
"STEEL_BLUE" : (70, 130, 180),
"STEEL_BLUE_1" : (99, 184, 255),
"STEEL_BLUE_2" : (92, 172, 238),
"STEEL_BLUE_3" : (79, 148, 205),
"STEEL_BLUE_4" : (54, 100, 139),
"SUMMER_SKY" : (56, 176, 222),
"TEAL" : (0, 128, 128),
"TRUE_IRIS_BLUE" : (3, 180, 204),
"TURQUOISE" : (64, 224, 208),
"TURQUOISE_1" : (0, 245, 255),
"TURQUOISE_2" : (0, 229, 238),
"TURQUOISE_3" : (0, 197, 205),
"TURQUOISE_4" : (0, 134,139),
 
 
# "BAKERS_CHOCOLATE" : (92, 51, 23),
# "BEIGE" : (245, 245, 220),
# "BROWN" : (166, 42, 42),
# "BROWN_1" : (255, 64, 64),
# "BROWN_2" : (238, 59, 59),
# "BROWN_3" : (205, 51, 51),
# "BROWN_4" : (139, 35, 35),
# "BURLYWOOD" : (222, 184, 135),
# "BURLYWOOD_1" : (255, 211, 155),
# "BURLYWOOD_2" : (238, 197, 145),
# "BURLYWOOD_3" : (205, 170, 125),
# "BURLYWOOD_4" : (139, 115, 85),
# "CHOCOLATE" : (210, 105, 30),
# "CHOCOLATE_1" : (255, 127, 36),
# "CHOCOLATE_2" : (238, 118, 33),
# "CHOCOLATE_3" : (205, 102, 29),
# "CHOCOLATE_4" : (139, 69, 19),
# "DARK_BROWN" : (92, 64, 51),
# "DARK_TAN" : (151, 105, 79),
# "DARK_WOOD" : (133, 94, 66),
"LIGHT_WOOD" : (133, 99, 99),
"MEDIUM_WOOD" : (166, 128, 100),
"NEW_TAN" : (235, 199, 158),
"PERU" : (205, 133, 63),
"ROSY_BROWN" : (188, 143, 143),
"ROSY_BROWN_1" : (255, 193, 193),
"ROSY_BROWN_2" : (238, 180, 180),
"ROSY_BROWN_3" : (205, 155, 155),
"ROSY_BROWN_4" : (139, 105, 105),
"SADDLE_BROWN" : (139, 69, 19),
"SANDY_BROWN" : (244, 164, 96),
"SEMI_SWEET_CHOCOLATE" : (107, 66, 38),
"SIENNA" : (142, 107, 35),
"TAN" : (219, 147, 112),
"TAN_1" : (255, 165, 79),
"TAN_2" : (238, 154, 73),
"TAN_3" : (205, 133, 63),
"TAN_4" : (139, 90, 43),
"VERY_DARK_BROWN" : (92, 64,51),
 
"CHARTREUSE" : (127, 255, 0),
"CHARTREUSE_1" : (127, 255, 0),
"CHARTREUSE_2" : (118, 238, 0),
"CHARTREUSE_3" : (102, 205, 0),
"CHARTREUSE_4" : (69, 139, 0),
# "DARK_GREEN" : (47, 79, 47),
# "DARK_GREEN_COPPER" : (74, 118, 110),
# "DARK_KHAKI" : (189, 183, 107),
# "DARK_OLIVE_GREEN" : (85, 107, 47),
# "DARK_OLIVE_GREEN_1" : (202, 255, 112),
# "DARK_OLIVE_GREEN_2" : (188, 238, 104),
# "DARK_OLIVE_GREEN_3" : (162, 205, 90),
# "DARK_OLIVE_GREEN_4" : (110, 139, 61),
# "DARK_SEA_GREEN" : (143, 188, 143),
# "DARK_SEA_GREEN_1" : (193, 255, 193),
# "DARK_SEA_GREEN_2" : (180, 238, 180),
# "DARK_SEA_GREEN_3" : (155, 205, 155),
# "DARK_SEA_GREEN_4" : (105, 139, 105),
"FOREST_GREEN" : (34, 139, 34),
"FREE_SPEECH_GREEN" : (9, 249, 17),
"GREEN_1" : (0, 255, 0),
"GREEN_2" : (0, 238, 0),
"GREEN_3" : (0, 205, 0),
"GREEN_4" : (0, 139, 0),
"GREEN_YELLOW" : (173, 255, 47),
"KHAKI" : (240, 230, 140),
"KHAKI_1" : (255, 246, 143),
"KHAKI_2" : (238, 230, 133),
"KHAKI_3" : (205, 198, 115),
"KHAKI_4" : (139, 134, 78),
"LAWN_GREEN" : (124, 252, 0),
"LIGHT_SEA_GREEN" : (32, 178, 170),
"LIME" : (0, 255, 0),
"MEDIUM_SEA_GREEN" : (60, 179, 113),
"MEDIUM_SPRING_GREEN" : (0, 250, 154),
"MINT_CREAM" : (245, 255, 250),
# "OLIVE" : (128, 128, 0),
# "OLIVE_DRAB" : (107, 142, 35),
# "OLIVE_DRAB_1" : (192, 255, 62),
# "OLIVE_DRAB_2" : (179, 238, 58),
# "OLIVE_DRAB_3" : (154, 205, 50),
# "OLIVE_DRAB_4" : (105, 139, 34),
# "PALE_GREEN" : (152, 251, 152),
# "PALE_GREEN_1" : (154, 255, 154),
# "PALE_GREEN_2" : (144, 238, 144),
# "PALE_GREEN_3" : (124, 205, 124),
"PALE_GREEN_4" : (84, 139, 84),
"SEA_GREEN" : (46, 139, 87),
"SEA_GREEN_1" : (84, 255, 159),
"SEA_GREEN_2" : (78, 238, 148),
"SEA_GREEN_3" : (67, 205, 128),
"SEA_GREEN_4" : (46, 139, 87),
"SPRING_GREEN" : (0, 255, 127),
"SPRING_GREEN_1" : (0, 255, 127),
"SPRING_GREEN_2" : (0, 238, 118),
"SPRING_GREEN_3" : (0, 205, 102),
"SPRING_GREEN_4" : (0, 139, 69),
"YELLOW_GREEN" : (154, 205,50),
"BISQUE" : (255, 228, 196),
"BISQUE_1" : (255, 228, 196),
"BISQUE_2" : (238, 213, 183),
"BISQUE_3" : (205, 183, 158),
"BISQUE_4" : (139, 125, 107),
"CORAL" : (255, 127, 0),
"CORAL_1" : (255, 114, 86),
"CORAL_2" : (238, 106, 80),
"CORAL_3" : (205, 91, 69),
"CORAL_4" : (139, 62, 47),
"DARK_ORANGE" : (255, 140, 0),
"DARK_ORANGE_1" : (255, 127, 0),
"DARK_ORANGE_2" : (238, 118, 0),
"DARK_ORANGE_3" : (205, 102, 0),
"DARK_ORANGE_4" : (139, 69, 0),
"DARK_SALMON" : (233, 150, 122),
"HONEYDEW" : (240, 255, 240),
"HONEYDEW_1" : (240, 255, 240),
"HONEYDEW_2" : (224, 238, 224),
"HONEYDEW_3" : (193, 205, 193),
"HONEYDEW_4" : (131, 139, 131),
"LIGHT_CORAL" : (240, 128, 128),
"LIGHT_SALMON" : (255, 160, 122),
"LIGHT_SALMON_1" : (255, 160, 122),
"LIGHT_SALMON_2" : (238, 149, 114),
"LIGHT_SALMON_3" : (205, 129, 98),
"LIGHT_SALMON_4" : (139, 87, 66),
"MANDARIN_ORANGE" : (142, 35, 35),
"ORANGE" : (255, 165, 0),
"ORANGE_1" : (255, 165, 0),
"ORANGE_2" : (238, 154, 0),
"ORANGE_3" : (205, 133, 0),
"ORANGE_4" : (139, 90, 0),
"ORANGE_RED" : (255, 36, 0),
"PEACH_PUFF" : (255, 218, 185),
"PEACH_PUFF_1" : (255, 218, 185),
"PEACH_PUFF_2" : (238, 203, 173),
"PEACH_PUFF_3" : (205, 175, 149),
"PEACH_PUFF_4" : (139, 119, 101),
"SALMON" : (250, 128, 114),
"SALMON_1" : (255, 140, 105),
"SALMON_2" : (238, 130, 98),
"SALMON_3" : (205, 112, 84),
"SALMON_4" : (139, 76, 57),
"SIENNA_1" : (255, 130, 71),
"SIENNA_2" : (238, 121, 66),
"SIENNA_3" : (205, 104, 57),
"SIENNA_4" : (139, 71, 38),
"DEEP_PINK," : (255, 20, 147),
"DEEP_PINK_1" : (255, 20, 147),
"DEEP_PINK_2" : (238, 18, 137),
"DEEP_PINK_3" : (205, 16, 118),
"DEEP_PINK_4" : (139, 10, 80),
"DUSTY_ROSE" : (133, 99, 99),
"FIREBRICK" : (178, 34, 34),
"FIREBRICK_1" : (255, 48, 48),
"FIREBRICK_2" : (238, 44, 44),
"FIREBRICK_3" : (205, 38, 38),
"FIREBRICK_4" : (139, 26, 26),
"FELDSPAR" : (209, 146, 117),
"FLESH" : (245, 204, 176),
"FREE_SPEECH_MAGENTA" : (227, 91, 216),
"FREE_SPEECH_RED" : (192, 0, 0),
"HOT_PINK" : (255, 105, 180),
"HOT_PINK_1" : (255, 110, 180),
"HOT_PINK_2" : (238, 106, 167),
"HOT_PINK_3" : (205, 96, 144),
"HOT_PINK_4" : (139, 58, 98),
"INDIAN_RED" : (205, 92, 92),
"INDIAN_RED_1" : (255, 106, 106),
"INDIAN_RED_2" : (238, 99, 99),
"INDIAN_RED_3" : (205, 85, 85),
"INDIAN_RED_4" : (139, 58, 58),
"LIGHT_PINK" : (255, 182, 193),
"LIGHT_PINK_1" : (255, 174, 185),
"LIGHT_PINK_2" : (238, 162, 173),
"LIGHT_PINK_3" : (205, 140, 149),
"LIGHT_PINK_4" : (139, 95, 101),
"MEDIUM_VIOLET_RED" : (199, 21, 133),
"MISTY_ROSE" : (255, 228, 225),
"MISTY_ROSE_1" : (255, 228, 225),
"MISTY_ROSE_2" : (238, 213, 210),
"MISTY_ROSE_3" : (205, 183, 181),
"MISTY_ROSE_4" : (139, 125, 123),
"ORANGE_RED_1" : (255, 69, 0),
"ORANGE_RED_2" : (238, 64, 0),
"ORANGE_RED_3" : (205, 55, 0),
"ORANGE_RED_4" : (139, 37, 0),
"PALE_VIOLET_RED" : (219, 112, 147),
"PALE_VIOLET_RED_1" : (255, 130, 171),
"PALE_VIOLET_RED_2" : (238, 121, 159),
"PALE_VIOLET_RED_3" : (205, 104, 137),
"PALE_VIOLET_RED_4" : (139, 71, 93),
"PINK" : (255, 192, 203),
"PINK_1" : (255, 181, 197),
"PINK_2" : (238, 169, 184),
"PINK_3" : (205, 145, 158),
"PINK_4" : (139, 99, 108),
"RED_1" : (255, 0, 0),
"RED_2" : (238, 0, 0),
"RED_3" : (205, 0, 0),
"RED_4" : (139, 0, 0),
"SCARLET" : (140, 23, 23),
"SPICY_PINK" : (255, 28, 174),
"TOMATO" : (255, 99, 71),
"TOMATO_1" : (255, 99, 71),
"TOMATO_2" : (238, 92, 66),
"TOMATO_3" : (205, 79, 57),
"TOMATO_4" : (139, 54, 38),
"VIOLET_RED" : (208, 32, 144),
"VIOLET_RED_1" : (255, 62, 150),
"VIOLET_RED_2" : (238, 58, 140),
"VIOLET_RED_3" : (205, 50, 120),
"VIOLET_RED_4" : (139, 34, 82),
 
"DARK_ORCHID," : (153, 50, 204),
"DARK_ORCHID_1" : (191, 62, 255),
"DARK_ORCHID_2" : (178, 58, 238),
"DARK_ORCHID_3" : (154, 50, 205),
"DARK_ORCHID_4" : (104, 34, 139),
"DARK_PURPLE" : (135, 31, 120),
"DARK_VIOLET" : (148, 0, 211),
"FUCHSIA" : (255, 0, 255),
"LAVENDER" : (230, 230, 250),
"LAVENDER_BLUSH" : (255, 240, 245),
"LAVENDER_BLUSH_1" : (255, 240, 245),
"LAVENDER_BLUSH_2" : (238, 224, 229),
"LAVENDER_BLUSH_3" : (205, 193, 197),
"LAVENDER_BLUSH_4" : (139, 131, 134),
"MAGENTA" : (255, 0, 255),
"MAGENTA_1" : (255, 0, 255),
"MAGENTA_2" : (238, 0, 238),
"MAGENTA_3" : (205, 0, 205),
"MAGENTA_4" : (139, 0, 139),
"MAROON" : (176, 48, 96),
"MAROON_1" : (255, 52, 179),
"MAROON_2" : (238, 48, 167),
"MAROON_3" : (205, 41, 144),
"MAROON_4" : (139, 28, 98),
"MEDIUM_ORCHID" : (186, 85, 211),
"MEDIUM_ORCHID_1" : (224, 102, 255),
"MEDIUM_ORCHID_2" : (209, 95, 238),
"MEDIUM_ORCHID_3" : (180, 82, 205),
"MEDIUM_ORCHID_4" : (122, 55, 139),
"MEDIUM_PURPLE" : (147, 112, 219),
"MEDIUM_PURPLE_1" : (171, 130, 255),
"MEDIUM_PURPLE_2" : (159, 121, 238),
"MEDIUM_PURPLE_3" : (137, 104, 205),
"MEDIUM_PURPLE_4" : (93, 71, 139),
"NEON_PINK" : (255, 110, 199),
"ORCHID" : (218, 112, 214),
"ORCHID_1" : (219, 112, 219),
"ORCHID_2" : (238, 122, 233),
"ORCHID_3" : (205, 105, 201),
"ORCHID_4" : (139, 71, 137),
"PLUM" : (221, 160, 221),
"PLUM_1" : (255, 187, 255),
"PLUM_2" : (238, 174, 238),
"PLUM_3" : (205, 150, 205),
"PLUM_4" : (139, 102, 139),
"PURPLE" : (160, 32, 240),
"PURPLE_1" : (155, 48, 255),
"PURPLE_2" : (145, 44, 238),
"PURPLE_3" : (125, 38, 205),
"PURPLE_4" : (85, 26, 139),
"THISTLE" : (216, 191, 216),
"THISTLE_1" : (255, 225, 255),
"THISTLE_2" : (238, 210, 238),
"THISTLE_3" : (205, 181, 205),
"THISTLE_4" : (139, 123, 139),
"VIOLET" : (238, 130, 238),
"VIOLET_BLUE" : (159, 95, 159),
 
"BLANCHED_ALMOND," : (255, 235, 205),
"DARK_GOLDENROD" : (184, 134, 11),
"DARK_GOLDENROD_1" : (255, 185, 15),
"DARK_GOLDENROD_2" : (238, 173, 14),
"DARK_GOLDENROD_3" : (205, 149, 12),
"DARK_GOLDENROD_4" : (139, 101, 8),
"LEMON_CHIFFON" : (255, 250, 205),
"LEMON_CHIFFON_1" : (255, 250, 205),
"LEMON_CHIFFON_2" : (238, 233, 191),
"LEMON_CHIFFON_3" : (205, 201, 165),
"LEMON_CHIFFON_4" : (139, 137, 112),
"LIGHT_GOLDENROD" : (238, 221, 130),
"LIGHT_GOLDENROD_1" : (255, 236, 139),
"LIGHT_GOLDENROD_2" : (238, 220, 130),
"LIGHT_GOLDENROD_3" : (205, 190, 112),
"LIGHT_GOLDENROD_4" : (139, 129, 76),
"LIGHT_GOLDENROD_YELLOW" : (250, 250, 210),
"LIGHT_YELLOW" : (255, 255, 224),
"LIGHT_YELLOW_1" : (255, 255, 224),
"LIGHT_YELLOW_2" : (238, 238, 209),
"LIGHT_YELLOW_3" : (205, 205, 180),
"LIGHT_YELLOW_4" : (139, 139, 122),
"PALE_GOLDENROD" : (238, 232, 170),
"PAPAYA_WHIP" : (255, 239, 213),
"CORNSILK" : (255, 248, 220),
"CORNSILK_1" : (255, 248, 220),
"CORNSILK_2" : (238, 232, 205),
"CORNSILK_3" : (205, 200, 177),
"CORNSILK_4" : (139, 236, 120),
"GOLDENROD" : (218, 165, 32),
"GOLDENROD_1" : (255, 193, 37),
"GOLDENROD_2" : (238, 180, 34),
"GOLDENROD_3" : (205, 155, 29),
"GOLDENROD_4" : (139, 105, 20),
"MOCCASIN" : (255, 228, 181),
"YELLOW" : (255, 255, 0),
"YELLOW_1" : (255, 255, 0),
"YELLOW_2" : (238, 238, 0),
"YELLOW_3" : (205, 205, 0),
"YELLOW_4" : (139, 139, 0),
"GOLD" : (255, 215, 0),
"GOLD_1" : (255, 215, 0),
"GOLD_2" : (238, 201, 0),
"GOLD_3" : (205, 173, 0),
"GOLD_4" : (139, 117, 0),
"MEDIUM_GOLDENROD" : (234, 234, 174),
"ANTIQUE_WHITE" : (250, 235, 215),
"ANTIQUE_WHITE_1" : (255, 239, 219),
"ANTIQUE_WHITE_2" : (238, 223, 204),
"ANTIQUE_WHITE_3" : (205, 192, 176),
"ANTIQUE_WHITE_4" : (139, 131, 120),
"FLORAL_WHITE" : (255, 250, 240),
"GHOST_WHITE" : (248, 248, 255),
"NAVAJO_WHITE" : (255, 222, 173),
"NAVAJO_WHITE_1" : (255, 222, 173),
"NAVAJO_WHITE_2" : (238, 207, 161),
"NAVAJO_WHITE_3" : (205, 179, 139),
"NAVAJO_WHITE_4" : (139, 121, 94),
"OLD_LACE" : (253, 245, 230),
"WHITE_SMOKE" : (245, 245, 245),
"GAINSBORO" : (220, 220, 220),
"IVORY" : (255, 255, 240),
"IVORY_1" : (255, 255, 240),
"IVORY_2" : (238, 238, 224),
"IVORY_3" : (205, 205, 193),
"IVORY_4" : (139, 139, 131),
"LINEN" : (250, 240, 230),
"SEASHELL" : (255, 245, 238),
"SEASHELL_1" : (255, 245, 238),
"SEASHELL_2" : (238, 229, 222),
"SEASHELL_3" : (205, 197, 191),
"SEASHELL_4" : (139, 134, 130),
"SNOW" : (255, 250, 250),
"SNOW_1" : (255, 250, 250),
"SNOW_2" : (238, 233, 233),
"SNOW_3" : (205, 201, 201),
"SNOW_4" : (139, 137, 137),
"WHEAT" : (245, 222, 179),
"WHEAT_1" : (255, 231, 186),
"WHEAT_2" : (238, 216, 174),
"WHEAT_3" : (205, 186, 150),
"WHEAT_4" : (139, 126, 102),
"QUARTZ" : (217, 217, 243),
}
clr=colors.get("limeGreen")
#Message Lists
messageMenu=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
messageSettings=["Background Colors", "Screen Size", "Sound On/Off"]
titleMain="Simon Game Menu"
#create dispay wind with any name y like
clock = pygame.time.Clock()

#boxes for menu
Bx=WIDTH//3
Button_menu=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_instruct=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_settings=pygame.Rect(Bx, 200, WIDTH//4, 40)
Button_Game1=pygame.Rect(Bx, 250, WIDTH//4, 40)
Button_Game2=pygame.Rect(Bx, 300, WIDTH//4, 40)
Button_score=pygame.Rect(Bx, 350, WIDTH//4, 40)
Button_exit=pygame.Rect(Bx, 400, WIDTH//4, 40)
Button_colors=pygame.Rect(Bx, 150, WIDTH//3, 40)
Button_size=pygame.Rect(Bx, 200, WIDTH//3, 40)
Button_sound=pygame.Rect(Bx, 250, WIDTH//3, 40)
#images

# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)



bg=pygame.image.load('final images/Background-clouds_800x553.jpg')



cx=350
cy=350
rad=25
speed=2
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse variables
mx = 0
my = 0

#Game Variables 
FPS = 30
FLASHSPEED = 500 # in milliseconds
FLASHDELAY = 200 # in milliseconds
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4 # seconds before game over if no button is pushed.

#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
BRIGHTRED    = (255,   0,   0)
RED          = (230, 177, 225)
BRIGHTGREEN  = (  0, 255,   0)
GREEN        = ( 8, 140, 55)
BRIGHTBLUE   = (  0,   0, 255)
BLUE         = (  168, 235, 237)
BRIGHTYELLOW = (255, 255,   0)
YELLOW       = (247, 148, 10)
DARKGRAY     = ( 40,  40,  40)
bgColor = BLACK

XMARGIN = int((WIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YMARGIN = int((HEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

# Rect objects for each of the four buttons
YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE) 

BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)

REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
    

GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
    
imgsize = 50
im1 = pygame.image.load('final images/flower-removebg-preview.png')
im1 = pygame.transform.scale(im1,(imgsize, imgsize))
im2 = pygame.image.load('final images/heart-removebg-preview.png')
im2 = pygame.transform.scale(im2,(imgsize, imgsize))
im3 = pygame.image.load('final images/peacesign.png')
im3 = pygame.transform.scale(im3,(imgsize, imgsize))
im4 = pygame.image.load('final images/star-removebg-preview.png')
im4 = pygame.transform.scale(im4,(imgsize, imgsize))
im5 = pygame.image.load('final images/shakka-removebg-preview.png')
im5 = pygame.transform.scale(im5,(imgsize, imgsize))
im6 = pygame.image.load('final images/lightningbolt-removebg-preview.png')
im6 = pygame.transform.scale(im6,(imgsize, imgsize))
im7 = pygame.image.load('final images/smileyface-removebg-preview.png')
im7 = pygame.transform.scale(im7,(imgsize, imgsize))
im8 = pygame.image.load('final images/strawberry-removebg-preview.png')
im8 = pygame.transform.scale(im8,(imgsize, imgsize))
# create the object to draw
insSquare=pygame.Rect(xig,yig,ibox,ibox)
squareClr=colors.get("pink")
#keep running create a lp
mountainSquare=pygame.Rect(250,320,180,250)
circleClr=colors.get("blue")
backgrnd=colors.get("limeGreen")
run = True
Game = False

def Menu(Title, message,MENU):
    
    textTitle = TITLE_FONT.render(Title, 1, colors.get("blue"))
    screen.fill(colors.get('white'))
    xd = WIDTH//2 - (textTitle.get_width()//2)
    screen.blit(textTitle, (xd, 50))
    yMenu=150
    clslist=list(colors.keys())
    for item in message:
        colorRand=random.choice(clslist)
        if colorRand == "blue":
            colorRand=random.choice(clslist)

        Button_menu=pygame.Rect(Bx, yMenu, WIDTH//3, 40)
        text=MENU_FONT.render(item, 1, colors.get("blue"))
        pygame.draw.rect(screen, colors.get(colorRand), Button_menu)
        screen.blit(text, (Bx, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
    
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                textTitle = TITLE_FONT.render("Bye-Bye", 1, colors.get("blue"))
                screen.fill(colors.get('white'))
                xd = WIDTH//2 - (textTitle.get_width()//2)
                yd = HEIGHT//2- 40
                screen.blit(textTitle, (xd, yd))
                pygame.display.update()
                pygame.time.delay(500)
                pygame.quit()
                sys.exit()

                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                print(mx,my)
                if Button_instruct.collidepoint((mx, my)):
                    readFile("Instructions","instructions.txt")
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_Game1.collidepoint((mx,my)):
                    Game_1()
                if Button_Game2.collidepoint((mx,my)):
                    Game_2()
                if Button_score.collidepoint((mx,my)):
                    readFile("ScoreBoard", "scoreboard.txt")
                if Button_exit.collidepoint((mx,my)):
                    textTitle = TITLE_FONT.render("Bye-Bye", 1, colors.get("blue"))
                    name="Maria"
                    sce=374
                    date=datetime.datetime.now()
                    scrLine=str(sce)+"      "+name + "      "+date.strftime("%m-%d-%Y")+ "\n"
                    myFile = open("scre.txt", 'a')
                    myFile.write(scrLine)
                    myFile.close()
                    screen.fill(colors.get('white'))
                    xd = WIDTH//2 - (textTitle.get_width()//2)
                    yd = HEIGHT//2- 40
                    screen.blit(textTitle, (xd, yd))
                    pygame.display.update()
                    pygame.time.delay(500)
                    pygame.quit()
                    sys.exit()
                    
           
def readFile(titleF,fileN):
    
    #fills screen with white
    screen.fill(colors.get("white"))
    #rendering text objects
    Title = TITLE_FONT.render(titleF, 1, colors.get("blue"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    text1 = MENU_FONT.render("Yes", 1, colors.get("blue"))
    text2 = MENU_FONT.render("No", 1, colors.get("blue"))

    #creating button options
    Button_1 = pygame.Rect(200, 400, 100, 50)
    Button_2 = pygame.Rect(400, 400, 100, 50)
    # pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
    # pygame.draw.rect(screen, colors.get("limeGreen"), Button_2)

    #ReAd files Instructions and scre
    myFile = open(fileN, "r")
    content = myFile.readlines()
    myFile.close()
    #var to controll change of line
    yi = 150
    for line in content:
        Item = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Item, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+= 40

    #renderig fonts to the screen

    screen.blit(text1, (225, 410))
    screen.blit(text2, (425, 410))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Menu(titleMain,messageMenu, True)
                print("You quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    Menu(titleMain,messageMenu, True) 
                # if Button_2.collidepoint((mx, my)):
                #     return False

def settings():
    Menu("Settings",messageSettings, False)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Menu(titleMain,messageMenu,True)
                print("You quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_colors.collidepoint((mx, my)):
                    print("Change colors")
                if Button_size.collidepoint((mx, my)):
                    print("Change size")
                if Button_sound.collidepoint((mx, my)):
                    print("Change sounds")
                # if Button_2.collidepoint((mx, my)):
                #     return False
    

def Game_1():
    
    def main():
     global FPSCLOCK, DISPLAYSURF, BASICFONT 

     pygame.init()
     FPSCLOCK = pygame.time.Clock()
     DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
     pygame.display.set_caption('Simulate')

     BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
     infoSurf = BASICFONT.render('Have fun!', 1, DARKGRAY)
    
    
     infoRect = infoSurf.get_rect()
     infoRect.topleft = (10, HEIGHT - 25)

    

     # Initialize some variables for a new game
     pattern = [] # stores the pattern of colors
     currentStep = 0 # the color the player must push next
     lastClickTime = 0 # timestamp of the player's last button push
     score = 0
     # when False, the pattern is playing. when True, waiting for the player to click a colored button:
     waitingForInput = False

     while True:
         # main game loop
         clickedButton = None # button that was clicked (set to YELLOW, RED, GREEN, or BLUE)
         
         drawButtons()

         scoreSurf = BASICFONT.render('Score: ' + str(score), 1, WHITE)
         scoreRect = scoreSurf.get_rect()
         scoreRect.topleft = (WIDTH - 100, 10)
         DISPLAYSURF.blit(scoreSurf, scoreRect)

         DISPLAYSURF.blit(infoSurf, infoRect) 

         
        
         
            

         



            


            

         checkForQuit()
         for event in pygame.event.get(): # event handling loop
             if event.type == MOUSEBUTTONUP:
                 mousex, mousey = event.pos
                 clickedButton = getButtonClicked(mousex, mousey)
             elif event.type == KEYDOWN:
                 if event.key == K_q:
                     clickedButton = YELLOW
                 elif event.key == K_w:
                     clickedButton = BLUE
                 elif event.key == K_a:
                     clickedButton = RED
                 elif event.key == K_s:
                     clickedButton = GREEN



         if not waitingForInput:
             # play the pattern
             pygame.display.update()
             pygame.time.wait(1000)
             pattern.append(random.choice((YELLOW, BLUE, RED, GREEN)))
             for button in pattern:
                 flashButtonAnimation(button)
                 pygame.time.wait(FLASHDELAY)
             waitingForInput = True
         else:
             # wait for the player to enter buttons
             if clickedButton and clickedButton == pattern[currentStep]:
                 # pushed the correct button
                 flashButtonAnimation(clickedButton)
                 currentStep += 1
                 lastClickTime = time.time()

                 if currentStep == len(pattern):
                     # pushed the last button in the pattern
                     changeBackgroundAnimation()
                     score += 1
                     waitingForInput = False
                     currentStep = 0 # reset back to first step

             elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
                 # pushed the incorrect button, or has timed out
                 gameOverAnimation()
                 # reset the variables for a new game:
                 pattern = []
                 currentStep = 0
                 waitingForInput = False
                 score = 0
                 pygame.time.wait(1000)
                 changeBackgroundAnimation()
                

            

         pygame.display.update()
         FPSCLOCK.tick(FPS)

    
        


 


    def terminate():
     pygame.quit()
     sys.exit()
     
    def checkForQuit():
     for event in pygame.event.get(QUIT): # get all the QUIT events
         terminate() # terminate if any QUIT events are present
     for event in pygame.event.get(KEYUP): # get all the KEYUP events
         if event.key == K_ESCAPE:
           terminate() # terminate if the KEYUP event was for the Esc key
         pygame.event.post(event) # put the other KEYUP event objects back

 
 
 
    def flashButtonAnimation(color, animationSpeed=50):
     if color == YELLOW:
        
         flashColor = BRIGHTYELLOW
         rectangle = YELLOWRECT
        
        
        
        
        
     elif color == BLUE:
        
         flashColor = BRIGHTBLUE
         rectangle = BLUERECT
       
        
     elif color == RED:
        
         flashColor = BRIGHTRED
         rectangle = REDRECT
        
        
     elif color == GREEN:
        
         flashColor = BRIGHTGREEN
         rectangle = GREENRECT
        
        
        

     origSurf = DISPLAYSURF.copy()
     flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
     flashSurf = flashSurf.convert_alpha()
     r, g, b = flashColor
    
     for start, end, step in ((0, 255, 1), (255, 0, -1)): # animation loop
         for alpha in range(start, end, animationSpeed * step):
             checkForQuit()
             DISPLAYSURF.blit(origSurf, (0, 0))
             flashSurf.fill((r, g, b, alpha))
             DISPLAYSURF.blit(flashSurf, rectangle.topleft)
             pygame.display.update()
             FPSCLOCK.tick(FPS)
     DISPLAYSURF.blit(origSurf, (0, 0))

     pygame.display.update()


    def drawButtons():
     pygame.draw.rect(DISPLAYSURF, YELLOW, YELLOWRECT) 
     pygame.draw.rect(DISPLAYSURF, BLUE,   BLUERECT)
     pygame.draw.rect(DISPLAYSURF, RED,    REDRECT)
     pygame.draw.rect(DISPLAYSURF, GREEN,  GREENRECT)
     DISPLAYSURF.blit(im1,(BUTTONSIZE//2-25+YELLOWRECT.x,BUTTONSIZE//2-25+YELLOWRECT.y))
     DISPLAYSURF.blit(im2,(BUTTONSIZE//2-25+BLUERECT.x,BUTTONSIZE//2-25+BLUERECT.y))
     DISPLAYSURF.blit(im3,(BUTTONSIZE//2-25+REDRECT.x,BUTTONSIZE//2-25+REDRECT.y))
     DISPLAYSURF.blit(im4,(BUTTONSIZE//2-25+GREENRECT.x,BUTTONSIZE//2-25+GREENRECT.y))


    def changeBackgroundAnimation(animationSpeed=40):
     global bgColor
     newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

     newBgSurf = pygame.Surface((WIDTH, HEIGHT))
     newBgSurf = newBgSurf.convert_alpha()
     r, g, b = newBgColor
     for alpha in range(0, 255, animationSpeed): # animation loop
         checkForQuit()
         DISPLAYSURF.fill(bgColor)

         newBgSurf.fill((r, g, b, alpha))
         DISPLAYSURF.blit(newBgSurf, (0, 0))

         drawButtons() # redraw the buttons on top of the

         pygame.display.update()
         FPSCLOCK.tick(FPS)
     bgColor = newBgColor








    def gameOverAnimation(color=WHITE, animationSpeed=50):
     # play all beeps at once, then flash the background
     origSurf = DISPLAYSURF.copy()
     flashSurf = pygame.Surface(DISPLAYSURF.get_size())
     flashSurf = flashSurf.convert_alpha()
    
     r, g, b = color
     for i in range(3): # do the flash 3 times
         for start, end, step in ((0, 255, 1), (255, 0, -1)):
             # The first iteration in this loop sets the following for loop
             # to go from 0 to 255, the second from 255 to 0.
             for alpha in range(start, end, animationSpeed * step): # animation loop #used a website for this part
                 # 
                 checkForQuit()
                 flashSurf.fill((r, g, b, alpha))
                 DISPLAYSURF.blit(origSurf, (0, 0))
                 DISPLAYSURF.blit(flashSurf, (0, 0))
                 drawButtons()
                 pygame.display.update()
                 FPSCLOCK.tick(FPS)



    def getButtonClicked(x, y):
     if YELLOWRECT.collidepoint( (x, y) ):
         return YELLOW
     elif BLUERECT.collidepoint( (x, y) ):
         return BLUE
     elif REDRECT.collidepoint( (x, y) ):
         return RED
     elif GREENRECT.collidepoint( (x, y) ):
         return GREEN
     return None


    if __name__ == '__main__':
     main()
    
    
    
def Game_2():
    
    def main():
     global FPSCLOCK, DISPLAYSURF, BASICFONT 

     pygame.init()
     FPSCLOCK = pygame.time.Clock()
     DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
     pygame.display.set_caption('Simulate')

     BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
     infoSurf = BASICFONT.render('Have fun!', 1, DARKGRAY)
    
    
     infoRect = infoSurf.get_rect()
     infoRect.topleft = (10, HEIGHT - 25)

    

     # Initialize some variables for a new game
     pattern = [] # stores the pattern of colors
     currentStep = 0 # the color the player must push next
     lastClickTime = 0 # timestamp of the player's last button push
     score = 0
     # when False, the pattern is playing. when True, waiting for the player to click a colored button:
     waitingForInput = False

     while True:
         # main game loop
         clickedButton = None # button that was clicked (set to YELLOW, RED, GREEN, or BLUE)
         
         drawButtons()

         scoreSurf = BASICFONT.render('Score: ' + str(score), 1, WHITE)
         scoreRect = scoreSurf.get_rect()
         scoreRect.topleft = (WIDTH - 100, 10)
         DISPLAYSURF.blit(scoreSurf, scoreRect)

         DISPLAYSURF.blit(infoSurf, infoRect) 

        

         



            


            

         checkForQuit()
         for event in pygame.event.get(): # event handling loop
             if event.type == MOUSEBUTTONUP:
                 mousex, mousey = event.pos
                 clickedButton = getButtonClicked(mousex, mousey)
             elif event.type == KEYDOWN:
                 if event.key == K_q:
                     clickedButton = YELLOW
                 elif event.key == K_w:
                     clickedButton = BLUE
                 elif event.key == K_a:
                     clickedButton = RED
                 elif event.key == K_s:
                     clickedButton = GREEN



         if not waitingForInput:
             # play the pattern
             pygame.display.update()
             pygame.time.wait(1000)
             pattern.append(random.choice((YELLOW, BLUE, RED, GREEN)))
             for button in pattern:
                 flashButtonAnimation(button)
                 pygame.time.wait(FLASHDELAY)
             waitingForInput = True
         else:
             # wait for the player to enter buttons
             if clickedButton and clickedButton == pattern[currentStep]:
                 # pushed the correct button
                 flashButtonAnimation(clickedButton)
                 currentStep += 1
                 lastClickTime = time.time()

                 if currentStep == len(pattern):
                     # pushed the last button in the pattern
                     changeBackgroundAnimation()
                     score += 1
                     waitingForInput = False
                     currentStep = 0 # reset back to first step

             elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
                 # pushed the incorrect button, or has timed out
                 gameOverAnimation()
                 # reset the variables for a new game:
                 pattern = []
                 currentStep = 0
                 waitingForInput = False
                 score = 0
                 pygame.time.wait(1000)
                 changeBackgroundAnimation()
                

            

         pygame.display.update()
         FPSCLOCK.tick(FPS)

    
        


 


    def terminate():
     pygame.quit()
     sys.exit()
     
    def checkForQuit():
     for event in pygame.event.get(QUIT): # get all the QUIT events
         terminate() # terminate if any QUIT events are present
     for event in pygame.event.get(KEYUP): # get all the KEYUP events
         if event.key == K_ESCAPE:
           terminate() # terminate if the KEYUP event was for the Esc key
         pygame.event.post(event) # put the other KEYUP event objects back

 
 
 
    def flashButtonAnimation(color, animationSpeed=50):
     if color == YELLOW:
        
         flashColor = BRIGHTYELLOW
         rectangle = YELLOWRECT
        
        
        
        
        
     elif color == BLUE:
        
         flashColor = BRIGHTBLUE
         rectangle = BLUERECT
       
        
     elif color == RED:
        
         flashColor = BRIGHTRED
         rectangle = REDRECT
        
        
     elif color == GREEN:
        
         flashColor = BRIGHTGREEN
         rectangle = GREENRECT
        
        
        

     origSurf = DISPLAYSURF.copy()
     flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
     flashSurf = flashSurf.convert_alpha()
     r, g, b = flashColor
    
     for start, end, step in ((0, 255, 1), (255, 0, -1)): # animation loop
         for alpha in range(start, end, animationSpeed * step):
             checkForQuit()
             DISPLAYSURF.blit(origSurf, (0, 0))
             flashSurf.fill((r, g, b, alpha))
             DISPLAYSURF.blit(flashSurf, rectangle.topleft)
             pygame.display.update()
             FPSCLOCK.tick(FPS)
     DISPLAYSURF.blit(origSurf, (0, 0))

     pygame.display.update()


    def drawButtons():
     pygame.draw.rect(DISPLAYSURF, YELLOW, YELLOWRECT) 
     pygame.draw.rect(DISPLAYSURF, BLUE,   BLUERECT)
     pygame.draw.rect(DISPLAYSURF, RED,    REDRECT)
     pygame.draw.rect(DISPLAYSURF, GREEN,  GREENRECT)
     DISPLAYSURF.blit(im5,(BUTTONSIZE//2-25+YELLOWRECT.x,BUTTONSIZE//2-25+YELLOWRECT.y))
     DISPLAYSURF.blit(im6,(BUTTONSIZE//2-25+BLUERECT.x,BUTTONSIZE//2-25+BLUERECT.y))
     DISPLAYSURF.blit(im7,(BUTTONSIZE//2-25+REDRECT.x,BUTTONSIZE//2-25+REDRECT.y))
     DISPLAYSURF.blit(im8,(BUTTONSIZE//2-25+GREENRECT.x,BUTTONSIZE//2-25+GREENRECT.y))


    def changeBackgroundAnimation(animationSpeed=40):
     global bgColor
     newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

     newBgSurf = pygame.Surface((WIDTH, HEIGHT))
     newBgSurf = newBgSurf.convert_alpha()
     r, g, b = newBgColor
     for alpha in range(0, 255, animationSpeed): # animation loop
         checkForQuit()
         DISPLAYSURF.fill(bgColor)

         newBgSurf.fill((r, g, b, alpha))
         DISPLAYSURF.blit(newBgSurf, (0, 0))

         drawButtons() # redraw the buttons on top of the

         pygame.display.update()
         FPSCLOCK.tick(FPS)
     bgColor = newBgColor








    def gameOverAnimation(color=WHITE, animationSpeed=50):
     # play all beeps at once, then flash the background
     origSurf = DISPLAYSURF.copy()
     flashSurf = pygame.Surface(DISPLAYSURF.get_size())
     flashSurf = flashSurf.convert_alpha()
    
     r, g, b = color
     for i in range(3): # do the flash 3 times
         for start, end, step in ((0, 255, 1), (255, 0, -1)):
             # The first iteration in this loop sets the following for loop
             # to go from 0 to 255, the second from 255 to 0.
             for alpha in range(start, end, animationSpeed * step): # animation loop
                 # alpha means transparency. 255 is opaque, 0 is invisible
                 checkForQuit()
                 flashSurf.fill((r, g, b, alpha))
                 DISPLAYSURF.blit(origSurf, (0, 0))
                 DISPLAYSURF.blit(flashSurf, (0, 0))
                 drawButtons()
                 pygame.display.update()
                 FPSCLOCK.tick(FPS)



    def getButtonClicked(x, y):
     if YELLOWRECT.collidepoint( (x, y) ):
         return YELLOW
     elif BLUERECT.collidepoint( (x, y) ):
         return BLUE
     elif REDRECT.collidepoint( (x, y) ):
         return RED
     elif GREENRECT.collidepoint( (x, y) ):
         return GREEN
     return None


    if __name__ == '__main__':
     main()

Menu(titleMain,messageMenu, True)