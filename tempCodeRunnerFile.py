for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit() 
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()