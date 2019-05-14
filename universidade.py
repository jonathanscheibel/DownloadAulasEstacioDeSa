####################################################################
## Script:          Download aulas universidade                   ##
## Requisitos:      Linux                                         ##
##                  Python2.7                                     ##    
##                  youtube-dl                                    ##
## Desenvolvedor:   Jonathan Scheibel - jsmorais@protonmail.com   ##
##                  https://jonathanscheibel.guithub.io           ##
####################################################################

import commands
import os

#codigoAtual -> Ponto de partida para checagem dos videos,
#               Quanto manor, mais probabilidade de encontrar, porem
#               quanto maior mais rapido sera o termino. Amostragem: 314392554
codigoAtual = 314392554 

#codigoFinal -> Ponto limite para checagem dos videos
#               Quanto maior, mais probabilidade de encontar, porem
#               quanto menor mais rapido sera o termino. Amostragem: 314392700 
codigoFinal = 314392700

LNK_V_VIMEO = "https://player.vimeo.com/video/"
PGR_V_DWNLD = "youtube-dl"
CMD_ESTACIO = PGR_V_DWNLD + " --no-warnings -e " + LNK_V_VIMEO

while (codigoAtual < codigoFinal):     
    codigoAtual = codigoAtual + 1
    tituloVideo = commands.getoutput(PGR_V_DWNLD + " --no-warnings -e " + LNK_V_VIMEO + str(codigoAtual))
    
    print ("Autenticidade [" + str(codigoAtual) + "] :")
    if not ('ERROR:' in tituloVideo):
        if ("v4-video-" in tituloVideo) or ("v5-video-" in tituloVideo): 
            print(" - Download: [" + str(codigoAtual) + "] - " + tituloVideo + " ...")
            os.system(PGR_V_DWNLD + " " + LNK_V_VIMEO + str(codigoAtual))

print("")
print("Contato: Jonathan Scheibel - jsmorais@protonmail.com")
