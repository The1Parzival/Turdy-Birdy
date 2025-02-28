import pygame
import random
import os
from PIL import Image
import time

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen settings with V-Sync enabled
WIDTH = 1728
HEIGHT = 960
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED, vsync=1)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
RED = (255, 0, 0)

# Load images
birdy_image = pygame.image.load("birdy.png").convert_alpha()
birdy_image = pygame.transform.scale(birdy_image, (150, 100))
birdy_image_flipped = pygame.transform.flip(birdy_image, True, False)

turdy_image = pygame.image.load("turdy.png").convert_alpha()
turdy_image = pygame.transform.scale(turdy_image, (30, 30))
big_turdy_image = pygame.transform.scale(turdy_image, (100, 100))
turdy_image_special = pygame.transform.scale(turdy_image, (15, 15))
big_turdy_image_special = pygame.transform.scale(turdy_image, (50, 50))

elon_birdy_image = pygame.image.load("elon_birdy.png").convert_alpha()
elon_birdy_image = pygame.transform.scale(elon_birdy_image, (150, 150))
elon_birdy_image_flipped = pygame.transform.flip(elon_birdy_image, True, False)

parzival_birdy_image = pygame.image.load("parzival_birdy.png").convert_alpha()
parzival_birdy_image = pygame.transform.scale(parzival_birdy_image, (150, 150))
parzival_birdy_image_flipped = pygame.transform.flip(parzival_birdy_image, True, False)

intro_image = pygame.image.load("intro.png").convert()
intro_image = pygame.transform.scale(intro_image, (WIDTH, HEIGHT))

elon_images = []
elon_hit_images = []
elon_images_special = []
elon_hit_images_special = []
for i in range(1, 21):
    img = pygame.image.load(f"elon{i}.png").convert_alpha()
    img = pygame.transform.scale(img, (75, 120))
    elon_images.append(img)
    img_special = pygame.transform.scale(img, (37, 60))
    elon_images_special.append(img_special)
    
    hit_img = pygame.image.load(f"elon_hit{i}.png").convert_alpha()
    hit_img = pygame.transform.scale(hit_img, (200, 200))
    elon_hit_images.append(hit_img)
    hit_img_special = pygame.transform.scale(hit_img, (100, 100))
    elon_hit_images_special.append(hit_img_special)

win_no_cheat_gif = Image.open("win_no_cheat.gif")
win_no_cheat_frames = []
for frame in range(win_no_cheat_gif.n_frames):
    win_no_cheat_gif.seek(frame)
    frame_image = win_no_cheat_gif.convert("RGBA")
    pygame_frame = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, frame_image.mode)
    pygame_frame = pygame.transform.scale(pygame_frame, (WIDTH, HEIGHT))
    win_no_cheat_frames.append(pygame_frame)
win_no_cheat_duration = win_no_cheat_gif.info.get('duration', 100) / 1000

win_idkfa_gif = Image.open("win_idkfa.gif")
win_idkfa_frames = []
for frame in range(win_idkfa_gif.n_frames):
    win_idkfa_gif.seek(frame)
    frame_image = win_idkfa_gif.convert("RGBA")
    pygame_frame = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, frame_image.mode)
    pygame_frame = pygame.transform.scale(pygame_frame, (WIDTH, HEIGHT))
    win_idkfa_frames.append(pygame_frame)
win_idkfa_duration = win_idkfa_gif.info.get('duration', 100) / 1000

win_iddqd_gif = Image.open("win_iddqd.gif")
win_iddqd_frames = []
for frame in range(win_iddqd_gif.n_frames):
    win_iddqd_gif.seek(frame)
    frame_image = win_iddqd_gif.convert("RGBA")
    pygame_frame = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, frame_image.mode)
    pygame_frame = pygame.transform.scale(pygame_frame, (WIDTH, HEIGHT))
    win_iddqd_frames.append(pygame_frame)
win_iddqd_duration = win_iddqd_gif.info.get('duration', 100) / 1000

win_both_gif = Image.open("win_both.gif")
win_both_frames = []
for frame in range(win_both_gif.n_frames):
    win_both_gif.seek(frame)
    frame_image = win_both_gif.convert("RGBA")
    pygame_frame = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, frame_image.mode)
    pygame_frame = pygame.transform.scale(pygame_frame, (WIDTH, HEIGHT))
    win_both_frames.append(pygame_frame)
win_both_duration = win_both_gif.info.get('duration', 100) / 1000

win_parzival_gif = Image.open("win_parzival.gif")
win_parzival_frames = []
for frame in range(win_parzival_gif.n_frames):
    win_parzival_gif.seek(frame)
    frame_image = win_parzival_gif.convert("RGBA")
    pygame_frame = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, frame_image.mode)
    pygame_frame = pygame.transform.scale(pygame_frame, (WIDTH, HEIGHT))
    win_parzival_frames.append(pygame_frame)
win_parzival_duration = win_parzival_gif.info.get('duration', 100) / 1000

win_special_gif = Image.open("win_special.gif")
win_special_frames = []
for frame in range(win_special_gif.n_frames):
    win_special_gif.seek(frame)
    frame_image = win_special_gif.convert("RGBA")
    pygame_frame = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, frame_image.mode)
    pygame_frame = pygame.transform.scale(pygame_frame, (WIDTH, HEIGHT))
    win_special_frames.append(pygame_frame)
