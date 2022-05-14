# 190202084, Serhat Sayan - 170201049, Halim Ahat Akturan

import numpy as np
import scipy as sp
import matplotlib as mpl
from scipy.io import wavfile
import matplotlib.pyplot as plt
# from scipy import signal

#bpm(beats per minute) değerine göre ikilik, dörtlük, sekizlik notaların sürelerini hesaplar
bpm = 180
sure4 = 60/bpm
sure8 = sure4/2
sure2 = sure4*2
sure1 = sure4*4

#notaları frenkanslarıyla eşleştirerek bir dictionary oluşturur
def notaların_frekansları():

    oktav = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
    ana_frekans = 440
    notalar = np.array([x+str(y) for y in range(0,9) for x in oktav])
    bas = np.where(notalar == 'A0')[0][0]
    son = np.where(notalar == 'C8')[0][0]
    notalar = notalar[bas:son+1]

    nota_frekans = dict(zip(notalar, [2**((n+1-49)/12)*ana_frekans for n in range(len(notalar))]))
    nota_frekans[''] = 0.0 
    return nota_frekans

#gelen frekans ve süreye göre bir sinüs dalgası oluşturur
def notadan_sinus_dalgası_olustur(frekans, sure, genlik, sample_rate=44100):

    #sample_rate = 44100
    #genlik = 4096
    t = np.linspace(0, sure, int(sample_rate*sure))
    dalga = genlik*np.sin(2*frekans*t*np.pi)
    return dalga

#verilen süreye göre sus(es) döndürür
def sus_olustur(sure):
    sample_rate=44100
    genlik=2048
    frekans=0
    t = np.linspace(0, sure, int(sample_rate*sure))
    dalga = genlik*np.sin(2*frekans*t*np.pi)
    return dalga

#sinüs dalga fonksiyonunu kullanarak verilen frekans ve süre değerlerine göre bir kare dalga döndürür
def square_wave_olustur(frekans, sure):
    dalga = notadan_sinus_dalgası_olustur(frekans, sure, genlik=2048)
    for x in range(3, 20, 2):
        y=0
        if(y%2==0):
            dalga = dalga + notadan_sinus_dalgası_olustur(frekans*x, sure, genlik=2048/x)
        else:
            dalga = dalga - notadan_sinus_dalgası_olustur(frekans*x, sure, genlik=2048/x)
        y=y+1
    return dalga

#verilen frekanslara göre 2 nota süresinde 3 nota içeren bir dalga döndürür
def uclu_nota_olustur(frekans1, frekans2, frekans3):
    finaldalga = []

    dalga = square_wave_olustur(frekans1, sure2/3)
    finaldalga = np.append(finaldalga, dalga)

    if(frekans1 == frekans2):
        dalga = sus_olustur(0.005)
        finaldalga = np.append(finaldalga, dalga)

    dalga = square_wave_olustur(frekans2, sure2/3)
    finaldalga = np.append(finaldalga, dalga)

    if(frekans2 == frekans3):
        dalga = sus_olustur(0.005)
        finaldalga = np.append(finaldalga, dalga)

    dalga = square_wave_olustur(frekans3, sure2/3)
    finaldalga = np.append(finaldalga, dalga)

    return finaldalga

nota_freqs = notaların_frekansları()


#---------------------------------------------Parçanın-Yazıldığı-Blok----------------------------------------------

#1-1
frekans = nota_freqs['E5']
parca = []
dalga = sus_olustur(0.5)
parca = np.append(parca, dalga)
#dalga = notadan_sinus_dalgası_olustur(frekans, sure=0.167, genlik=2048)

dalga = square_wave_olustur(frekans, sure=0.167)
parca = np.append(parca, dalga)

#notaların birbirinden ayrışması için araya çok küçük bir es koydum
dalga = sus_olustur(0.005)
parca = np.append(parca, dalga)

#dalga = notadan_sinus_dalgası_olustur(frekans, sure=0.167, genlik=2048)
dalga = square_wave_olustur(frekans, sure=0.167)
parca = np.append(parca, dalga)

dalga = sus_olustur(0.167)
parca = np.append(parca, dalga)

#dalga = notadan_sinus_dalgası_olustur(frekans, sure=0.167, genlik=2048)
dalga = square_wave_olustur(frekans, sure=0.167)
parca = np.append(parca, dalga)

