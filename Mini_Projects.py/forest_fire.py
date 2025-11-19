import pygame as pg
import random

# Konstanter
ROWS, COLS = 300, 300
CELL_SIZE = 2
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
FPS = 600

# Celletilstander
DEAD = 0
ACTIVE = 1
BURNED = 2

# Farger
COLORS = {
    DEAD: (0,150,50),    # grønn
    ACTIVE: (255, 0, 0),      # rød
    BURNED: (19, 19, 19)   # svart
}

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.state = DEAD
        self.rect = pg.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

    def draw(self, surface):
        pg.draw.rect(surface, COLORS[self.state], self.rect)

    def ignite(self):
        if self.state == DEAD:
            self.state = ACTIVE

    def burn(self):
        self.state = BURNED

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Simulering i rutenett - pygame")
        self.running = True

        self.grid = [[Cell(r, c) for c in range(COLS)] for r in range(ROWS)]
        """
        self.grid blir en liste med lister hvor hver indre liste er en rad i rutenettet. Denne indre lista inneholder
        like mange celler som verdien til variabelen (konstanten) COLS. Hver celle i denne listen er et Cell-objekt.
        Man kan alternativt skrive en nøstet løkke som gjør det samme.
        """
        
        self.spreading = False

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN and not self.spreading:
                x, y = pg.mouse.get_pos()
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                self.grid[row][col].ignite()
                self.spreading = True

    def update(self):
        if not self.spreading: #Sjekker om simuleringen er aktiv
            return

        new_ignitions = []  #Oppretter liste som skal samle celler som skal antennes
        for r in range(ROWS):  #Nøstet løkke som går gjennom alle cellene i rutenettet
            for c in range(COLS):
                cell = self.grid[r][c] #Oppretter variabelen cell som holder på aktuell celle
                if cell.state == ACTIVE: #Sjekker om det er en celle som brenner (fra forrige runde)
                    cell.burn()  #Endrer status på den brennende cellen til utbrent
                    for dr in [-1, 0, 1]:  #Nøstet løkke som løper gjennom alle nabocellene
                        for dc in [-1, 0, 1]:
                            nr, nc = r + dr, c + dc #nr = radnummer, #cr = kollonne nr for celle som undersøkes
                            if 0 <= nr < ROWS and 0 <= nc < COLS: #skjekker om cellen er innenfor rutenettet
                                neighbor = self.grid[nr][nc] #oppretter variabelen neighbor som inneholder en peker til den aktuelle cellen
                                if neighbor.state == DEAD and random.random() < 0.25: #Sjekker om cellen er 'ubrent' og om den er trukket ut til å brenne
                                    new_ignitions.append(neighbor) #Hvis if-testen slår til legges cellen inn i listen over celler som skal brennes

        for cell in new_ignitions:
            cell.ignite()

        if not new_ignitions:
            self.spreading = False

    def draw(self):
        self.screen.fill("white")
        for row in self.grid:
            for cell in row:
                cell.draw(self.screen)

        # Tegn rutenettlinjer hver 5x5 celler
        for r in range(0, ROWS, 5):
            y = r * CELL_SIZE
            pg.draw.line(self.screen, (0, 0, 0), (0, y), (WIDTH, y), 1)
        for c in range(0, COLS, 5):
            x = c * CELL_SIZE
            pg.draw.line(self.screen, (0, 0, 0), (x, 0), (x, HEIGHT), 1)

        pg.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()

if __name__ == "__main__":
    app = App()
    app.run()