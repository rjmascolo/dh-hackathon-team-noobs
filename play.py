import librosa
import numpy as np
import pygame
import glob


def clamp(min_value, max_value, value):
    if value < min_value:
        return min_value
    if value > max_value:
        return max_value
    return value


def load_image(name):
    image = pygame.image.load(name)
    return image


class AudioBar:

    def __init__(self, x, y, freq, color, width=50, min_height=10, max_height=100, min_decibel=-80, max_decibel=0):

        self.x, self.y, self.freq = x, y, freq

        self.color = color

        self.width, self.min_height, self.max_height = width, min_height, max_height

        self.height = min_height

        self.min_decibel, self.max_decibel = min_decibel, max_decibel

        self.__decibel_height_ratio = (self.max_height - self.min_height)/(self.max_decibel - self.min_decibel)

    def update(self, dt, decibel):

        desired_height = decibel * self.__decibel_height_ratio + self.max_height

        speed = (desired_height - self.height)/0.1

        self.height += speed * dt

        self.height = clamp(self.min_height, self.max_height, self.height)

    def render(self, screen):

        pygame.draw.rect(screen, self.color, (self.x, self.y + self.max_height - self.height, self.width, self.height))


class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('images/frame_00_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_01_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_02_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_03_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_04_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_05_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_06_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_07_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_08_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_09_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_10_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_11_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_12_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_13_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_14_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_15_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_16_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_17_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_18_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_19_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_20_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_21_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_22_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_23_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_24_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_25_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_26_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_27_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_28_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_29_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_30_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_31_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_32_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_33_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_34_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_35_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_36_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_37_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_38_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_39_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_40_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_41_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_42_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_43_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_44_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_45_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_46_delay-0.03s.gif'))
        self.images.append(load_image('images/frame_47_delay-0.03s.gif'))


        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 64, 64)

    def update(self):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


def main():

    def get_decibel(target_time, freq):
        return spectrogram[int(freq * frequencies_index_ratio)][int(target_time * time_index_ratio)]

    filename = "Sick_Beets.mp3"
    time_series, sample_rate = librosa.load(filename)  # getting information from the file

    # getting a matrix which contains amplitude values according to frequency and time indexes
    stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*4))
    spectrogram = librosa.amplitude_to_db(stft, ref=np.max)  # converting the matrix to decibel matrix
    frequencies = librosa.core.fft_frequencies(n_fft=2048*4)  # getting an array of frequencies

    # getting an array of time periodic
    times = librosa.core.frames_to_time(np.arange(spectrogram.shape[1]), sr=sample_rate, hop_length=512, n_fft=2048*4)
    time_index_ratio = len(times)/times[len(times) - 1]
    frequencies_index_ratio = len(frequencies)/frequencies[len(frequencies)-1]
    pygame.init()
    pygame.display.set_caption('DH NOOBS IN DA HOUSE')
    infoObject = pygame.display.Info()
    screen_w = int(infoObject.current_w/2.5)
    screen_h = int(infoObject.current_w/2.5)

    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)


    # Set up the drawing window
    screen = pygame.display.set_mode([screen_w, screen_h])
    bars = []

    frequencies = np.arange(100, 8000, 100)
    r = len(frequencies)
    width = screen_w/r
    x = (screen_w - width*r)/2

    for c in frequencies:
        bars.append(AudioBar(x, 300, c, (255, 0, 0), max_height=400, width=width))
        x += width

    t = pygame.time.get_ticks()
    getTicksLastFrame = t
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(0)
    background = pygame.image.load('qpoc_by_pride_flags-db316qe_1200x1200.png') # pygame.image.load('images/frame_00_delay-0.03s.gif') # pygame.image.load('IMG_20190218_092018.jpg') # pygame.image.load("dZT0km.gif").convert_alpha()

    # Run until the user asks to quit
    running = True
    while running:
        t = pygame.time.get_ticks()
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calling the 'my_group.update' function calls the 'update' function of all
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        my_group.update()
        my_group.draw(screen)
        pygame.display.flip()

        # Fill the background with white
        screen.fill((0, 0, 0))
        screen.blit(background,(0, 0))
        for b in bars:
            b.update(deltaTime, get_decibel(pygame.mixer.music.get_pos()/1000.0, b.freq))
            b.render(screen)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


if __name__ == '__main__':
    main()

