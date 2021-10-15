import pygame

from Life.Greedy import Cells

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Changes these variables to change GUI
DRAW_GRID = True
GRID_GIRTH = 1
GRID_COLOR = (100, 100, 100)
CELL_COLOR = (255, 255, 255)

# OPTIONAL TEXT
DRAW_CELL_TEXT = False
CELL_TEXT_FONT = 'Arial'
# FONTS = ['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambriacambriamath', 'cambria', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhengheimicrosoftjhengheiui', 'microsoftjhengheimicrosoftjhengheiuibold', 'microsoftjhengheimicrosoftjhengheiuilight', 'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyaheimicrosoftyaheiui', 'microsoftyaheimicrosoftyaheiuibold', 'microsoftyaheimicrosoftyaheiuilight', 'microsoftyibaiti', 'mingliuextbpmingliuextbmingliuhkscsextb', 'mongolianbaiti', 'msgothicmsuigothicmspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsunnsimsun', 'simsunextb', 'sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner', 'sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold', 'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic', 'sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 'yugothicyugothicuisemiboldyugothicuibold', 'yugothicyugothicuilight', 'yugothicmediumyugothicuiregular', 'yugothicregularyugothicuisemilight', 'holomdl2assets', 'aharoni', 'david', 'frankruehl', 'gisha', 'levenim', 'miriam', 'miriamfixed', 'narkisim', 'rod', 'caladea', 'emojionecolorsvginot', 'scheherazade', 'liberationmono', 'amiri', 'linuxbiolinumg', 'notokufiarabic', 'gentiumbasic', 'sourcecodeproblack', 'sourcesansproblack', 'davidlibre', 'davidclm', 'liberationsans', 'sourceserifproblack', 'alef', 'kacstbook', 'reemkufiregular', 'carlito', 'dejavumathtexgyreregular', 'opensymbol', 'alefregular', 'amirislanted', 'amiriquran', 'davidclmmedium', 'frankruehlclm', 'frankruehlclmoblique', 'frankruehlclmmedium', 'frankruehlclmmediumoblique', 'miriamclm', 'miriamclmbook', 'miriammonoclm', 'miriammonoclmoblique', 'miriammonoclmbook', 'miriammonoclmbookoblique', 'nachlieliclm', 'nachlieliclmoblique', 'dejavusans', 'dejavusansoblique', 'dejavusansextralight', 'dejavusanscondensed', 'dejavusanscondensedoblique', 'dejavusansmono', 'dejavusansmonooblique', 'dejavuserif', 'dejavuserifcondensed', 'gentiumbookbasic', 'kacstoffice', 'liberationserif', 'linuxbiolinumgregular', 'linuxlibertinegdisplayregular', 'linuxlibertineg', 'linuxlibertinegsemibold', 'linuxlibertinegregular', 'davidlibreregular', 'frankruhlhofshi', 'frankruhlhofshiregular', 'miriamlibre', 'miriamlibreregular', 'rubikbold', 'rubik', 'rubikregular', 'notomono', 'notonaskharabic', 'notonaskharabicui', 'notosans', 'notosanscondensed', 'notosansregular', 'notosansarabic', 'notosansarabicregular', 'notosansarabicui', 'notosansarabicuiregular', 'notosansarmenian', 'notosansarmenianregular', 'notosansgeorgian', 'notosansgeorgianregular', 'notosanshebrew', 'notosanshebrewregular', 'notosanslao', 'notosanslaoregular', 'notosanslisuregular', 'notoserif', 'notoserifcondensed', 'notoserifregular', 'notoserifarmenian', 'notoserifarmenianregular', 'notoserifgeorgian', 'notoserifgeorgianregular', 'notoserifhebrew', 'notoserifhebrewregular', 'notoseriflao', 'notoseriflaoregular', 'sourcecodepro', 'sourcecodeproextralight', 'sourcecodepromedium', 'sourcecodeprosemibold', 'sourcesanspro', 'sourcesansproextralight', 'sourcesansprosemibold', 'sourceserifpro', 'sourceserifproextralight', 'sourceserifprosemibold', 'teamviewer15', 'agencyfb', 'algerian', 'bookantiqua', 'arialrounded', 'baskervilleoldface', 'bauhaus93', 'bell', 'bernardcondensed', 'bodoni', 'bodoniblack', 'bodonicondensed', 'bodonipostercompressed', 'bookmanoldstyle', 'bradleyhanditc', 'britannic', 'berlinsansfb', 'berlinsansfbdemi', 'broadway', 'brushscript', 'bookshelfsymbol7', 'californianfb', 'calisto', 'castellar', 'centuryschoolbook', 'centaur', 'century', 'chiller', 'colonna', 'cooperblack', 'copperplategothic', 'curlz', 'dubai', 'dubaimedium', 'dubairegular', 'elephant', 'engravers', 'erasitc', 'erasdemiitc', 'erasmediumitc', 'felixtitling', 'forte', 'franklingothicbook', 'franklingothicdemi', 'franklingothicdemicond', 'franklingothicheavy', 'franklingothicmediumcond', 'freestylescript', 'frenchscript', 'footlight', 'garamond', 'gigi', 'gillsans', 'gillsanscondensed', 'gillsansultracondensed', 'gillsansultra', 'gloucesterextracondensed', 'gillsansextcondensed', 'centurygothic', 'goudyoldstyle', 'goudystout', 'harlowsolid', 'harrington', 'haettenschweiler', 'hightowertext', 'imprintshadow', 'informalroman', 'blackadderitc', 'edwardianscriptitc', 'kristenitc', 'jokerman', 'juiceitc', 'kunstlerscript', 'widelatin', 'lucidabright', 'lucidacalligraphy', 'leelawadee', 'lucidafaxregular', 'lucidafax', 'lucidahandwriting', 'lucidasansregular', 'lucidasansroman', 'lucidasanstypewriterregular', 'lucidasanstypewriter', 'lucidasanstypewriteroblique', 'magneto', 'maiandragd', 'maturascriptcapitals', 'mistral', 'modernno20', 'microsoftuighur', 'monotypecorsiva', 'extra', 'niagaraengraved', 'niagarasolid', 'ocraextended', 'oldenglishtext', 'onyx', 'msoutlook', 'palacescript', 'papyrus', 'parchment', 'perpetua', 'perpetuatitling', 'playbill', 'poorrichard', 'pristina', 'rage', 'ravie', 'msreferencesansserif', 'msreferencespecialty', 'rockwellcondensed', 'rockwell', 'rockwellextra', 'script', 'showcardgothic', 'snapitc', 'stencil', 'twcen', 'twcencondensed', 'twcencondensedextra', 'tempussansitc', 'vinerhanditc', 'vivaldi', 'vladimirscript', 'wingdings2', 'wingdings3']
CELL_TEXT_SIZE = 10
CELL_TEXT_COLOR = BLACK
CELL_TEXT_BACKGROUND = (0, 255, 0)
CELL_TEXT_AA = False  # Anti-aliasing

