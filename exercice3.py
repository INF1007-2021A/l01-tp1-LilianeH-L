
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees= int(secondes/(3600*24*365))
    secondes -= annees*3600*24*365

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines= int(secondes/(3600*24*7))
    secondes -= semaines*3600*24*7

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours= int(secondes/(3600*24))
    secondes -= jours*3600*24

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures= int(secondes/3600)
    secondes -= heures*3600

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = int(secondes/60)
    secondes -= minutes*60

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = int(secondes)

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(f"{annees} années,{semaines} semaines,{jours} jours, {heures} heures, {minutes} minutes, {secondes} secondes")

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
