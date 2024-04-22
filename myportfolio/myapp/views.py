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
    
def index_en(request):
        
    side1 = SideBar()
    side1.name = 'About me'
    side1.anchor = 'sobre-mim'

    side2 = SideBar()
    side2.name = 'Skills'
    side2.anchor = 'habilidades'

    side3 = SideBar()
    side3.name = 'My Projects'
    side3.anchor = 'meus-projetos'

    side4 = SideBar()
    side4.name = 'Contact me'
    side4.anchor = 'contate-me'
    sides = [side1, side2, side3, side4]
        
    feature1 = Features()
    feature1.name = 'Python'
    feature1.details = 'With six years of experience in Python, I have delved deep into this language, initially attracted by its applications in artificial intelligence. Over time, I have explored its capabilities in various areas, gaining proficiency in several key libraries such as NumPy, pandas, Matplotlib, Math, among others. Additionally, I have extensively used Python for backend development, employing frameworks like Django and Flask.'
    feature1.img_path = '/assets/images/python_logo.webp'

    feature2 = Features()
    feature2.name = 'C and C++'
    feature2.details = 'In the course cycle of Computer Engineering at UFSC, all programming part is done in C and C++. The use of C was mainly focused on hardware, such as microprocessors and microcontrollers, as well as embedded operating systems. On the other hand, in C++, I explored its entire object-oriented cycle, data structure, and even the architecture of operating systems. Therefore, I have solid practice and knowledge in both languages.'
    feature2.img_path = '/assets/images/clogo.png'

    feature3 = Features()
    feature3.name = 'Artificial Intelligence'
    feature3.details  = 'In the past six years, I have delved deeply into the world of artificial intelligence, focusing on computer vision, natural language processing (NLP), and machine learning. I have explored a wide range of projects, from convolutional neural networks to time series analysis, always aiming to apply AI tangibly in real-world situations. I have experience in various essential libraries such as TensorFlow, PyTorch, OpenCV, Transformers, Keras, Scikit-learn, among others.'
    feature3.img_path= '/assets/images/ai_logo.png'

    feature4 = Features()
    feature4.name = 'Full Stack'
    feature4.details = 'In the web development area, I have more experience in backend, especially using Django, Flask. However, I also have a brief knowledge of JavaScript and TypeScript applied in Node Js, while in the frontend area, I have a brief knowledge of html, css, and js and have used a bit of React Js.'
    feature4.img_path = '/assets/images/second-main-icon.png'

    feature5 = Features()
    feature5.name = 'Other Knowledge'
    feature5.details = 'I would like to mention some other topics I have knowledge of: Git, Docker, AmazonAWS, MySQL, MatLab, R, Proteus, Arduino.'
    feature5.img_path = '/assets/images/first-white-icon.png'
    features = [feature1, feature2, feature3, feature4, feature5]

    ai1 = MyProjects()
    ai1.name = 'Body Measurements Extraction'
    ai1.details = 'With just a photo and providing your height, you will receive your body measurements.'
    ai1.img_path = '/assets/images/BodyMeasure.png'

    ai2 = MyProjects()
    ai2.name = 'Ideal Clothing Size Based on Body Measurements'
    ai2.details = 'With the body measurements extraction algorithm, an application for clothing was made. This application uses the results of body measurements as input for a fuzzy logic, which determines the ideal clothing size pattern for each individual based on their unique measurements. Thus, the application returns the most suitable clothing size according to the provided body measurements. (Example photo, T-shirt)'
    ai2.img_path = '/assets/images/cloth_measure.png'

    ai3 = MyProjects()
    ai3.name = 'Facial Recognition'
    ai3.details = 'In this project, I made a facial recognition to recognize people with and without masks, I used a dataset available on the internet to train the model, as a result it would show the top 5 most likely classes to be the person in the photo, if the score was very good it showed that the person was recognized (In this experiment I put 3 photos of mine without a mask and put it to recognize one with a mask, to test the model)'
    ai3.img_path = '/assets/images/FacialRecognition.png'

    ai4 = MyProjects()
    ai4.name = 'Stock Price Prediction'
    ai4.details = 'In this project, I developed a stock price prediction model for BBAS3 stock. I used historical stock price data over the days to build the model. It was trained with data covering the period from January 2018 to December 2022 and subsequently tested with data from the first month of 2022.'
    ai4.img_path = '/assets/images/Stock_Price.png'
    ai_projects = [ai1, ai2, ai3, ai4]

    bc1 = MyProjects()
    bc1.name = 'MeasureMate'
    bc1.details = 'I applied my body measurements extraction code on a web server, using python for the backend, django as a framework, and as a frontend html, css, and js.'
    bc1.img_path = '/assets/images/MeasureMate.png'

    bc2 = MyProjects()
    bc2.name = 'Inventory Management System'
    backend_projects = [bc1]

    hd1 = MyProjects()
    hd1.name = 'Smart Fireplace'
    hd1.details = 'This project was developed using the C language, Proteus software, and a PIC 16F877A. It is a smart fireplace, designed to offer control over functions such as turn on/off, temperature adjustment, and flame intensity. An additional feature is the ability to release scents of essences chosen by the customer, providing a personalized sensory experience.'
    hd1.img_path = '/assets/images/Lareira_inteligente.png'

    hd2 = MyProjects()
    hd2.name = 'Vertical Agriculture Automation'
    hd2.details = 'Using FPGA and VHDL, I developed a control system for an automated vertical farm. The system has Temperature control (temperature sensors), Humidity Monitoring (humidity sensors), Automatic irrigation (time chosen according to each type of planting), and Lighting control (automatically adjusted to provide the ideal photoperiod for plant growth)'
    hd2.img_path = '/assets/images/Agricultura_vertical.png'
    hardware_projects = [hd1, hd2]

    ot1 = MyProjects()
    ot1.name =  'Ideal Planting Conditions System'
    ot1.details = 'I used fuzzy logic to optimize planting development, aiming to achieve the maximum growth and production potential.'
    ot1.img_path = '/assets/images/Fuzzy_estufa.png'
    outros_projects = [ot1]

    return render(request, 'index_en.html', {'features': features, 'sides': sides, 'ai_projects': ai_projects,
                                            'backend_projects': backend_projects, 'hardware_projects': hardware_projects, 'outros_projects': outros_projects})
