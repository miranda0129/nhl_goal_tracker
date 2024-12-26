import pygame
import threading
import time
import queue

# Function to run the Pygame window
def run_pygame(shared_queue):
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pygame Animation with Thread')

    # Set up font
    font = pygame.font.SysFont('Arial', 50)

    # Text settings
    text = "Hello, World!"
    color = (255, 255, 255)
    x, y = 250, 250

    clock = pygame.time.Clock()
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Check for updates from the main thread via the queue
        try:
            new_x = shared_queue.get_nowait()  # Try to get updated position from the queue
            x = new_x  # Update the position if there is new data
        except queue.Empty:
            pass  # If the queue is empty, just continue

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Render and display the text
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

        # Update the screen
        pygame.display.flip()
        clock.tick(30)  # Limit to 30 FPS

    pygame.quit()

# Function to update the animation in the main function
def main():
    # Create a queue for communication between the threads
    shared_queue = queue.Queue()

    # Create and start the Pygame thread
    pygame_thread = threading.Thread(target=run_pygame, args=(shared_queue,))
    pygame_thread.daemon = True  # Daemonize the thread so it exits with the main program
    pygame_thread.start()

    # Simulate the main function sending updated information to Pygame
    x_position = 0
    try:
        while True:
            # Simulate some logic in the main thread (e.g., changing position)
            x_position += 5
            if x_position > 800:
                x_position = -100  # Reset position

            # Send the updated position to the Pygame thread via the queue
            shared_queue.put(x_position)

            time.sleep(0.1)  # Simulate doing other work
    except KeyboardInterrupt:
        print("Main program exiting.")

if __name__ == "__main__":
    main()
