import sys

pq=0

print("***bienvenido a -Deadly Decisions-***\nEn este juego ambientado en un bloque de apartamentos, donde algo salió mal\nTu objetivo es formar un equipo de ¿personasas? confiables para poder enfrentar al moutro que se encurntra custodiando la salida")

print("\nantes de empezar a jugar debes de saber un par de cosa importante del juego")
print("\n1. Abra dos formas de tomar las decisiones, la primera es escribiendo el numero de la opcion que deseas tomar y la segunda es escribiendo la opcion completa\n2. tomar una decicion que no esta en las opciones que te da el juego lo rompe y contara perder el juego\n3. tienes solo una vida, morir significa empezar desde 0")

print("\npara emepezar esta aventura dime")
n=input("¿Cual es tu nombre?: ")

print(f"\nEres {n},vives en el pito 4 apartamento 3, mientras te preparas para ir a trabajar ves que por la ventana se nota una luz verde muy rara\n")

d= input("¿Que haces? \n(1) ignorar la luz y seguir con tu dia\n(2) abrir las cortinas para ver de donde viene la luz\n(3) tirar al gato entre las cortinas\n:".lower())

if d=="1" or d=="ignorar la luz y seguir con tu dia":
    print("\nDecides ignorar la luz y seguir con tu dia")
    
    
elif d=="2" or d=="abrir las cortinas para ver de donde viene la luz":   
    print("\n¿Decides abrir las cortinas para ver de donde viene la luz\nLa luz hace que tu cuerpo mute de manera grotresca mientras pierdes lenteamente\n")
    print(f"\n{n} A muerto, GAME OVER")
    sys.exit()
    
elif d=="3" or d=="tirar al gato entre las cortinas":
    print("\nDecides tirar al gato entre las cortinas\nVes como tu gato se transoforma en un moustro y te ve con intenciones de ataca\n")
  
    d= input("\n¿Que haces? \n(1) salir corriendo fuera del apartamento\n(2) intentar calmar al mounstro con comida\n(3) intentar matar al mounstro\n:".lower())

    if d=="1" or d=="salir corriendo fuera del apartamento":
        print("\nDecides salir corriendo fuera del apartamento\nlogras salir y serrar la puerta\nves a uno de tus vecino en el pasillo")
        d= input("\n¿Que haces? \n(1)intentar pasar por el pasillo corriendo\n(2)volver a tu apartamento\n(3)pedir ayuda al vecino\n:".lower())
        
        if d=="1" or d=="intentar pasar por el pasillo corriendo":
            print("\nDecides intentar pasar por el pasillo\nEl vesino te persigue y te atrapa\nLo ultimo que ves es como al vesino se le parte el rostro en dos parte revelando una boca los suficientemente grande como para comerese tu cavesa de un solo bocado\n-100HP")
            print(f"\n{n} A muerto, GAME OVER")
            sys.exit()
            
        elif d=="2" or d=="volver a tu apartamento":
            print("\nDecides volver a tu apartamento\nen el momento que abres la puerta el gato mutante te ataca sin oportunidad de huir\n")
            print(f"\n{n} A muerto, GAME OVER")
            sys.exit()
            
        elif d=="3" or d=="pedir ayuda al vecino":
            print("\nDecides pedir ayuda al vecino\nEl vecino resulta ser un moutro que solo te ayuda a dejar este mundo\n")  
            print(f"\n{n} A muerto, GAME OVER")
            sys.exit()
              
    elif d=="2" or d=="intentar calmar al mounstro con comida":
        print("\nDecides intentar calmar al mounstro con comida\nEl mounstro se calma y se pone a comer\nA pesar de su tamaño aspecto mutado decides acarisiarlo\n*Felicidades gato mutante se a unido a tu quipo*")
        pq=pq+1
        
    elif d=="3" or d=="intentar matar al mounstro":
        print("\nDecides intentar matar al mounstro\nNo tienes ninguna oportunidad de ganar\n")
        print(f"\n{n} A muerto, GAME OVER")
        sys.exit()    

d= input("\n¿Que haces? \n(1)salir del apartamento\n(2)llamar a un vecino para preguntar por la luz verde\n:".lower())

