import pygame

# Initialize Pygame
pygame.init()

# Create the screen, now in fullscreen mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF)

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
current_color = black

# Load a clicking sound
# Make sure you have a click sound (.wav) in the same directory as this script
click_sound = pygame.mixer.Sound('Perc_Castanet_hi.wav')

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Press ESC to exit
                running = False

    # Toggle screen color
    screen.fill(current_color)
    if current_color == black:
        current_color = white
    else:
        current_color = black

    # Play click sound
    click_sound.play()

    # Update the display
    pygame.display.flip()

    # Wait to achieve 40 Hz toggle rate
    pygame.time.delay(25)  # Delay in milliseconds to achieve approximately 40Hz

# Quit Pygame
pygame.quit()
