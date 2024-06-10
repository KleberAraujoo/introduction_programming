driver = input()
dist = float(input())
time = float(input())

v_m = dist / time

if v_m > 227:
  
  print(f"{driver} se deu muito bem na prova de hoje!!")
  
elif v_m == 227:
  
  print(f"{driver} teve um ótimo resultado. Mas, acredito que temos potencial para melhorar um pouco mais!")
  
else:
  
  print(f"{driver} não se deu tão bem. É preciso melhorar isso!")
  
  