if (d=="1" or d=="salir del apartamento") and pq==0:
    print("\nDecides salir del apartamento\nVes que el pasillo esta uno de tus vesinos pero parese que algo raro esta pasando \n")
    d= input("\n¿Que haces? \n(1) intentar pasar por el pasillo corriendo\n(2)pedir ayuda a un aliado\n:".lower())
    
    if d=="1" or d=="intentar pasar por el pasillo corriendo":
        print("\nDecides intentar pasar por el pasillo\nEl vesino te persigue y te atrapa\nLo ultimo que ves es como al vesino se le parte el rostro en dos parte revelando una boca los suficientemente grande como para comerese tu cavesa de un solo bocado\n-100HP")
        print(f"\n{n} A muerto, GAME OVER")
        sys.exit()
    
    elif d=="2" or d=="pedir ayuda a un aliado":
        print("\nno tienes ningul aliado\nel moutro te ataca\nno tiene oportunidad alguno contra el")
        print(f"\n{n} A muerto, GAME OVER")
        sys.exit()
        
elif (d=="1" or d=="salir del apartamento") and pq==1:
    print("\nDecides salir del apartamento\nVes que el pasillo esta uno de tus vesinos pero parese que algo raro esta pasando \n")
    d= input("\n¿Que haces? \n(1) intentar pasar por el pasillo corriendo\n(2)pedir ayuda a un aliado\n:".lower())   
    
    if d=="1" or d=="intentar pasar por el pasillo corriendo":
            print("\nDecides intentar pasar por el pasillo\nEl vesino te persigue y te atrapa\nLo ultimo que ves es como al vesino se le parte el rostro en dos parte revelando una boca los suficientemente grande como para comerese tu cavesa de un solo bocado\n-100HP")
            print(f"\n{n} A muerto, GAME OVER")
            sys.exit()
            
    elif d=="2" or d=="pedir ayuda a un aliado":
             print("\ntu gato mutante decapita al vecino de una mordida con facilidad\n*felicidades el pasillo del piso 4 quedo libre de amenazas*\nVes que la puerta del apartamento dos esta abierta")
    
            
elif d=="2" or d=="llamar a un vecino para preguntar por la luz verde":
        print("\nDecides llamar a un vecino para preguntar por la luz verde\npero tienes poca bareria en tu telefono y solo puedes llamar a un vecino\n")
        d= input("\n¿A cual vecino llamas? \n(1)Paco\n(2)Pedro\n(3)Pepe\n:".lower())

        if d=="1" or d=="paco":
            print("\nDecides llamar al vecino del 2do piso")
            print(f"\n{n}: Hola, ¿te encuenras bein?\nVecino: Hola, {n} ¿sabes que esta pasando con esa luz verde?\n{n}: al pareser tranforma a los animales en moustros\nVecino: que horible, y como lo descubriste?\n{n}: tire al gato por la ventana y se transformo en un moustro\nvecino:Er diablo, ahora hay un gato muntante rondando por el edificio\n{n}: si pero no te preocupes, le de su comida favoirta y se comporta como un gatito\nVecino: que bueno, que te parese si te espero aqui en el 2do piso departamento 2 para ir guntos a ver los que sea que esta haciendo esos ruidos en el primer piso\n{n}: de acuerdo, nos vemos hay \nVecino: de acuerdo, nos vemos\n")
            
        elif d=="2" or d=="pedro":
            print("\nDecides llamar al vecino del 3er piso")
            print(f"\n{n}: Hola, ¿te encuentras bien?\nvecino:...\n{n}: ¿hay alguien ahí?\nvecino_...")
            print("\n te quedas espernado una respuesta pero solo se escucha una respiracion hasta que telefono se descarga")
            
        elif d=="3" or d=="pepe":
            print("\nDecides llamar al vecino del 4to piso")
            print(f"\n{n}: Hola, ¿te encuentras bien?\nvecino:no, nesesito ayuda\n{n}: ¿que pasa?\nvecino:esto sonara raro pero mi planta combro vida y me esta buscando para atacarme\n{n}: que horible, en que apartamento estas?\nvecino: en el 4to piso apartamento 1\n{n}: de acuerdo, voy para aya\nvecino: gracias, nos vemos pronto\n")
       
        d= input("\nDecides salir del apartamento\nVes que el pasillo esta uno de tus vesinos pero parese que algo raro esta pasando\n\n¿Que haces?\n(1)intentar pasar por el pasillo corriendo\n(2)pedir ayuda a un aliado\n:".lower()) 
        
        if (d=="1" or d=="intentar pasar por el pasillo corriendo") and pq==0:
            print("\nDecides intentar pasar por el pasillo\nEl vesino te persigue y te atrapa\nLo ultimo que ves es como al vesino se le parte el rostro en dos parte revelando una boca los suficientemente grande como para comerese tu cavesa de un solo bocado")
            print(f"\n{n} A muerto, GAME OVER")
            sys.exit()
                
        elif (d=="2" or d=="pedir ayuda a un aliado") and pq==0:
             print("\nno tienes ningul aliado\nel moutro te ataca\nno tiene oportunidad alguno contra el")
             print(f"\n{n} A muerto, GAME OVER")
             sys.exit()
                    
        elif (d=="1" or d=="intentar pasar por el pasillo corriendo") and pq==1:
            print("\nDecides intentar pasar por el pasillo\nEl vesino te persigue y te atrapa\nLo ultimo que ves es como al vesino se le parte el rostro en dos parte revelando una boca los suficientemente grande como para comerese tu cavesa de un solo bocado")
            print(f"\n{n} A muerto, GAME OVER")
            sys.exit()
                     
        elif (d=="2" or d=="pedir ayuda a un aliado") and pq==1:
            print("\ntu gato mutante decapita al vecino de una mordida con facilidad\n*felicidades el pasillo del piso 4 quedo libre de amenazas*\nVes que la puerta del apartamento 2 esta abierta")   
       
