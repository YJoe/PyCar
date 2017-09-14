from Car import*

vehicle = Car()


def display_all(main_surface, display_list, text_list):
    main_surface.fill((0, 100, 100))
    for element in display_list:
        element.display(main_surface)
    for element_val in range(0, len(text_list)):
        main_surface.blit(font.render(str(text_list[element_val]), True, (0, 255, 0)), (10, 10 + (10 * element_val)))


def update_all(update_list):
    for element in update_list:
        element.update()


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            None

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        print "LEFT"
        vehicle.left = True
    if key[pygame.K_RIGHT]:
        vehicle.right = True
    if key[pygame.K_UP]:
        vehicle.forward = True
    if key[pygame.K_DOWN]:
        vehicle.backward = True
    if key[pygame.K_r]:
        vehicle.rect.x = 500
        vehicle.rect.y = 300
        vehicle.angle = 0

    to_update = [vehicle]
    to_display = [vehicle]
    to_text = [clock.get_fps(),
               vehicle.angle,
               vehicle.current_speed,
               vehicle.move_x,
               vehicle.move_y,
               "F " + str(vehicle.forward),
               "L " + str(vehicle.left),
               "R " + str(vehicle.right)]

    update_all(to_update)
    display_all(main_s, to_display, to_text)
    pygame.display.flip()