win_special_duration = win_special_gif.info.get('duration', 100) / 1000

background_images = []
for i in range(1, 5):
    img = pygame.image.load(f"background{i}.png").convert()
    img = pygame.transform.scale(img, (WIDTH, HEIGHT))
    background_images.append(img)

background_special = pygame.image.load("background_special.png").convert()
background_special = pygame.transform.scale(background_special, (WIDTH, HEIGHT))

background_music_files = []
for i in range(1, 5):
    music = pygame.mixer.Sound(f"background_music{i}.mp3")
    background_music_files.append(music)

background_music_special = pygame.mixer.Sound("background_music_special.mp3")
winner_music = pygame.mixer.Sound("winner_music.mp3")
winner_music_special = pygame.mixer.Sound("winner_music_special.mp3")

barricade_image = pygame.image.load("barricade.png").convert_alpha()
barricade_image = pygame.transform.scale(barricade_image, (150, 150))

barricade_hit_images = []
for i in range(1, 21):
    hit_img = pygame.image.load(f"barricade_hit{i}.png").convert_alpha()
    hit_img = pygame.transform.scale(hit_img, (200, 200))
    barricade_hit_images.append(hit_img)

cheat_idkfa_image = pygame.image.load("cheat_idkfa.png").convert_alpha()
cheat_idkfa_image = pygame.transform.scale(cheat_idkfa_image, (600, 600))

cheat_iddqd_image = pygame.image.load("cheat_iddqd.png").convert_alpha()
cheat_iddqd_image = pygame.transform.scale(cheat_iddqd_image, (600, 600))

cheat_both_image = pygame.image.load("cheat_both.png").convert_alpha()
cheat_both_image = pygame.transform.scale(cheat_both_image, (600, 600))

cheat_parzival_image = pygame.image.load("cheat_parzival.png").convert_alpha()
cheat_parzival_image = pygame.transform.scale(cheat_parzival_image, (1200, 450))

turdy_fire_sound = pygame.mixer.Sound("turdy_fire.mp3")
elon_hit_sound = pygame.mixer.Sound("elon_hit.mp3")
barricade_hit_sound = pygame.mixer.Sound("barricade_hit.mp3")
big_turdy_launch_sound = pygame.mixer.Sound("big_turdy_launch.mp3")
cheat_idkfa_sound = pygame.mixer.Sound("cheat_idkfa_sound.mp3")
cheat_iddqd_sound = pygame.mixer.Sound("cheat_iddqd_sound.mp3")
cheat_both_sound = pygame.mixer.Sound("cheat_both_sound.mp3")
cheat_parzival_sound = pygame.mixer.Sound("cheat_parzival_sound.mp3")

# Game variables
level = 1
highest_level = 1
stage = 1
score = 0
miss_count = 0
total_misses = 0
level_misses = 0
consecutive_hits = 0
turdy_lives = 2
rapid_fire = False
invincible = False
parzival_mode = False
special_mode = False
special_win = False
cheat_sequence = ""
back_sequence = ""
special_sequence = ""
exit_sequence = ""
dot_sequence = ""
cheat_timer = 0
both_cheats_active = False
game_won = False
background_channel = None
current_background_image = background_images[0]
current_elon_images = elon_images
current_elon_hit_images = elon_hit_images
current_turdy_image = turdy_image
current_big_turdy_image = big_turdy_image
clock = pygame.time.Clock()

birdy_x = WIDTH // 2 - birdy_image.get_width() // 2
birdy_y = 50
birdy_speed = 5
birdy_direction = 1
birdy_width = birdy_image.get_width()
birdy_height = birdy_image.get_height()
current_birdy_image = birdy_image

elon_x = WIDTH // 2 - elon_images[0].get_width() // 2
elon_y = HEIGHT - elon_images[0].get_height() - 20
elon_width = elon_images[0].get_width()
elon_height = elon_images[0].get_height()
elon_speed = 0
elon_direction = 1
elon_hit_timer = 0
elon_hit_x = 0

barricade_x = WIDTH // 2 - barricade_image.get_width() // 2
barricade_y = elon_y - 150
barricade_speed = 0
barricade_direction = 1
barricade_width = barricade_image.get_width()
barricade_height = barricade_image.get_height()
barricade_hit_timer = 0
barricade_hit_x = 0

turdies = []
base_turdy_speed = 10
turdy_rotation_speed = 10
turdy_spawn_timer = 0
TURDY_SPAWN_COOLDOWN = 0.066

big_turdy_x = -100
big_turdy_y = -100
big_turdy_speed = -15
big_turdy_active = False
big_turdy_width = big_turdy_image.get_width()
big_turdy_height = big_turdy_image.get_height()
big_turdy_angle = 0

font = pygame.font.Font(None, 36)
win_font = pygame.font.Font(None, 144)
level_font = pygame.font.Font(None, 288)
special_font = pygame.font.Font(None, 200)
flawless_font = pygame.font.Font(None, 144)

screen.blit(intro_image, (0, 0))
pygame.display.flip()
pygame.time.wait(3000)

background_channel = background_music_files[0].play(-1)

