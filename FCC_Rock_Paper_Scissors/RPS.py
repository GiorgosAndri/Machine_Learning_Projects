# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
i = 0
import random
history = []
sequences = {}
def player(prev_play, opponent_history=[]):
    global i, sequences
    guess = random.choice(["P", "S", "R"])
    opponent_history.append(prev_play) 
    if len(opponent_history) == 0:
      i += 1
      return "P"
    if i <= 1000 :
      if prev_play == "R":
          i += 1
          return "P"
      elif prev_play == "P":
           i += 1
           return "S"
      elif prev_play == "S":
        i += 1
        return "R"


        
    if i == 1000:
      opponent_history.clear()
      guess = "R"
      history.clear()
      history.append(guess)
      i += 1
      return guess

      
    

    if i > 1000 and i <= 2000:
          limit = 3

          if len(opponent_history) <= limit:
            i += 1
            return "R"
        
          
          if len(opponent_history) > limit + 1:
            opponent_history.pop(0)
        
         
          seq = "".join(opponent_history)
          sequences[seq] = sequences.get(seq, 0) + 1
        
          
          seq     = "".join(opponent_history[-limit:])
          prediction = max([seq+"R", seq+"P", seq+"S"],
                          key=lambda key: sequences.get(key,0))[-1]
        
          if prediction == "R":
            i += 1
            return "P"
          if prediction == "P":
            i += 1
            return "S"
          i += 1
          return "R"
      
    if i > 2000 and i <= 3000:
      if len(opponent_history) == 0:
          i += 1
          return random.choice(['R', 'P', 'S'])
          
    
      if len(opponent_history) >= 2:
          last_two = "".join(opponent_history[-2:])
          if last_two == 'RR':
            prediction = 'P'  
          elif last_two == 'PP':
            prediction = 'S'  
          elif last_two == 'SS':
            prediction = 'R'  
          elif last_two == 'RP':
            prediction = 'S'  
          elif last_two == 'RS':
            prediction = 'P'  
          elif last_two == 'PR':
            prediction = 'R'  
          elif last_two == 'PS':
            prediction = 'R'  
          elif last_two == 'SR':
            prediction = 'S'
          else:
            prediction = 'P'
      else:
          prediction = prev_play
        
        
      if prediction == 'R':
          i += 1
          return 'P' 
      elif prediction == 'P':
          i += 1
          return 'S'
      else:
          i += 1
          return 'R' 

    
    
    if i == 3000:
      opponent_history.clear()
      guess = "R"
      history.clear()
      history.append(guess)
      i += 1
      return guess
    result = "tie"
    if i > 3000:
      if history[-1] == opponent_history[-1]:
          result == "tie"
      elif (history[-1] == "P" and opponent_history[-1] == "R") or  (history[-1] == "R" and opponent_history[-1] == "S") or (history[-1] == "S" and opponent_history[-1] == "P"):
        result = "win"
      elif opponent_history[-1] == "P" and history[-1] == "R" or opponent_history[-1] == "R" and history[-1] == "S" or opponent_history[-1] == "S" and history[-1] == "P":
              result = "loss"
    if i > 3000:
      if result == "tie":
        guess = random.choice(["R", "P", "S"])
        history.append(guess)
        i += 1
        return guess
      if result == "loss":
        if prev_play == "R":
          history.append("P")
          return "P"
        elif prev_play == "S":
          history.append("R")
          return "R"
        else:
          history.append("S")
          return "S"
      elif result == "win":
        if history[-2] == "R":
          history.append("P")
          return "P"
        elif history[-2] == "S":
          history.append("R")
          return "R"
        else:
          history.append("S")
          return "S"
    
        
    i += 1
    return guess

