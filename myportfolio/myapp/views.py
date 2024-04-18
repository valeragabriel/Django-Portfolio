from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import SideBar, Features, MyProjects 

def index(request):
    side1 = SideBar()
    side1.name = 'Sobre mim'
    side1.anchor = 'sobre-mim'

    side2 = SideBar()
    side2.name = 'Habilidades'
    side2.anchor = 'habilidades'

    side3 = SideBar()
    side3.name = 'Meus projetos'
    side3.anchor = 'meus-projetos'

    side4 = SideBar()
    side4.name = 'Contate-me'
    side4.anchor = 'contate-me'
    sides = [side1, side2, side3, side4]

    feature1 = Features()
    feature1.name = 'Python'
    feature1.details = 'Com seis anos de experiência em Python, mergulhei profundamente nesta linguagem, inicialmente atraído por suas aplicações em inteligência artificial. Ao longo do tempo, explorei suas capacidades em diversas áreas, adquirindo proficiência em várias bibliotecas-chave, como NumPy, pandas, Matplotlib, Math, entre outras. Além disso, utilizei extensivamente o Python para o desenvolvimento de backend, empregando frameworks como Django e Flask'
    feature1.img_path = 'static/assets/images/python_logo.webp'

    feature2 = Features()
    feature2.name = 'C and C++'
    feature2.details = 'No ciclo do curso de Engenharia de Computação na UFSC, toda a parte de programação é feita em C e C++. O uso de C foi focado principalmente em hardware, como microprocessadores e microcontroladores, além de sistemas operacionais embarcados. Por outro lado, em C++, explorei todo o seu ciclo de orientação a objetos, estrutura de dados e até mesmo a arquitetura de sistemas operacionais. Portanto, possuo sólida prática e conhecimento em ambas as linguagens'
    feature2.img_path = 'static/assets/images/clogo.png'

    feature3 = Features()
    feature3.name = 'Artificial Inteligence'
    feature3.details  = 'Nos últimos seis anos, mergulhei profundamente no mundo da inteligência artificial, concentrando-me em visão computacional, processamento de linguagem natural (NLP) e aprendizado de máquina. Explorei uma ampla gama de projetos, desde redes neurais convolucionais até análise de séries temporais, sempre com o objetivo de aplicar a IA de forma tangível em situações do mundo real. Tenho experiência em várias bibliotecas essenciais, como TensorFlow, PyTorch, OpenCV, Transformers, Keras, Scikit-learn, entre outras'
    feature3.img_path= 'static/assets/images/ai_logo.png'

    feature4 = Features()
    feature4.name = 'Full Stack'
    feature4.details = 'Na área de desenvolvimento web, tenho mais experiência em backend, especialmente utilizando Django, Flaskntretanto tambem tenho um breve conhecimento em JavaScript e TypeScript aplicando em Node Js, enquanto na área do frontend tenho um breve conhecimento de html, css e js e ja utilizei um pouco de React Js'
    feature4.img_path = 'static/assets/images/second-main-icon.png'
   
    feature5 = Features()
    feature5.name = 'Outros Conhecimentos'
    feature5.details = 'Gostaria de citar alguns outros tópicos que tenho conhecimento: Git, Docker, AmazonAWS, MySQL, MatLab, R, Proteus, Arduino.'
    feature5.img_path = 'static/assets/images/first-white-icon.png'
    features = [feature1, feature2, feature3, feature4, feature5]

    ai1 = MyProjects()
    ai1.name = 'Extração de Medidas Corporais'
    ai1.details = 'Apenas com uma foto e informando sua altura, você receberá suas medidas corporais.'
    ai1.img_path = 'static/assets/images/BodyMeasure.png'

    ai2 = MyProjects()
    ai2.name = 'Tamanho de roupa ideal com base nas medidas corporais'
    ai2.details = 'Com o algoritmo de extração de medidas corporais, foi feito uma aplicação para vestuário.Esta aplicação utiliza os resultados das medidas corporais como entrada para uma lógica fuzzy, que determina o padrão de tamanho de roupas ideal para cada indivíduo com base em suas medidas únicas. Desta forma, a aplicação retorna o tamanho de roupa mais adequado de acordo com as medidas corporais fornecidas. (foto de exemplo, camiseta)'
    ai2.img_path = 'static/assets/images/cloth_measure.png'

    ai3 = MyProjects()
    ai3.name = 'Reconehcimento Facial'
    ai3.details = 'Neste projeto eu fiz um reconhecimento facial para reconhecer pessoas com mascara e sem mascara, utilizei um dataset disponivel na internet para treinar o modelo, como resultado mostraria as top 5 classes mais provaveis de ser a pessoa que esta na foto, caso o score fosse muito bom mostrava que a pessoa foi reconhecida (Nesse experimento eu coloquei 3 fotos minhas sem mascara e coloquei para reconhecer uma com mascara, para testar o modelo)'
    ai3.img_path = 'static/assets/images/FacialRecognition.png'

    ai4 = MyProjects()
    ai4.name = 'Previsão no Preço de Ações'
    ai4.details = 'Neste projeto, desenvolvi um modelo de previsão de preços da ação BBAS3. Utilizei os dados históricos de preços das ações ao longo dos dias para construir o modelo. Ele foi treinado com dados abrangendo o período de janeiro de 2018 a dezembro de 2022 e posteriormente testado com os dados do primeiro mês de 2022'
    ai4.img_path = 'static/assets/images/Stock_Price.png'
    ai_projects = [ai1, ai2, ai3, ai4]

    bc1 = MyProjects()
    bc1.name = 'MeasureMate'
    bc1.details = 'Apliquei o meu código de extração de medidas corporais em um servidor web, utilizando python pro beckend, django como framework e como frontend html, css e js.'
    bc1.img_path = 'static/assets/images/MeasureMate.png'
    
    bc2 = MyProjects()
    bc2.name = 'Sistema de Gerenciamento de Estoque'
    backend_projects = [bc1]

    hd1 = MyProjects()
    hd1.name = 'Lareira Smart'
    hd1.details = '"Este projeto foi desenvolvido utilizando a linguagem C, o software Proteus e um PIC 16F877A. Trata-se de uma lareira inteligente, projetada para oferecer controle sobre funções como ligar/desligar, ajuste de temperatura e intensidade das chamas. Uma característica adicional é a capacidade de liberar aromas de essências escolhidas pelo cliente, proporcionando uma experiência sensorial personalizada'
    hd1.img_path = 'static/assets/images/Lareira_inteligente.png'


    hd2 = MyProjects()
    hd2.name = 'Automatização de uma agricultura vertical'
    hd2.details = 'Utilizando FPGA e VHDL, desenvolvi um sistema de controle para uma fazenda vertical automatizada. O sistema possui controle de Temperatura (sensores de temperatura), Monitoramento de Umidade (sensores de umidade), Irrigação automática (escolhido o tempo conforme cada tipo de plantio) e Controle de iluminção (ajustado automaticamente para fornecer o fotoperíodo ideal para o crescimento das plantas)'
    hd2.img_path = 'static/assets/images/Agricultura_vertical.png'
    hardware_projects = [hd1, hd2]


    ot1 = MyProjects()
    ot1.name =  'Sistema de condicoes ideais para o plantio desejado'
    ot1.details = 'Empreguei lógica fuzzy para otimizar o desenvolvimento do plantio, visando alcançar o máximo potencial de crescimento e produção'
    ot1.img_path = 'static/assets/images/Fuzzy_estufa.png'
    outros_projects = [ot1]

    return render(request, 'index.html', {'features': features, 'sides': sides, 'ai_projects': ai_projects,
                                               'backend_projects': backend_projects, 'hardware_projects': hardware_projects, 'outros_projects': outros_projects})


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        name = request.POST.get('name')
                
        send_mail(
            name,
            email,
            subject,
            message,
            ['gabrielgavalera@gmail.com'],
            fail_silently=False
        )        
    return render(request, 'index.html')      
    