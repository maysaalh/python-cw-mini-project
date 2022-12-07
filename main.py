# write your code here
def padel_court_cost(court_type):
    if court_type == ('indoor'):
        return 30
    elif court_type ==('outdoor'):
        return 20
def rackets_cost(racket_brand):
    if racket_brand== ('Bullpadel'):
        return 100
    elif racket_brand ==('Nox'):
        return 140
    elif racket_brand == ('Siux'):
        return 200
def padel_balls_cost(ball_boxes):
    if ball_boxes== "1":
        return 2
    elif ball_boxes== "2":
        return 3.5
    elif ball_boxes== "3":
        return 5
def padel_game_cost():
    courttype = input("indoor or outdoor?")
    ballboxes =input ("how many boxes (1-3)?")
    racketbrand = input ("which racket? Bullpadel or Nox or Siux")
    padel_court_cost(courttype)
    rackets_cost(racketbrand)
    padel_balls_cost(ballboxes)
    print(padel_court_cost(courttype) + rackets_cost(racketbrand) + padel_balls_cost(ballboxes))
padel_game_cost()
