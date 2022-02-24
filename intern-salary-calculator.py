import PySimpleGUI as sg
# This is a sample Python script to calculate the net salary's intern in France base on it brut salary (Developed by Wilfried SINKAM).
# source of calcul : https://www.jobteaser.com/fr/advices/112-gratification-de-stage-les-5-questions-que-vous-vous-posez-tous
cste = 601


def calculSalaireNet(brut, percent):
    net = brut - ((brut - cste)*percent/100)
    return net


brut = ''
while not(brut.isnumeric()):
    brut = sg.popup_get_text(f'Entrer votre salaire brut correct (superieur à {cste})', 'Calcul Salaire Net')
    if brut.isnumeric():
        while int(brut) <= cste:
            brut = sg.popup_get_text(
                f'Vous avez entré {brut}€. Or, votre salaire doit etre strictement superieur à {cste}€. Merci de resaisir votre salaire...',
                'Calcul Salaire Net')
brut = float(brut)

percent = sg.popup_get_text('Entrer le pourcentage de calcul (entre 10 et 15)', 'Calcul Salaire Net', '10')
if percent.isnumeric():
    if int(percent) >= 10 & int(percent) <= 15:
        percent = int(percent)
    else:
        percent = 10  # valeur par defaut = 10 si ce n'est pas compris entre 10 et 15
else:
    percent = 10  # valeur par defaut = 10 si ce n'est pas un nombre

net = calculSalaireNet(brut, percent)
sg.popup('Resultat - Calcul Salaire Net', f'Votre salaire brut est {brut}€ et le pourcentage appliqué au calcul du salaire net de votre entreprise est de {percent}%\n\nVotre salaire net est donc de {net}')
