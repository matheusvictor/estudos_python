# Test Driven Development - TDD

Test Driven Development (ou, Desenvolvimento Orientado a Testes), é uma metodologia na qual o desenvolvimento de testes
vem antes do desenvolvimento de código.
A ideia é fazer com que o código, ao passar nos testes, o código esteja atendendo aquilo que era esperado na regra de
negócios

Ciclo do TDD:

Escrever Testes --> Testes irão Falhar => Implementar código para passar nos testes --> Testes passam => Refatora código

Test-Driven Development é uma metodologia para desenvolvimento de software utilizando testes e possui 3 etapas cíclicas:
Construção de Testes, Implementação de Código e Refatoração;

### Given-When-Then

### Marks

Servem para marcar qual pilha de testes serão executados.

``from pytest import mark``

Para isso, é preciso usar o decorador ``@mark`` em cima de cada método e dar a esta marcação um nome que funcionará como
etiqueta que identifica a que tipo de teste aqueles se referenciam

"Parte da razão pela qual o Pytest é conhecido como framework de testes, não uma simples biblioteca, está no fato do
Pytest possuir uma vasta gama de ferramentas direcionadas a melhorar a eficiência e organização dos testes
desenvolvidos.

Os markers ou marcadores são uma dessas ferramentas incríveis do Pytest e oferecem não somente uma forma de organizar
melhor os testes com tags personalizadas, mas colaboram para definir como determinados testes irão funcionar ou ser
executados."