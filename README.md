# Projeto em pausa

# Sistema de Cadastro para Lanchonete com Flet

&nbsp;

Sistema completo para gestão de pedidos em lanchonete. Interface gráfica desenvolvida com o framework Flet, incluindo cadastro de itens, cálculo de preços, emissão de nota fiscal em PDF e mais.
---
### Versão 1.0

&nbsp;

> Pré-requisitos>

Python 3.9+

&nbsp;
  
> Bibliotecas
 
[Flet](https://flet.dev/docs/guides/python/getting-started/)
  
[ReportLab](https://docs.reportlab.com/)

&nbsp;
&nbsp;

> Pré-code
> > virtual environment
### Feito via terminal, instalação de um ambiente virtual
    python -m venv env
    .\env\Scripts\activate

&nbsp;
&nbsp;
    
> Pré-code
> > Instalando as bibliotécas

    pip install flet reportlab


&nbsp;
&nbsp;


> Funcionalidades:

* Tela de cadastro de novos pedidos
* Campos para preencher nome, endereço e itens do cliente
* Adiciona os itens em uma lista
* Calcula preço total randomicamente para cada item
* Exibe todos os pedidos já cadastrados em uma lista
* Para cada item nas listas, mostra o nome, quantidade e preço total
* Botão para emitir a nota fiscal de todos os pedidos
* Geração da nota fiscal em PDF utilizando ReportLab
* Nota fiscal contém:
  
1- Dados do cliente

2- Lista de todos os itens e quantidades

3- Data da emissão

4- Total do pedido

5- Permite salvar o PDF da nota fiscal através de FilePicker

&nbsp;
&nbsp;

> Uso

Execute python `app.py` e acesse http://localhost:80 para utilizar a interface web.

Preencher os dados de cliente e dos pedidos e utilizar os botões para adicionar, imprimir e salvar a nota.

As funções estão disponíveis através de botões e menus.

&nbsp;
&nbsp;

### Implementação

A interface é construída com [Flet](https://flet.dev/docs/guides/python/getting-started/) utilizando componentes como `Container`, `Buttons`, `Column` e `TextFields`.

Os dados são mantidos em listas e dicionários Python na memória.

A nota fiscal é gerada com [ReportLab](https://docs.reportlab.com/) definindo o layout em `PDF`, com

preços e totalizações feitas randomicamente para demonstrar funcionalidade.

&nbsp;
&nbsp;

> Créditos


Código inicial baseado no canal [Cursos de Programação](https://www.youtube.com/watch?v=cOzpRMBfvcY&list=WL&index=24).


Documentação e melhorias adicionadas por [Wesley Pereira](https://github.com/wesleyp846)



&nbsp;
> Licença
MIT


Espero que a documentação ajude a entender a aplicação! Por favor sinta-se a vontade para melhorá-la.


# Algumas telas gráficas