dalga = sus_olustur(0.167)
parca = np.append(parca, dalga)

frekans = nota_freqs['C5']
dalga = square_wave_olustur(frekans, sure=0.167)
parca = np.append(parca, dalga)

frekans = nota_freqs['E5']
dalga = square_wave_olustur(frekans, sure=sure4)
parca = np.append(parca, dalga)

#1-2
frekans = nota_freqs['G5']
dalga = square_wave_olustur(frekans, sure=sure4)
parca = np.append(parca, dalga)

dalga = sus_olustur(sure4)
parca = np.append(parca, dalga)

frekans = nota_freqs['G4']
dalga = square_wave_olustur(frekans, sure=sure4)
parca = np.append(parca, dalga)

dalga = sus_olustur(sure4)
parca = np.append(parca, dalga)


yuvarlak_parca = []

for x in range(2):
    #1-3
    frekans = nota_freqs['C5']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    dalga = sus_olustur(sure8)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    frekans = nota_freqs['G4']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    dalga = sus_olustur(sure8)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    frekans = nota_freqs['E4']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    #1-4
    dalga = sus_olustur(sure8)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    frekans = nota_freqs['A4']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    frekans = nota_freqs['B4']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    frekans = nota_freqs['a4']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    frekans = nota_freqs['A4']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    #1-5
    #------------------------üçlü-nota----------------------------------------
    dalga = uclu_nota_olustur(nota_freqs['G4'], nota_freqs['E5'], nota_freqs['G5'])
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)
    #-------------------------------------------------------------------------

    frekans = nota_freqs['A5']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    frekans = nota_freqs['F5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    frekans = nota_freqs['G5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    #1-6
    dalga = sus_olustur(sure8)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    frekans = nota_freqs['E5']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    frekans = nota_freqs['C5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    frekans = nota_freqs['D5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    frekans = nota_freqs['B4']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)

    dalga = sus_olustur(sure8)
    parca = np.append(parca, dalga)
    yuvarlak_parca = np.append(yuvarlak_parca, dalga)


for x in range(2):
    #2-1
    yıldız_parca = []

    dalga = sus_olustur(sure4)
    parca = np.append(parca, dalga)
    yıldız_parca = np.append(yıldız_parca, dalga)

    frekans = nota_freqs['G5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    yıldız_parca = np.append(yıldız_parca, dalga)

    frekans = nota_freqs['f5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    yıldız_parca = np.append(yıldız_parca, dalga)

    frekans = nota_freqs['F5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    yıldız_parca = np.append(yıldız_parca, dalga)

    frekans = nota_freqs['d5']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    yıldız_parca = np.append(yıldız_parca, dalga)

    frekans = nota_freqs['E5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    yıldız_parca = np.append(yıldız_parca, dalga)

    #2-2
    ucgen_parca = []

    dalga = sus_olustur(sure8)
    parca = np.append(parca, dalga)
    ucgen_parca = np.append(ucgen_parca, dalga)

    frekans = nota_freqs['g4']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    ucgen_parca = np.append(ucgen_parca, dalga)

    frekans = nota_freqs['A4']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    ucgen_parca = np.append(ucgen_parca, dalga)

    frekans = nota_freqs['C5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    ucgen_parca = np.append(ucgen_parca, dalga)

    dalga = sus_olustur(sure8)
    parca = np.append(parca, dalga)
    ucgen_parca = np.append(ucgen_parca, dalga)

    frekans = nota_freqs['A4']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    ucgen_parca = np.append(ucgen_parca, dalga)

    frekans = nota_freqs['C5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    ucgen_parca = np.append(ucgen_parca, dalga)

    frekans = nota_freqs['D5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    ucgen_parca = np.append(ucgen_parca, dalga)

    #2-3
    parca = np.append(parca, yıldız_parca)

    #2-4
    dalga = sus_olustur(sure8)
    parca = np.append(parca, dalga)

    frekans = nota_freqs['C6']
    dalga1 = square_wave_olustur(frekans, sure=sure4)
    frekans = nota_freqs['G5']
    dalga2 = square_wave_olustur(frekans, sure=sure4)
    dalga = dalga1 + dalga2
    parca = np.append(parca, dalga)

    #notaların birbirinden ayrışması için araya çok küçük bir es koydum
    dalga = sus_olustur(0.005)
    parca = np.append(parca, dalga)

    frekans = nota_freqs['C6']
    dalga1 = square_wave_olustur(frekans, sure=sure8)
    frekans = nota_freqs['G5']
    dalga2 = square_wave_olustur(frekans, sure=sure8)
    dalga = dalga1 + dalga2
    parca = np.append(parca, dalga)

    #notaların birbirinden ayrışması için araya çok küçük bir es koydum
    dalga = sus_olustur(0.005)
    parca = np.append(parca, dalga)

    frekans = nota_freqs['C6']
    dalga1 = square_wave_olustur(frekans, sure=sure4)
    frekans = nota_freqs['G5']
    dalga2 = square_wave_olustur(frekans, sure=sure4)
    dalga = dalga1 + dalga2
    parca = np.append(parca, dalga)

    dalga = sus_olustur(sure4)
    parca = np.append(parca, dalga)

    #2-5
    parca = np.append(parca, yıldız_parca)

    #3-1
    parca = np.append(parca, ucgen_parca)

    #3-2
    dalga = sus_olustur(sure4)
    parca = np.append(parca, dalga)

    frekans = nota_freqs['d5']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)

    dalga = sus_olustur(sure8)
    parca = np.append(parca, dalga)

    frekans = nota_freqs['D5']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)

    dalga = sus_olustur(sure8)
    parca = np.append(parca, dalga)

    #3-3
    frekans = nota_freqs['C5']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)

    dalga = sus_olustur(sure4)
    parca = np.append(parca, dalga)

    dalga = sus_olustur(sure2)
    parca = np.append(parca, dalga)

#3-4
kare_parca = []

frekans = nota_freqs['C5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)
kare_parca = np.append(kare_parca, dalga)

dalga = sus_olustur(0.005)
parca = np.append(parca, dalga)
kare_parca = np.append(kare_parca, dalga)

frekans = nota_freqs['C5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)
kare_parca = np.append(kare_parca, dalga)

dalga = sus_olustur(sure8)
parca = np.append(parca, dalga)
kare_parca = np.append(kare_parca, dalga)

frekans = nota_freqs['C5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)
kare_parca = np.append(kare_parca, dalga)

dalga = sus_olustur(sure8)
parca = np.append(parca, dalga)
kare_parca = np.append(kare_parca, dalga)

frekans = nota_freqs['C5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)
kare_parca = np.append(kare_parca, dalga)

frekans = nota_freqs['D5']
dalga = square_wave_olustur(frekans, sure=sure4)
parca = np.append(parca, dalga)
kare_parca = np.append(kare_parca, dalga)

#3-5
frekans = nota_freqs['E5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)
kare_parca = np.append(kare_parca, dalga)

frekans = nota_freqs['C5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)
kare_parca = np.append(kare_parca, dalga)

dalga = sus_olustur(sure8)
parca = np.append(parca, dalga)
kare_parca = np.append(kare_parca, dalga)

frekans = nota_freqs['A4']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)
kare_parca = np.append(kare_parca, dalga)

frekans = nota_freqs['G4']
dalga = square_wave_olustur(frekans, sure=sure2)
parca = np.append(parca, dalga)
kare_parca = np.append(kare_parca, dalga)

#4-1
frekans = nota_freqs['C5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)

dalga = sus_olustur(0.005)
parca = np.append(parca, dalga)

frekans = nota_freqs['C5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)

dalga = sus_olustur(sure8)
parca = np.append(parca, dalga)

frekans = nota_freqs['C5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)

dalga = sus_olustur(sure8)
parca = np.append(parca, dalga)

frekans = nota_freqs['C5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)

frekans = nota_freqs['D5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)

frekans = nota_freqs['E5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)

#4-2
dalga = sus_olustur(sure1)
parca = np.append(parca, dalga)

#4-3, 4-4
parca = np.append(parca, kare_parca)

#4-5
frekans = nota_freqs['E5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)

dalga = sus_olustur(0.005)
parca = np.append(parca, dalga)

frekans = nota_freqs['E5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)

dalga = sus_olustur(sure8)
parca = np.append(parca, dalga)

frekans = nota_freqs['E5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)

dalga = sus_olustur(sure8)
parca = np.append(parca, dalga)

frekans = nota_freqs['C5']
dalga = square_wave_olustur(frekans, sure=sure8)
parca = np.append(parca, dalga)

frekans = nota_freqs['E5']
dalga = square_wave_olustur(frekans, sure=sure4)
parca = np.append(parca, dalga)

#4-6
frekans = nota_freqs['G5']
dalga = square_wave_olustur(frekans, sure=sure4)
parca = np.append(parca, dalga)

dalga = sus_olustur(sure4)
parca = np.append(parca, dalga)

frekans = nota_freqs['G4']
dalga = square_wave_olustur(frekans, sure=sure4)
parca = np.append(parca, dalga)

dalga = sus_olustur(sure4)
parca = np.append(parca, dalga)

#5-1, 5-2, 5-4, 5-4
parca = np.append(parca, yuvarlak_parca)

for x in range(2):
    ay_parca = []
    #5-5
    frekans = nota_freqs['E5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    ay_parca = np.append(ay_parca, dalga)

    frekans = nota_freqs['C5']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    ay_parca = np.append(ay_parca, dalga)

    frekans = nota_freqs['G4']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    ay_parca = np.append(ay_parca, dalga)

    dalga = sus_olustur(sure4)
    parca = np.append(parca, dalga)
    ay_parca = np.append(ay_parca, dalga)

    frekans = nota_freqs['g4']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    ay_parca = np.append(ay_parca, dalga)

    #5-6
    frekans = nota_freqs['A4']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    ay_parca = np.append(ay_parca, dalga)

    frekans = nota_freqs['F5']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    ay_parca = np.append(ay_parca, dalga)

    dalga = sus_olustur(0.005)
    parca = np.append(parca, dalga)
    ay_parca = np.append(ay_parca, dalga)

    frekans = nota_freqs['F5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)
    ay_parca = np.append(ay_parca, dalga)

    frekans = nota_freqs['A4']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)
    ay_parca = np.append(ay_parca, dalga)

    dalga = sus_olustur(sure4)
    parca = np.append(parca, dalga)
    ay_parca = np.append(ay_parca, dalga)

    #6-1
    dalga = uclu_nota_olustur(nota_freqs['B4'], nota_freqs['A5'], nota_freqs['A5'])
    parca = np.append(parca, dalga)

    dalga = sus_olustur(0.005)
    parca = np.append(parca, dalga)

    dalga = uclu_nota_olustur(nota_freqs['A5'], nota_freqs['G5'], nota_freqs['F5'])
    parca = np.append(parca, dalga)

    #6-2
    frekans = nota_freqs['E5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)

    frekans = nota_freqs['C5']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)

    frekans = nota_freqs['A4']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)

    frekans = nota_freqs['G4']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)

    dalga = sus_olustur(sure4)
    parca = np.append(parca, dalga)

    #6-3, 6-4
    parca = np.append(parca, ay_parca)

    #6-5
    frekans = nota_freqs['B4']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)

    frekans = nota_freqs['F5']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)

    dalga = sus_olustur(0.005)
    parca = np.append(parca, dalga)

    frekans = nota_freqs['F5']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)

    dalga = sus_olustur(0.005)
    parca = np.append(parca, dalga)

    dalga = uclu_nota_olustur(nota_freqs['F5'], nota_freqs['E5'], nota_freqs['D5'])
    parca = np.append(parca, dalga)

    #6-6
    frekans = nota_freqs['G4']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)

    frekans = nota_freqs['E4']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)

    dalga = sus_olustur(0.005)
    parca = np.append(parca, dalga)

    frekans = nota_freqs['E4']
    dalga = square_wave_olustur(frekans, sure=sure8)
    parca = np.append(parca, dalga)

    frekans = nota_freqs['C4']
    dalga = square_wave_olustur(frekans, sure=sure4)
    parca = np.append(parca, dalga)

    dalga = sus_olustur(sure4)
    parca = np.append(parca, dalga)

#---------------------------------------------Parça-Bloğunun-Sonu------------------------------------- 

#parçayı uygun tipe dönüştürür, ardından dönüştürülmüş parçayı bir wav dosyası olarak kaydeder
data = parca.astype(np.int16)
wavfile.write("super-mario-bros-theme.wav", 44100, data)