def reset_game(new_level, special=False):
    global birdy_x, birdy_y, birdy_speed, birdy_direction, elon_x, elon_y, elon_speed, elon_direction, elon_hit_timer, elon_hit_x
    global barricade_x, barricade_y, barricade_speed, barricade_direction, barricade_hit_timer, barricade_hit_x, turdies
    global big_turdy_x, big_turdy_y, big_turdy_active, score, miss_count, total_misses, level_misses, consecutive_hits, turdy_spawn_timer
    global game_won, background_channel, level, stage, current_birdy_image, highest_level, turdy_lives, current_background_image
    global current_elon_images, current_elon_hit_images, current_turdy_image, current_big_turdy_image, special_mode, elon_width, elon_height, big_turdy_width, big_turdy_height

    elon_width = elon_images[0].get_width()
    elon_height = elon_images[0].get_height()
    big_turdy_width = big_turdy_image.get_width()
    big_turdy_height = big_turdy_image.get_height()

    flawless = (level_misses == 0 and score >= 20 and level < 4 and not special_mode)

    if special:
        screen.fill(BLACK)
        special_text = special_font.render("Special Level Unlocked!", True, RED)
        text_x = WIDTH // 2 - special_text.get_width() // 2
        text_y = HEIGHT // 2 - special_text.get_height() // 2
        screen.blit(special_text, (text_x, text_y))
        pygame.display.flip()
        pygame.time.wait(2000)
    elif not game_won:
        screen.fill(BLACK)
        level_text = level_font.render(f"Level {new_level}", True, RED)
        text_x = WIDTH // 2 - level_text.get_width() // 2
        text_y = HEIGHT // 2
        if flawless:
            flawless_text = flawless_font.render("Flawless Victory", True, RED)
            flawless_x = WIDTH // 2 - flawless_text.get_width() // 2
            flawless_y = HEIGHT // 2 - level_text.get_height() // 2 - flawless_text.get_height() - 20
            screen.blit(flawless_text, (flawless_x, flawless_y))
        screen.blit(level_text, (text_x, text_y))
        pygame.display.flip()
        pygame.time.wait(2000)

    if new_level > highest_level:
        highest_level = new_level
    level = new_level
    stage = 1
    score = 0
    if not special:
        total_misses += level_misses
    miss_count = 0
    level_misses = 0
    special_mode = special

    if level == 1 or special_mode:
        birdy_x = WIDTH // 2 - birdy_width // 2
        birdy_y = 50
        birdy_direction = 1
        elon_x = WIDTH // 2 - (37 if special_mode and elon_images_special[0] else elon_width) // 2
        elon_y = HEIGHT - (60 if special_mode and elon_images_special[0] else elon_height) - 20
        barricade_x = WIDTH // 2 - barricade_width // 2
        barricade_y = elon_y - barricade_height
    elif level == 2:
        birdy_x = 20
        birdy_y = HEIGHT // 2 - birdy_height // 2
        birdy_direction = 1
        elon_x = WIDTH - elon_width - 20
        elon_y = HEIGHT // 2 - elon_height // 2
        barricade_x = elon_x - barricade_width - 10
        barricade_y = HEIGHT // 2 - barricade_height // 2
    elif level == 3:
        birdy_x = WIDTH - birdy_width - 20
        birdy_y = HEIGHT // 2 - birdy_height // 2
        birdy_direction = 1
        elon_x = 20
        elon_y = HEIGHT // 2 - elon_height // 2
        barricade_x = elon_x + elon_width + 10
        barricade_y = HEIGHT // 2 - barricade_height // 2
    elif level == 4:
        birdy_x = WIDTH // 2 - birdy_width // 2
        birdy_y = HEIGHT - birdy_height - 50
        birdy_direction = 1
        elon_x = WIDTH // 2 - elon_width // 2
        elon_y = 20
        barricade_x = WIDTH // 2 - barricade_width // 2
        barricade_y = elon_y + elon_height + 10

    birdy_speed = 5
    elon_speed = 0
    elon_direction = 1
    elon_hit_timer = 0
    elon_hit_x = 0
    barricade_speed = 0
    barricade_direction = 1
    barricade_hit_timer = 0
    barricade_hit_x = 0
    turdies = []
    big_turdy_x = -100
    big_turdy_y = -100
    big_turdy_active = False
    consecutive_hits = 0
    turdy_spawn_timer = 0
    cheat_timer = 0
    game_won = False
    
    if parzival_mode:
        turdy_lives = 5
    elif both_cheats_active:
        turdy_lives = 4
    elif rapid_fire:
        turdy_lives = 3
    elif invincible:
        turdy_lives = 2
    else:
        turdy_lives = 2

    if parzival_mode:
        current_birdy_image = parzival_birdy_image_flipped if level == 3 else parzival_birdy_image
    elif rapid_fire and invincible:
        current_birdy_image = elon_birdy_image_flipped if level == 3 else elon_birdy_image
    else:
        current_birdy_image = birdy_image_flipped if level == 3 else birdy_image

    if special_mode:
        current_background_image = background_special
        current_elon_images = elon_images_special
        current_elon_hit_images = elon_hit_images_special
        current_turdy_image = turdy_image_special
        current_big_turdy_image = big_turdy_image_special
        elon_width = elon_images_special[0].get_width()
        elon_height = elon_images_special[0].get_height()
        big_turdy_width = big_turdy_image_special.get_width()
        big_turdy_height = big_turdy_image_special.get_height()
    else:
        current_background_image = background_images[level - 1]
        current_elon_images = elon_images
        current_elon_hit_images = elon_hit_images
        current_turdy_image = turdy_image
        current_big_turdy_image = big_turdy_image
        elon_width = elon_images[0].get_width()
        elon_height = elon_images[0].get_height()
        big_turdy_width = big_turdy_image.get_width()
        big_turdy_height = big_turdy_image.get_height()

    if background_channel:
        background_channel.stop()
    if special_mode:
        background_channel = background_music_special.play(-1)
    else:
        background_channel = background_music_files[level - 1].play(-1)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_i, pygame.K_d, pygame.K_k, pygame.K_f, pygame.K_a, pygame.K_q, pygame.K_p, pygame.K_r, pygame.K_z, pygame.K_v, pygame.K_l, pygame.K_h, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_y]:
                cheat_sequence += chr(event.key).lower()
                if "idkfa" in cheat_sequence:
                    rapid_fire = True
                    turdy_lives = 3
                    cheat_timer = 3
                    cheat_sequence = ""
                    cheat_idkfa_sound.play()
                    if invincible and not parzival_mode:
                        both_cheats_active = True
                        turdy_lives = 4
                        cheat_both_sound.play()
                elif "iddqd" in cheat_sequence:
                    invincible = True
                    turdy_lives = 2
                    cheat_timer = 3
                    cheat_sequence = ""
                    cheat_iddqd_sound.play()
                    if rapid_fire and not parzival_mode:
                        both_cheats_active = True
                        turdy_lives = 4
                        cheat_both_sound.play()
                elif "parzival" in cheat_sequence:
                    rapid_fire = True
                    invincible = True
                    parzival_mode = True
                    turdy_lives = 5
                    cheat_timer = 3
                    cheat_sequence = ""
                    cheat_parzival_sound.play()
                    both_cheats_active = False
                elif "halliday1" in cheat_sequence:
                    reset_game(1)
                    cheat_sequence = ""
                    print("Cheat: Jumped to Level 1")
                elif "halliday2" in cheat_sequence:
                    reset_game(2)
                    cheat_sequence = ""
                    print("Cheat: Jumped to Level 2")
                elif "halliday3" in cheat_sequence:
                    reset_game(3)
                    cheat_sequence = ""
                    print("Cheat: Jumped to Level 3")
                elif "halliday4" in cheat_sequence:
                    reset_game(4)
                    cheat_sequence = ""
                    print("Cheat: Jumped to Level 4")
            if event.key == pygame.K_b:
                back_sequence = "b"
            elif back_sequence == "b" and event.key == pygame.K_a:
                back_sequence = "ba"
            elif back_sequence == "ba" and event.key == pygame.K_c:
                back_sequence = "bac"
            elif back_sequence == "bac" and event.key == pygame.K_k:
                if level > 1 and not special_mode:
                    print("BACK sequence completed, dropping level")
                    reset_game(level - 1)
                back_sequence = ""
            else:
                back_sequence = ""
            
            if game_won and event.key in [pygame.K_s, pygame.K_p, pygame.K_e, pygame.K_c, pygame.K_i, pygame.K_a, pygame.K_l]:
                special_sequence += chr(event.key).lower()
                if "special" in special_sequence:
                    print("Special level activated!")
                    reset_game(1, special=True)
                    special_sequence = ""
            elif game_won:
                special_sequence = ""

            if special_mode and event.key in [pygame.K_e, pygame.K_x, pygame.K_i, pygame.K_t]:
                exit_sequence += chr(event.key).lower()
                if "exit" in exit_sequence:
                    print("Exiting special level!")
                    if background_channel:
                        background_channel.stop()
                    time.sleep(0.1)
                    winner_music.play(-1)
                    game_won = True
                    special_mode = False
                    level = 4
                    stage = 20
                    exit_sequence = ""
            elif special_mode:
                exit_sequence = ""

            if special_mode and stage >= 20 and event.key in [pygame.K_d, pygame.K_o, pygame.K_t]:
                dot_sequence += chr(event.key).lower()
                if "dot" in dot_sequence:
                    print("Special level win activated!")
                    if background_channel:
                        background_channel.stop()
                    time.sleep(0.1)
                    winner_music_special.play(-1)
                    special_win = True
                    dot_sequence = ""
            elif special_mode and stage >= 20:
                dot_sequence = ""

            if game_won and event.key == pygame.K_n and level == 4 and stage == 20 and not special_mode:
                winner_music.stop()
                print("Winner music stopped.")
                reset_game(1)

    if not game_won and not special_win:
        turdy_spawn_timer -= 1 / 60
        if turdy_spawn_timer < 0:
            turdy_spawn_timer = 0

        if score < 19:
            birdy_speed = 5 + score * 2
        else:
            birdy_speed = 50 + (score - 18) * 50

        turdy_speed = base_turdy_speed * 1.2 if level in [2, 3] else base_turdy_speed

        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:
            if rapid_fire and turdy_spawn_timer <= 0:
                if level == 1 or special_mode:
                    turdies.append([birdy_x + birdy_width // 2 - current_turdy_image.get_width() // 2, birdy_y + birdy_height, 0, True])
                elif level == 2:
                    turdies.append([birdy_x + birdy_width, birdy_y + birdy_height // 2 - current_turdy_image.get_height() // 2, 0, True])
                elif level == 3:
                    turdies.append([birdy_x - current_turdy_image.get_width(), birdy_y + birdy_height // 2 - current_turdy_image.get_height() // 2, 0, True])
                elif level == 4:
                    turdies.append([birdy_x + birdy_width // 2 - current_turdy_image.get_width() // 2, birdy_y - current_turdy_image.get_height(), 0, True])
                turdy_spawn_timer = TURDY_SPAWN_COOLDOWN
                turdy_fire_sound.play()
            elif not any(t[3] for t in turdies):
                if level == 1 or special_mode:
                    turdies.append([birdy_x + birdy_width // 2 - current_turdy_image.get_width() // 2, birdy_y + birdy_height, 0, True])
                elif level == 2:
                    turdies.append([birdy_x + birdy_width, birdy_y + birdy_height // 2 - current_turdy_image.get_height() // 2, 0, True])
                elif level == 3:
                    turdies.append([birdy_x - current_turdy_image.get_width(), birdy_y + birdy_height // 2 - current_turdy_image.get_height() // 2, 0, True])
                elif level == 4:
                    turdies.append([birdy_x + birdy_width // 2 - current_turdy_image.get_width() // 2, birdy_y - current_turdy_image.get_height(), 0, True])
                turdy_fire_sound.play()

        prev_direction = birdy_direction
        if level in [1, 4] or special_mode:
            birdy_x += birdy_speed * birdy_direction
            if birdy_x > WIDTH - birdy_width or birdy_x < 0:
                birdy_direction *= -1
        elif level in [2, 3]:
            birdy_y += birdy_speed * birdy_direction
            if birdy_y > HEIGHT - birdy_height or birdy_y < 0:
                birdy_direction *= -1

        if level == 1 or level == 4 or special_mode:
            if parzival_mode:
                current_birdy_image = parzival_birdy_image if birdy_direction > 0 else parzival_birdy_image_flipped
            elif rapid_fire and invincible:
                current_birdy_image = elon_birdy_image if birdy_direction > 0 else elon_birdy_image_flipped
            else:
                current_birdy_image = birdy_image if birdy_direction > 0 else birdy_image_flipped
        elif level == 2:
            if parzival_mode:
                current_birdy_image = parzival_birdy_image
            elif rapid_fire and invincible:
                current_birdy_image = elon_birdy_image
            else:
                current_birdy_image = birdy_image
        elif level == 3:
            if parzival_mode:
                current_birdy_image = parzival_birdy_image_flipped
            elif rapid_fire and invincible:
                current_birdy_image = elon_birdy_image_flipped
            else:
                current_birdy_image = birdy_image_flipped

        if score >= 10:
            elon_speed = (score - 9) * 2
            if level in [1, 4] or special_mode:
                elon_x += elon_speed * elon_direction
                if elon_x > WIDTH - elon_width or elon_x < 0:
                    elon_direction *= -1
            elif level in [2, 3]:
                elon_y += elon_speed * elon_direction
                if elon_y > HEIGHT - elon_height or elon_y < 0:
                    elon_direction *= -1

        if score >= 5:
            barricade_speed = (score - 4) * 2
            if level in [1, 4] or special_mode:
                barricade_x += barricade_speed * barricade_direction
                if barricade_x > WIDTH - barricade_width or barricade_x < 0:
                    barricade_direction *= -1
            elif level in [2, 3]:
                barricade_y += barricade_speed * barricade_direction
                if barricade_y > HEIGHT - barricade_height or barricade_y < 0:
                    barricade_direction *= -1

        if elon_hit_timer > 0:
            elon_hit_timer -= 1 / 60
        if barricade_hit_timer > 0:
            barricade_hit_timer -= 1 / 60
        if cheat_timer > 0:
            cheat_timer -= 1 / 60

        for turdy in turdies[:]:
            if turdy[3]:
                if level == 1 or special_mode:
                    turdy[1] += turdy_speed
                elif level == 2:
                    turdy[0] += turdy_speed
                elif level == 3:
                    turdy[0] -= turdy_speed
                elif level == 4:
                    turdy[1] -= turdy_speed
                
                turdy[2] = (turdy[2] + turdy_rotation_speed) % 360
                
                rotated_turdy = pygame.transform.rotate(current_turdy_image, turdy[2])
                turdy_width = rotated_turdy.get_width()
                turdy_height = rotated_turdy.get_height()
                turdy_rect = rotated_turdy.get_rect(center=(int(turdy[0] + turdy_width // 2), int(turdy[1] + turdy_height // 2)))

                if turdy_rect.colliderect(pygame.Rect(elon_x, elon_y, elon_width, elon_height)):
                    consecutive_hits += 1
                    if consecutive_hits >= 4 and not big_turdy_active:
                        if level == 1 or special_mode:
                            big_turdy_x = elon_x + elon_width // 2 - big_turdy_width // 2
                            big_turdy_y = elon_y
                        elif level == 2:
                            big_turdy_x = elon_x
                            big_turdy_y = elon_y + elon_height // 2 - big_turdy_height // 2
                        elif level == 3:
                            big_turdy_x = elon_x + elon_width
                            big_turdy_y = elon_y + elon_height // 2 - big_turdy_height // 2
                        elif level == 4:
                            big_turdy_x = elon_x + elon_width // 2 - big_turdy_width // 2
                            big_turdy_y = elon_y + elon_height
                        big_turdy_active = True
                        consecutive_hits = 0
                        big_turdy_launch_sound.play()
                    
                    score += 1
                    turdy_lives = 2 if not (parzival_mode or both_cheats_active or rapid_fire or invincible) else turdy_lives
                    elon_hit_sound.play()
                    turdy[3] = False
                    stage = min(score + 1, 20)
                    elon_width = current_elon_images[min(score, 19)].get_width()
                    elon_height = current_elon_images[min(score, 19)].get_height()
                    if level == 1 or special_mode:
                        elon_x = max(0, min(elon_x, WIDTH - elon_width))
                        elon_y = HEIGHT - elon_height - 20
                        barricade_y = elon_y - barricade_height
                    elif level == 2:
                        elon_x = WIDTH - elon_width - 20
                        elon_y = max(0, min(elon_y, HEIGHT - elon_height))
                        barricade_x = elon_x - barricade_width - 10
                    elif level == 3:
                        elon_x = 20
                        elon_y = max(0, min(elon_y, HEIGHT - elon_height))
                        barricade_x = elon_x + elon_width + 10
                    elif level == 4:
                        elon_x = max(0, min(elon_x, WIDTH - elon_width))
                        elon_y = 20
                        barricade_y = elon_y + elon_height + 10
                    elon_hit_timer = 1.0
                    hit_width = current_elon_hit_images[min(score-1, 19)].get_width()
                    hit_height = current_elon_hit_images[min(score-1, 19)].get_height()
                    if level in [1, 4] or special_mode:
                        elon_hit_x = elon_x + elon_width + 10 if elon_direction < 0 else elon_x - hit_width - 10
                        elon_hit_x = max(0, min(elon_hit_x, WIDTH - hit_width))
                    elif level in [2, 3]:
                        elon_hit_y = elon_y + elon_height + 10 if elon_direction < 0 else elon_y - hit_height - 10
                        elon_hit_x = elon_x + (elon_width - hit_width) // 2
                        elon_hit_x = max(0, min(elon_hit_x, WIDTH - hit_width))
                        elon_hit_y = max(0, min(elon_hit_y, HEIGHT - hit_height))

                elif (level == 1 and turdy[1] > HEIGHT) or \
                     (special_mode and turdy[1] > HEIGHT) or \
                     (level == 2 and turdy[0] > WIDTH) or \
                     (level == 3 and turdy[0] < -turdy_width) or \
                     (level == 4 and turdy[1] < -turdy_height):
                    turdy[3] = False
                    miss_count += 1
                    level_misses += 1
                    consecutive_hits = 0
                    if not (parzival_mode or both_cheats_active or rapid_fire or invincible):
                        turdy_lives = max(0, turdy_lives - 1)
                        if turdy_lives <= 0:
                            score = max(0, score - 1)
                            stage = min(score + 1, 20)
                            turdy_lives = 2
                            consecutive_hits = 0
                            elon_speed = max(0, (score - 9) * 2) if score >= 10 else 0
                            barricade_speed = max(0, (score - 4) * 2) if score >= 5 else 0
                            elon_width = current_elon_images[min(score, 19)].get_width()
                            elon_height = current_elon_images[min(score, 19)].get_height()
                            if level == 1 or special_mode:
                                elon_x = max(0, min(elon_x, WIDTH - elon_width))
                                elon_y = HEIGHT - elon_height - 20
                                barricade_y = elon_y - barricade_height
                            elif level == 2:
                                elon_x = WIDTH - elon_width - 20
                                elon_y = max(0, min(elon_y, HEIGHT - elon_height))
                                barricade_x = elon_x - barricade_width - 10
                            elif level == 3:
                                elon_x = 20
                                elon_y = max(0, min(elon_y, HEIGHT - elon_height))
                                barricade_x = elon_x + elon_width + 10
                            elif level == 4:
                                elon_x = max(0, min(elon_x, WIDTH - elon_width))
                                elon_y = 20
                                barricade_y = elon_y + elon_height + 10

                elif (score >= 5 and 
                      turdy_rect.colliderect(pygame.Rect(barricade_x, barricade_y, barricade_width, barricade_height))):
                    turdy[3] = False
                    miss_count += 1
                    level_misses += 1
                    consecutive_hits = 0
                    barricade_hit_sound.play()
                    barricade_hit_timer = 1.0
                    hit_width = barricade_hit_images[min(score-1, 19)].get_width()
                    hit_height = barricade_hit_images[min(score-1, 19)].get_height()
                    if level in [1, 4] or special_mode:
                        barricade_hit_x = barricade_x + barricade_width + 10 if barricade_direction < 0 else barricade_x - hit_width - 10
                        barricade_hit_x = max(0, min(barricade_hit_x, WIDTH - hit_width))
                    elif level in [2, 3]:
                        barricade_hit_y = barricade_y + barricade_height + 10 if barricade_direction < 0 else barricade_y - hit_height - 10
                        barricade_hit_x = barricade_x + (barricade_width - hit_width) // 2
                        barricade_hit_x = max(0, min(barricade_hit_x, WIDTH - hit_width))
                        barricade_hit_y = max(0, min(barricade_hit_y, HEIGHT - hit_height))
                    if not (parzival_mode or both_cheats_active or rapid_fire or invincible):
                        turdy_lives = max(0, turdy_lives - 1)
                        if turdy_lives <= 0:
                            score = max(0, score - 1)
                            stage = min(score + 1, 20)
                            turdy_lives = 2
                            consecutive_hits = 0
                            elon_speed = max(0, (score - 9) * 2) if score >= 10 else 0
                            barricade_speed = max(0, (score - 4) * 2) if score >= 5 else 0
                            elon_width = current_elon_images[min(score, 19)].get_width()
                            elon_height = current_elon_images[min(score, 19)].get_height()
                            if level == 1 or special_mode:
                                elon_x = max(0, min(elon_x, WIDTH - elon_width))
                                elon_y = HEIGHT - elon_height - 20
                                barricade_y = elon_y - barricade_height
                            elif level == 2:
                                elon_x = WIDTH - elon_width - 20
                                elon_y = max(0, min(elon_y, HEIGHT - elon_height))
                                barricade_x = elon_x - barricade_width - 10
                            elif level == 3:
                                elon_x = 20
                                elon_y = max(0, min(elon_y, HEIGHT - elon_height))
                                barricade_x = elon_x + elon_width + 10
                            elif level == 4:
                                elon_x = max(0, min(elon_x, WIDTH - elon_width))
                                elon_y = 20
                                barricade_y = elon_y + elon_height + 10

        if big_turdy_active:
            if level == 1 or special_mode:
                big_turdy_y += big_turdy_speed
            elif level == 2:
                big_turdy_x += big_turdy_speed
            elif level == 3:
                big_turdy_x -= big_turdy_speed
            elif level == 4:
                big_turdy_y -= big_turdy_speed
            
            big_turdy_angle = (big_turdy_angle + turdy_rotation_speed) % 360
            
            rotated_big_turdy = pygame.transform.rotate(current_big_turdy_image, big_turdy_angle)
            big_turdy_width = rotated_big_turdy.get_width()
            big_turdy_height = rotated_big_turdy.get_height()
            big_turdy_rect = rotated_big_turdy.get_rect(center=(big_turdy_x + big_turdy_width // 2, big_turdy_y + big_turdy_height // 2))

            if big_turdy_rect.colliderect(pygame.Rect(birdy_x, birdy_y, birdy_width, birdy_height)) and not invincible:
                score = max(0, score - 1)
                stage = min(score + 1, 20)
                big_turdy_active = False
                consecutive_hits = 0
                level_misses += 1
                elon_speed = max(0, (score - 9) * 2) if score >= 10 else 0
                barricade_speed = max(0, (score - 4) * 2) if score >= 5 else 0
                elon_width = current_elon_images[min(score, 19)].get_width()
                elon_height = current_elon_images[min(score, 19)].get_height()
                if level == 1 or special_mode:
                    elon_x = max(0, min(elon_x, WIDTH - elon_width))
                    elon_y = HEIGHT - elon_height - 20
                    barricade_y = elon_y - barricade_height
                elif level == 2:
                    elon_x = WIDTH - elon_width - 20
                    elon_y = max(0, min(elon_y, HEIGHT - elon_height))
                    barricade_x = elon_x - barricade_width - 10
                elif level == 3:
                    elon_x = 20
                    elon_y = max(0, min(elon_y, HEIGHT - elon_height))
                    barricade_x = elon_x + elon_width + 10
                elif level == 4:
                    elon_x = max(0, min(elon_x, WIDTH - elon_width))
                    elon_y = 20
                    barricade_y = elon_y + elon_height + 10
            elif invincible and big_turdy_rect.colliderect(pygame.Rect(birdy_x, birdy_y, birdy_width, birdy_height)):
                big_turdy_active = False
            
            if ((level == 1 or special_mode) and big_turdy_y < -big_turdy_height) or \
               (level == 2 and big_turdy_x < -big_turdy_width) or \
               (level == 3 and big_turdy_x > WIDTH) or \
               (level == 4 and big_turdy_y > HEIGHT):
                big_turdy_active = False

        if score >= 20 and level < 4 and not special_mode:
            reset_game(level + 1)
            print(f"Advanced to Level {level}")

        if level == 4 and stage == 20 and not special_mode:
            background_channel.stop()
            print("Background music stopped.")
            time.sleep(0.1)
            print("Attempting to play winner_music.mp3")
            winner_music.play(-1)
            total_misses += level_misses
            game_won = True

    if not game_won and not special_win:
        screen.blit(current_background_image, (0, 0))
        screen.blit(current_birdy_image, (birdy_x, birdy_y))
        
        if score >= 5:
            screen.blit(barricade_image, (barricade_x, barricade_y))
            if barricade_hit_timer > 0:
                hit_width = barricade_hit_images[min(score-1, 19)].get_width()
                hit_height = barricade_hit_images[min(score-1, 19)].get_height()
                if level in [1, 4] or special_mode:
                    hit_y = barricade_y + (barricade_height - hit_height) // 2
                    hit_x = barricade_hit_x
                    screen.blit(barricade_hit_images[min(score-1, 19)], (hit_x, hit_y))
                elif level in [2, 3]:
                    hit_x = barricade_hit_x
                    hit_y = barricade_hit_y
                    screen.blit(barricade_hit_images[min(score-1, 19)], (hit_x, hit_y))
        
        screen.blit(current_elon_images[min(score, 19)], (elon_x, elon_y))
        if elon_hit_timer > 0:
            hit_width = current_elon_hit_images[min(score-1, 19)].get_width()
            hit_height = current_elon_hit_images[min(score-1, 19)].get_height()
            if level in [1, 4] or special_mode:
                hit_y = elon_y + (elon_height - hit_height) // 2
                hit_x = elon_hit_x
                screen.blit(current_elon_hit_images[min(score-1, 19)], (hit_x, hit_y))
            elif level in [2, 3]:
                hit_x = elon_hit_x
                hit_y = elon_hit_y
                screen.blit(current_elon_hit_images[min(score-1, 19)], (hit_x, hit_y))
        
        for turdy in turdies:
            if turdy[3]:
                rotated_turdy = pygame.transform.rotate(current_turdy_image, turdy[2])
                turdy_width = rotated_turdy.get_width()
                turdy_height = rotated_turdy.get_height()
                turdy_rect = rotated_turdy.get_rect(center=(int(turdy[0] + turdy_width // 2), int(turdy[1] + turdy_height // 2)))
                screen.blit(rotated_turdy, turdy_rect.topleft)
        
        if big_turdy_active:
            screen.blit(rotated_big_turdy, big_turdy_rect.topleft)
        
        score_text = font.render(f"Special Level  Stage: {stage}" if special_mode else f"Level: {level}  Stage: {stage}", True, RED if special_mode else BLACK)
        screen.blit(score_text, (10, 10))
        
        text_width = score_text.get_width()
        turdy_x = 10 + text_width + 10
        for i in range(turdy_lives):
            screen.blit(turdy_image, (turdy_x + i * 40, 10))

        if cheat_timer > 0:
            if parzival_mode:
                cheat_x = WIDTH // 2 - cheat_parzival_image.get_width() // 2
                cheat_y = HEIGHT // 2 - cheat_parzival_image.get_height() // 2
                screen.blit(cheat_parzival_image, (cheat_x, cheat_y))
            elif both_cheats_active and not parzival_mode:
                cheat_x = WIDTH // 2 - cheat_both_image.get_width() // 2
                cheat_y = HEIGHT // 2 - cheat_both_image.get_height() // 2
                screen.blit(cheat_both_image, (cheat_x, cheat_y))
            elif rapid_fire and not invincible:
                cheat_x = WIDTH // 2 - cheat_idkfa_image.get_width() // 2
                cheat_y = HEIGHT // 2 - cheat_idkfa_image.get_height() // 2
                screen.blit(cheat_idkfa_image, (cheat_x, cheat_y))
            elif invincible and not rapid_fire:
                cheat_x = WIDTH // 2 - cheat_iddqd_image.get_width() // 2
                cheat_y = HEIGHT // 2 - cheat_iddqd_image.get_height() // 2
                screen.blit(cheat_iddqd_image, (cheat_x, cheat_y))

    if game_won:
        if parzival_mode:
            frame_index = (pygame.time.get_ticks() // int(win_parzival_duration * 1000)) % len(win_parzival_frames)
            screen.blit(win_parzival_frames[frame_index], (0, 0))
        elif both_cheats_active:
            frame_index = (pygame.time.get_ticks() // int(win_both_duration * 1000)) % len(win_both_frames)
            screen.blit(win_both_frames[frame_index], (0, 0))
        elif rapid_fire:
            frame_index = (pygame.time.get_ticks() // int(win_idkfa_duration * 1000)) % len(win_idkfa_frames)
            screen.blit(win_idkfa_frames[frame_index], (0, 0))
        elif invincible:
            frame_index = (pygame.time.get_ticks() // int(win_iddqd_duration * 1000)) % len(win_iddqd_frames)
            screen.blit(win_iddqd_frames[frame_index], (0, 0))
        else:
            frame_index = (pygame.time.get_ticks() // int(win_no_cheat_duration * 1000)) % len(win_no_cheat_frames)
            screen.blit(win_no_cheat_frames[frame_index], (0, 0))
        
        if total_misses == 0 and not special_mode:
            perfect_text = win_font.render("Gamer Extraordinaire", True, RED)
            perfect_x = WIDTH // 2 - perfect_text.get_width() // 2
            perfect_y = HEIGHT // 2 - perfect_text.get_height() // 2
            screen.blit(perfect_text, (perfect_x, perfect_y))
        
        win_text = win_font.render("Thanks for playing my game!", True, RED)
        text_x = WIDTH // 2 - win_text.get_width() // 2
        text_y = HEIGHT - win_text.get_height() - 20
        screen.blit(win_text, (text_x, text_y))

    if special_win:
        frame_index = (pygame.time.get_ticks() // int(win_special_duration * 1000)) % len(win_special_frames)
        screen.blit(win_special_frames[frame_index], (0, 0))
        
        win_text = win_font.render("Thanks for playing my game!", True, RED)
        text_x = WIDTH // 2 - win_text.get_width() // 2
        text_y = HEIGHT - win_text.get_height() - 20
        screen.blit(win_text, (text_x, text_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()