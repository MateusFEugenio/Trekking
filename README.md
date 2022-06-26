# Trekking
Esse é um projeto desenvolvindo por ex membros do IEEE-UFJF, onde a função do mesmo a o mapeamento de lugares Hostil. 

## Nunca fez um código em Python? eu tbm não, venha e vamos aprender juntos. 

* Fique atento ao nosso projeto
#### Para o comando do Projeto foi utilizado o Raspberry py 3 com auxilio de uma Camera para o mapeamento do local de trabalho. o acionamento dos motores foi utilizado a ponte H L298N.  

* Sejam Bem vindo ao meu mundo!
 
 
 * vale se lembra que o código mais completo é o sensor infla, onde o mesmo tem como princimpal finalidade o controle do Carro através dos 3 sensores inflavermelhos localizados a frente do carro 

# Vamos a explicação de cada arquivo a cima:
* o Código chamado cd camerapai, é um código onde testamos a coneção da dispositivo de entrada camera;
* Cascade é um classificador de cone com a proporção 24 pixels por 24 pixels onde as 1800 imagens positivas foram originadas de uma imagem de cone;
* cascade10 é um classificador de cone com a proporção 20 pixels por 20 pixes utilizando 10 imagens de cone para gerar as 1800 positivas;
* classificadorCone10-24x24.xml é um classificador de cone com a proporção 24 pixels por 24 pixes utilizando 10 imagens de cone para gerar as 1800 positivas;
* piscaled.py é um código onde foi testato o Giroflex do projeto na ponteH L298n;
* pylon.jpg é o jpg usado para testar q qualidade do classificador;
* sensorinfla.py é um código base onde o nosso projeto roda sem a utilização da camera, só se orientado pelos 3 sensores infla vermelhor;
* testandomotorr.py é um código onde testamos os motores individualmente para saber a sua orientação nas portas da PonteH;
* teste.py estamos lendo a imagem via camera do Raspeberry  e retornando a posição do cone via vetor. 
