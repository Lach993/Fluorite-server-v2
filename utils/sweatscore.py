# Used to calculate the sweat score of a player
from math import e
logistic_values = [
    [1, 0.4, 50],
    [1, 0.2, 100],
    [1.5, 0.04, 450]
]

def logistic_growth(limit, scale, mover, x):
    return limit/(1+e**(-scale*(x-mover)))

def final_rating(final_kills, final_deaths):
    x = final_kills/(final_kills+final_deaths)
    return (e**x-1)**1.5 + 0.247620345
    
def win_loss_rating(wins,losses):
    x = wins/(wins+losses)
    # taylor series for \frac{24}{5\left(e-1\right)^{2}}\left(e^{x}-1\right)^{2}+.2
    return 0.2+1.6255*x**2 + 1.625*x**3 + 0.94833*x**4+0.406*x**5+.14*x**6

def star_rating(star):
    return sum([logistic_growth(limit, scale, mover, star) for limit, scale, mover in logistic_values]) + 0.5
    
def sweat_score(star, wins, losses, kills, deaths):
    return round(star_rating(star) * win_loss_rating(wins, losses) * final_rating(kills, deaths), 2)