# Flag the starting position (0, 0)
DRAW_POS_0 = True
DRAW_POS_0_TEXT = False
DRAW_POS_0_BORDER = True
CELL_BORDER_COLOR = (255, 255, 0)


class GUI:
    def __init__(self, rows: int, cols: int, start_x: int, start_y: int, block_size: int):
        super().__init__()

        # Modifiable outside class
        self.start_x = start_x
        self.start_y = start_y

        self._rows = rows
        self._cols = cols
        self._block_size = block_size

        self._grid_color = GRID_COLOR
        self._border_width = GRID_GIRTH
        self._cell_color = CELL_COLOR

        self._window_width = self._block_size * cols + GRID_GIRTH
        self._window_height = self._block_size * rows + GRID_GIRTH
        window_title = "Game of Life - by Shlomi Domnenko"

        self._screen = pygame.display.set_mode((self._window_width, self._window_height))
        pygame.display.set_caption(window_title)

        # For text
        pygame.font.init()
        self._txt_font = pygame.font.SysFont(CELL_TEXT_FONT, CELL_TEXT_SIZE)

    def __draw_lines(self):
        # Draw horizontal lines
        for y in range(0, self._window_height, self._block_size):
            pygame.draw.line(self._screen, self._grid_color, (0, y), (self._window_width, y), self._border_width)

        # Draw vertical lines
        for x in range(0, self._window_width, self._block_size):
            pygame.draw.line(self._screen, self._grid_color, (x, 0), (x, self._window_width), self._border_width)

    def __calc_left_top(self, x, y) -> (int, int):
        left = x * self._block_size
        top = y * self._block_size

        left = left - (self._block_size * self.start_x)
        top = top - (self._block_size * self.start_y)

        return left, top


    def __draw_cell(self, x: int, y: int):
        width = self._block_size
        height = self._block_size

        left, top = self.__calc_left_top(x, y)

        rect = pygame.Rect(left, top, width, height)
        pygame.draw.rect(self._screen, self._cell_color, rect)

        if DRAW_CELL_TEXT:
            text = f"({x},{y})"
            text_surface = self._txt_font.render(text, CELL_TEXT_AA, CELL_TEXT_COLOR, CELL_TEXT_BACKGROUND)
            self._screen.blit(text_surface, (left, top))

    def __draw_pos(self, x: int, y: int):
        left, top = self.__calc_left_top(x, y)

        if DRAW_POS_0_TEXT:
            text = f"({x},{y})"
            text_surface = self._txt_font.render(text, True, CELL_TEXT_COLOR, CELL_TEXT_BACKGROUND)
            self._screen.blit(text_surface, (left, top))

        elif DRAW_POS_0_BORDER:
            pygame.draw.rect(self._screen, CELL_BORDER_COLOR, (left, top, self._block_size, self._block_size), GRID_GIRTH, 1)

    def __draw_cells(self, cells: Cells):
        for x, y in cells:
            self.__draw_cell(x, y)

    def draw(self, cells: Cells):
        self._screen.fill(BLACK)

        if DRAW_GRID:
            self.__draw_lines()

        if DRAW_POS_0:
            self.__draw_pos(0, 0)

        self.__draw_cells(cells)
        pygame.display.flip()