d= input("\n¿Que haces?\n(1)bajar al piso 3\n(2)entrar al apartamento 2\n(3)forsar la puerta del apartamento 1\n:".lower())

if d=="1" or d=="bajar al piso 3":
    print("\nte encuentras a dos moutros\nes demasiado para tu gato mutante\nlos moutro despedasan a tu gato munte y el siguiente eres tu")
    print(f"\n{n} A muerto, GAME OVER")
    sys.exit()

elif d=="2" or d=="entrar al apartamento 2":
    print("\nentras al apartamento 2 y encuetras un machete\n*felicidades ya no eres inutil en las peleas*")
    pq=pq+1

elif d=="3" or d=="forsar la puerta del apartamento 1":
    print("\nlogras abrir la puerta\nlo primero que ves es una planta humanoide intentado derrumbar la puerta del baño")   
    d=input ("\nQue haces?\n(1)escapar al 3er piso\n(2)pelear contra el moutro\n:".lower())
     
    if d=="1" or d=="escapar al 3er piso":
        print("\nte encuentras a dos moutros\nes demasiado para tu gato mutante\nlos moutro despedasan a tu gato munte y el siguiente eres tu")
        print(f"\n{n} A muerto, GAME OVER")
        sys.exit()
        
    elif d=="2" or d=="pelear contra el moutro":
        print("\nel moutro planta inmoviliza a tu gato mutante\nes tu turno de pelear\neres un inutil que no pudo conseguir un arma\nel moutro te mata a ti y a tu gatito")    
        print(f"\n{n} A muerto, GAME OVER")
        sys.exit()

d = input ("\n¿Que haces?\n(1)bajar al 3er piso\n(2)entrar al apartamento 1\n:".lower())  

if d=="1" or d=="bajar al 3er piso":
    print("\nte encuatras a dos moutro\nte sientes confiado con tu machete y decides atacar\nlogreas derrotar a los moutros pero\nde la nada unas enredaderas ensagrentadas te inmovilizan\nlo ultimo que ves es el cadaver de pepe desmenbredo lleno de plantas nutriendose de su sangre\nsolo te que esperar lo inevitable")      
    print(f"\n{n} A muerto, GAME OVER")
    sys.exit()
    
elif d=="2" or d=="entrar al apartamento 1":
    print("\nlo primero que ves es una planta humanoide intentado derrumbar la puerta del baño")
    d=input ("\nQue haces?\n(1)escapar al 3er piso\n(2)pelear contra el moutro\n:".lower())
         
    if d=="1" or d=="escapar al 3er piso":
        print("\nte encuentras a dos moutros\nes demasiado para tu gato mutante\nlos moutro despedasan a tu gato munte y el siguiente eres tu")
        print(f"\n{n} A muerto, GAME OVER")
        sys.exit()
            
    elif d=="2" or d=="pelear contra el moutro":
        print("\nel moutro planta inmoviliza a tu gato mutante\nes tu turno de pelear\nlogras liberar al gatito con el machete\ntu y tu gatante logran venser el moutro planta\n*felicidades el piso 4 quedo libre de moustros*")    
        d=input("\n¿Que haces?\n(1)ver por que el moustro tenia tantas ganas de ir al baño\n(2)bajar al siguiente piso\n:".lower())
        
        if d=="1" or d=="ver por que el moustro tenia tantas ganas de ir al baño":
            print("\ntocas la puerta del baño\nescuchas un grito diciendo ta ocupao\nle dices a pape que pare de jugar y que te acompañe a buscar nas sibrevivientes?\n*felicidades pepe se a unido a tu equipo")
            pq=pq+1
            
        elif d=="2" or d=="bajar al siguiente piso":
            print("\nignoras el los llantos y decides irte")    

