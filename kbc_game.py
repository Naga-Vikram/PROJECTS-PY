""""Kaun Banega Crorepati" (KBC), where players are presented with a question 
      and must choose the correct answer from the given options."""


n = [
    ["What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai", 2],
    ["Which planet is known as the 'Red Planet'?", "Mars", "Jupiter", "Venus", "Saturn", 1],
    ["What is the chemical symbol for water?", "Wa", "H2O", "Ox", "Hy", 2],
    ["Who wrote the play 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain", 2],
    ["What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],
    ["What is the currency of Japan?", "Yuan", "Won", "Yen", "Ringgit", 3],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet", 2]
]
levels=[1000,2000,3000,4000]
for i in range(0,len(n)):
    print(f"\n\nlevel {i+1} of {levels[i]} rupees question")
    print(n[i][0])
    # print("who is your fav")
    print(f"""1.{n[i][1]}     2.{n[i][2]}
3.{n[i][3]}     4.{n[i][3]}""")
    r=int(input("enter the option between 1-4 :"))
    if r==n[i][-1]:
        print("right answer")
    else:
        print("wrong answer")
        print(f"you have won {levels[i-1]} rupees")  
        break
                
