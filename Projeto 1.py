from flask import Flask, jsonify, request 

 

app = Flask(__name__) 

 #outro comentario aleatorio

@app.route("/") 

def calcular(): 

    # Obter os valores das bolas a partir dos parâmetros de consulta 

    bolas_azuis = int(request.args.get('bolas_azuis', 3))  # Valor padrão é 3 

    bolas_amarelas = int(request.args.get('bolas_amarelas', 4))  # Valor padrão é 4 

    bolas_verdes = int(request.args.get('bolas_verdes', 5))  # Valor padrão é 5 

 

    # Operação matemática: elevar ao quadrado e somar 

    resultado = { 

        'Bolas azuis': bolas_azuis, 

        'Bolas amarelas': bolas_amarelas, 

        'Bolas verdes': bolas_verdes, 

        'Soma dos quadrados': (bolas_azuis ** 2) + (bolas_amarelas ** 2) + (bolas_verdes ** 2) 

    } 

     

    return jsonify(resultado) 

 

if __name__ == "__main__": 

    app.run() 

#Para alterar as quantidades e realizar novo calculo, 

#acessar http://127.0.0.1:5000/?bolas_azuis= (ValorA) &bolas_amarelas= (ValorB) &bolas_verdes= (ValorC) 
#Testando