d=input("\nbajas al siguiente piso\nte encuetras a dos moutros en el pasillo\nlogras acabar con ellos\n¿Que hacer?\n(1)explorar los apartamentos\n(2)bajar al siguiente piso\n:".lower())

if d=="1" or d=="explorar los apartamentos":   
   d=input("\n¿por cual empiezas?\n(1)apartamento 1\n(2)apartameto 2\n(3)apartamento 3\n:".lower())   
   if (d=="1" or d=="apartamento 1") or (d=="3" or d=="apartamento 3"):
       print("\nen el momento que abres la puerta un polvo raro inunda tus pulmones y los de tu equipo\npierde el control de tu cuerpo\nsolo les queda esperar que alguien los libre de su miseria")
       print(f"\n{n} A perdido el contro, GAME OVER")
       sys.exit()
    
   elif d=="2" or d=="apartamento 2":
       print("\nentras al apartamento 2\nal entrar la puerta se sierra de golpe\nun hongo comiensa a creser rapidamente atrapandote a ti y a todo tu equipo\nno puedes ver nada\nno puedes escuchar nada\nno puedes sentir nada")
       print(f"\n{n} A perdido el contro, GAME OVER")
       sys.exit()
       
elif d=="2" or d=="bajar al siguiente piso": 
    print("decides ignorar todo el piso 3 y bajar al piso 2")    

d=input("\nbajas al segundo piso y solo ves un cadaver en el pasillo\n¿Que haces?\n(1)bajar al primer piso\n(2)explorar los apartamento\n:".lower())

if d=="1" or d=="bajar al primer piso":
    print("\ndecides ingorar todo")

elif d=="2" or d=="explorar los apartamentos":
   print("\ndecides ariesgarte a ver los departamentos que estan abiertos solo encuentras cadaveres\nhasta que llegas al apartamento 2\ntocas la puerta y te abre la puerta paco")     
   print(f"\npaco:hola {n} sigues vivo\n{n}:hola paco ¿tu fuiste el responsabre de esta matansa?\npaco:si pero no quise abansar mas por que solo me quedan dos balas de escopeta\n{n}esperemos que sea mas que suficiente para lo que viene")
   print("\n*felicidade paco se a unido a tu equipo*")   
   pq=pq+1

d=input("\nbajas al primer piso\nal bajar notas que el piso y las paredes estan cubiertas de una carne palpitante\na lo lejos se ve una criatura cubierta de ojo y carne\nparese ser la responsabre de la nueva decoracion\nla carne de las paredes bloque la cualquier salida\n¿Que haces?\n(1)matar\n(2)morir\n:".lower())

if (d=="1" or d=="matar") and pq<4:
    print("\nluchas con todo pero el enemigo es demaciado fuerte\nmientras la carne te consume piensas\n¿que pude haber echo diferente para evitar este destino?")
    print(f"\n{n} A muerto, GAME OVER")
    sys.exit()

elif (d=="1" or d=="matar") and pq==4:  
    print("\ndespues de tanta preparacion te sientes invensible\ntu junto a tu quico se preparan para matar al moutro\npaco dispara dos escopetaso y eso fue suficiente para acabar con el moustro\n*felicidades ya pueden salir del edificio*\npero")
    print("\ncuando salen ven que las cosas que mataron no se comparan a lo que ven\ndecenas de mutaciones grotescas de tamaño descomunal matando entre si\nmientras que ves como una de esas cosa se acerca a su direccion\nsolo te queda rogar que tu muerte se rapida y sin dolor")
    print("\nFin")
    sys.exit()
    
elif (d=="2" or d=="morir") and pq<4:
    print("\n¿como que moiri? tu tienes que matar")
    print("\nluchas con todo pero el enemigo es demaciado fuerte\nmientras la carne te consume piensas\n¿que pude haber echo diferente para evitar este destino?")
    print(f"\n{n} A muerto, GAME OVER")
    sys.exit()
    
elif (d=="2" or d=="morir") and pq==4: 
    print("\n¿como que moiri? tu tienes que matar") 
    print("\ndespues de tanta preparacion te sientes invensible\ntu junto a tu quico se preparan para matar al moutro\npaco dispara dos escopetaso y eso fue suficiente para acabar con el moustro\n*felicidades ya pueden salir del edificio*\npero")
    print("\ncuando salen ven que las cosas que mataron no se comparan a lo que ven\ndecenas de mutaciones grotescas de tamaño descomunal matando entre si\nmientras que ves como una de esas cosa se acerca a su direccion\nsolo te queda rogar que tu muerte se rapida y sin dolor")
    print("\nFin")
    sys.exit()
    
    