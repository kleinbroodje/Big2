import socket
from cards import *
from threading import Thread


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 5555))


class Player:
    def __init__(self):
        self.hand = "empty"
        self.turn = False
        self.id = "pending"

    def update(self):
        card_num = 0
        if self.hand != "empty":
            for card in self.hand:
                cards[card].update(card_num)
                card_num += 1


def recv_server_msg():
    while True:
        message = client.recv(2048).decode()

        if message.startswith("id"):
            player.id =  int(message.split()[1])
        
        if message.startswith("dealt_cards"):
            player.hand = message.split()[1:14]


def game():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        current_time = pygame.time.get_ticks()
        screen.fill((0, 0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            card_touched = False
            for card in reversed(player.hand):
                if player.hand != "empty" and cards[card].rect.collidepoint(pygame.mouse.get_pos()) and not card_touched:
                    cards[card].touched = True
                    card_touched = True
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        last_click = current_time
                        cards[card].drag = True
                        if current_time - last_click > 200:
                            print(1)
                    
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and current_time - last_click <= 200:
                            cards[card].drag = False
                            if cards[card].clicked == True:
                                cards[card].clicked = False
                            else:
                                cards[card].clicked = True

                elif player.hand != "empty":
                    cards[card].touched = False

        render = font.render(str(player.id), False, (255, 255, 255))
        screen.blit(render, (0, 0))

        player.update()

        pygame.display.update() 


player = Player()

Thread(target=recv_server_msg, daemon=True).start()
game()
pygame.quit()