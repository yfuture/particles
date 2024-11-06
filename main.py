import time, particles, random
import pygame as py

py.init()
telax, telay = 200, 200
info = py.display.Info()
largura = info.current_w
altura = info.current_h
tela = py.display.set_mode((largura,altura-40), py.RESIZABLE)
clock = py.time.Clock()
font = py.font.SysFont("Arial",20)
part = [particles.Particle(largura//2, altura//2, 0.1, 0.1, altura)]

while True:
    
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        print(event.type)

    for particle in part:
        particle.update()
        particle.randomizer()
        py.draw.circle(tela,(255,255,255),[int(particle.position[0]),int(particle.position[1])],6)

        if particle.position[1] >= int(particle.life):
            part.remove(particle)

    part.append(particles.Particle(largura//2, altura//2, 0.1, 0.1, altura))
    
    py.draw.rect(tela,(200,200,200),py.Rect(0,30,largura,90))

    num = len(part)
    text_part = font.render(f"Particles N: {num}", True, (0,0,0))
    tela.blit(text_part,(10,50))
    
    text_info = font.render(f"Info system screen: {largura}px, {altura}px, {clock}", True, (0,0,0))
    tela.blit(text_info,(10,70))
    
    py.display.update()
    clock.tick(60)
    tela.fill((100,100,100))
    