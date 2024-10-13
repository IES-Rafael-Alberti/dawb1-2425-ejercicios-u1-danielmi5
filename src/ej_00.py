import subprocess # subprocess.run(): Para ejecutar un archivo como si fuera un script separado.

def pedir_num():
    num = input("")
    while num.isdigit() == False:
      num = input("ERROR: Debe introducir un número (1-30): ")
      while num.isdigit() == True:
        if int(num) >= 1 and int(num) <=30:
          return int(num) 
        else:
          num = input("ERROR: Solo existen programas del 1 al 30: ")
          if num.isdigit() == True and int(num) >= 1 and int(num) <=30:
            return int(num) 
          
def ejecucion():
  subprocess.run(["python", "archivo1.py"])
  
  
    
  



def main():
  print ("Introduzca el número del programa: " , end="")
  num_programa = pedir_num()
  
  
  
  
if __name__ == "__main__":
  main()