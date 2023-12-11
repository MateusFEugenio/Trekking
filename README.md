# Trekking
Esse é um projeto desenvolvindo por ex membros do IEEE-UFJF, onde a função do mesmo a o mapeamento de lugares Hostil. 

## Nunca fez um código em Python? eu tbm não, venha e vamos aprender juntos. 

* Fique atento ao nosso projeto
#### Para o comando do Projeto foi utilizado o Raspberry py 3 com auxilio de uma Camera para o mapeamento do local de trabalho. o acionamento dos motores foi utilizado a ponte H L298N.  

* Sejam Bem vindo ao meu mundo!
 
 
 * vale se lembra que o código mais completo é o sensor infla, onde o mesmo tem como princimpal finalidade o controle do Carro através dos 3 sensores inflavermelhos localizados a frente do carro 

# Vamos a explicação de cada arquivo a cima:
* camerapai é um código onde testamos a coneção da dispositivo de entrada camera;
* Cascade é um classificador de cone com a proporção 24 pixels por 24 pixels onde as 1800 imagens positivas foram originadas de uma imagem de cone;
* cascade10 é um classificador de cone com a proporção 20 pixels por 20 pixes utilizando 10 imagens de cone para gerar as 1800 positivas;
* classificadorCone10-24x24.xml é um classificador de cone com a proporção 24 pixels por 24 pixes utilizando 10 imagens de cone para gerar as 1800 positivas;
* piscaled.py é um código onde foi testato o Giroflex do projeto na ponteH L298n;
* pylon.jpg é o jpg usado para testar q qualidade do classificador;
* sensorinfla.py é um código base onde o nosso projeto roda sem a utilização da camera, só se orientado pelos 3 sensores infla vermelhor;
* testandomotorr.py é um código onde testamos os motores individualmente para saber a sua orientação nas portas da PonteH;
* teste.py estamos lendo a imagem via camera do Raspeberry  e retornando a posição do cone via vetor. 



__________________________________________________________________________________________



#Ligação do projeto:

Ponto de atenção, estamos utilizando um RaspBerry como controlador do projeto, a porta do mesmo esta sendo acionando a  como mostrado acima na imagem, coisas importantes a serem sitadas como a tabela expresssa abaixo é a respeito das tensões de liagação e acionamento do mesmo, isso é muito imporante manater a atenção, senão poderá gerar perdas de comonetes. onde para piorar ainda mais kkkk cada componete é acionado em uma tensão diferente, leia a tabela a seguir para enteder cada tensão.

|Componete|Tensão(V)|OBS:|
|----|-----|---|
|Sensor de refletancia|5V|os 5 Volt's que é a tensão de acionamento é colocado na fio Marron|
|Motores|12V|Os motores são energizado pela tensão de 12V, mas cairá para 11.1 que á tensão da bateria que iremos utilizar, onde o mesmo é manipulado pela ponte H|
|Comando PonteH|5V|existe um botão azul ON/OFF na lateral no projeto, onde a função do mesmo é manipular o projeto para acionar e desligar o projeto|
|Potencia Ponte H|11.1V|tensão essa que é dosponibilizada pela nossa bateria|
||||

O projeto tem como princimpal obejetivo o tratamento da leitura dos sensores que estão alocados a frente, muita atenção ao rodizio de manipulação do código.


|Porta RaspBerry|Componete|OBS:|
|-----|---|----|
|0|Sensor de Refletancia 1|Sensor da frente|
|5|Sensor de Refletancia 2|Sensor da Direita|
|11|Sensor de refletancia 3|Sensor da Esquerda|
|12|DireçãoA|Gira|
|13|MotorTA|Motor de trás ligado na ponte H|
|16|DireçãoB|Gira|
|19|GiroflexB|Porta ligada ao giroflex|
|20|MotorFA|Motor frente ligado a ponte H|
|21|MotorFB|Motor da frente ligado a ponte H|
|26|Giroflexa|giroflez ligado a ponte H |
||||


# Situação atual:


O projeto funciona com os 3 senores a frente, qualidade, na bateria de 2.2mAH e 11.1V ele é bem rápido, para esse código não á muitos problemas para se executado, duas cousas estão atrapalhando muito, o mla contato das peças e a respeito do projeto ter um comportamento diferente com os rodas no chão, claro o motivo é pelo peso do carro esta gerando queda de
tensão que acaarenta em um consumo de corrente maior, coisa linda coisa bela. 

*Problemas:
o projeto tem se mostrado com o código muito pesado para rodar tratando imagem, logo teremos que estudar uma forma de otimizar o código. através do mesmo após isso teremos o reconhecimento do cone em ambiente aberto. até o momento isso esta meio longe de acontecer.







oque gera maus
