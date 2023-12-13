# Sistema de Cadastro para Lanchonete com Flet

Sistema completo para gestão de pedidos em lanchonete, com interface desenvolvida com o framework Flet, incluindo cadastro de itens, cálculo de preços, emissão de nota fiscal em PDF e mais.

Funcionalidades
O sistema conta com diversas funcionalidades:

Tela de cadastro de novos pedidos:
Campos para preencher nome, endereço e itens do cliente
Adiciona os itens em uma lista
Calcula preço total randomicamente para cada item
Exibe todos os pedidos já cadastrados em uma lista
Para cada item nas listas, mostra o nome, quantidade e preço total
Botão para emitir a nota fiscal de todos os pedidos
Geração da nota fiscal em PDF utilizando ReportLab
Nota fiscal contém:
Dados do cliente
Lista de todos os itens e quantidades
Data da emissão
Total do pedido
Permite salvar o PDF da nota fiscal através de FilePicker
Pré-requisitos
Python 3.9+
Bibliotecas utilizadas:
Flet - interface declarativa
ReportLab - geração de PDFs
Copy code

pip install flet reportlab
Utilização
Executar python app.py e acessar http://localhost

Preencher os dados de cliente e dos pedidos e utilizar os botões para adicionar, imprimir e salvar a nota.

Implementação
A interface gráfica é construída com Flet, utilizando componentes como Container, Column, TextFields e Buttons.

Os dados são mantidos em listas e dicionários Python na memória.
A nota fiscal é gerada com ReportLab definindo o layout em PDF.

Preços e totalização feitos randomicamente para demonstrar funcionalidade.

Créditos
Código original de [Fulano]

Documentação estendida por Sicrano

Licença
MIT
