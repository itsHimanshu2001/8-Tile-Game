f event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        blankX,blankY=move("U",blankX,blankY)
                    if event.key == pygame.K_LEFT:
                        blankX,blankY= move("L",blankX,blankY)
                    if event.key == pygame.K_RIGHT:
                        blankX,blankY=move("R",blankX,blankY)
                    if event.key == pygame.K_DOWN:
                        blankX,blankY=move("D",blankX,blankY)