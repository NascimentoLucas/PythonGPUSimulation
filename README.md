# Projeto
Neste projeto simulo em um terminal um render pipeline, onde nele ocorre: Rasterização e Transformações por matrix. Tive essa idea de projeto pois queria praticar um pouco minha matemática e também python.
Nele é possível girar, escalonar e mover objetos e depois realizar o "render" no terminal.

# Rasterização
Para fazer o processo de rasterização primeiro pego as extremidades do triangulo do meu objeto a fim de fazer um quadrado. Por exemplo: do Triangulo ABC eu gero o quadrao BDEC

![image](https://github.com/NascimentoLucas/PythonGPUSimulation/assets/20142342/ef99ee48-7e4f-4cb2-bdc5-e15c3d07aba9)

Após isso eu checo com Pineda cada ponto dentro desse quadrado se ele está dentro do triangulo. Então eu pego as coordenas X e Y dos pontos que pertecem ao triangulo, e pinto na "tela" esses pontos. 

![image](https://github.com/NascimentoLucas/PythonGPUSimulation/assets/20142342/edfcc3e2-c391-4a52-9aa5-177b89bcf8e0)


# Transformações por matrix
Como a "tela" é bem limitada eu usei objetos simples, como um quadrado. Então eu a mão gero uma matrix dos vertixes desses objetos, é importante que eles estejam **centralizados**, com o meio no 0.0 já que isso influencia ao aplicar as trasnformações.

![image](https://github.com/NascimentoLucas/PythonGPUSimulation/assets/20142342/93eeb4dd-4e8f-4d92-99b8-cdf94acb3b86)
![image](https://github.com/NascimentoLucas/PythonGPUSimulation/assets/20142342/41558d3d-a0ad-4741-8d0f-e66a89eca2f1)

# Referencias
* Rastericação
  * https://www.scratchapixel.com/lessons/3d-basic-rendering/rasterization-practical-implementation/rasterization-stage.html
  * https://en.wikipedia.org/wiki/Rasterisation
* Transformações por matrix
  * https://pt.wikipedia.org/wiki/Matriz_de_transforma%C3%A7%C3%A3o
