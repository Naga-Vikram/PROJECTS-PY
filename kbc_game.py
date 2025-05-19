n=[
    [""""who is your fav1""","vikram","rajesh","karun","cutiee",1],
  [""""who is your fav2""","vikram","rajesh","karun","cutiee",2],
  [""""who is your fav3""","vikram","rajesh","karun","cutiee",3],
  [""""who is your fav4""","vikram","rajesh","karun","cutiee",4]
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
                