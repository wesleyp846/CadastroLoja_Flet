import flet as ft
from flet import *
import random
import datetime
import os
#import para parte de imprimir recibo
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle

casa=True

now=datetime.datetime.now()
formated_data=now.strftime('%d-%m-%Y')

def main(page:ft.Page):
    page.theme_mode='dark'
    page.scroll = 'auto'
    page.window_width = 600
    page.window_height = 700

    all_food = Column()

    def addtofood(e):
        random_price=random.randint(50,100)
        total_price=random_price * int(con_input.content.controls[4].value)
        all_food.controls.append(
            Container(
                padding=10,
                bgcolor='green200',
                content=Column([
                    #pegando o valor de con_input o terceiro valor que é 'Nome comida'
                    Text(con_input.content.controls[3].value,
                        weight='bold',
                        color='black',
                        size=20
                    ),
                    
                    Text(f'{con_input.content.controls[4].value}',
                        weight='bold',
                        color='black',
                        size=20
                    ),

                    Row([
                        Text('Total a pagar', width='bold',color='black'),
                        Text(f"R${'{:,.2f}'.format(total_price)}",color='black')
                    ], alignment='spaceBetween')
                ])
            )
        )

        page.update()

    con_input = Container(
        content=Column([
            TextField(label='Nome do usuario'),
            TextField(label='Endereço'),
            Text('faça seu pedido', size=25,weight='bold'),
            TextField(label='Nome comida'),
            TextField(label='Compra por peças'),
            ElevatedButton(
                'Cadastrar o pedido',
                on_click=addtofood
            )
        ])
    )

    def saveminhanota(e:FilePickerResultEvent):
        you_file_save_location=e.path

        file_path=f'{you_file_save_location}.pdf'
        doc = SimpleDocTemplate(file_path,pagesizes=letter)

        elements=[]

        styles =getSampleStyleSheet()
        elements.append(Paragraph('Recibo de compra', styles['title']))
        customer_name = con_input.content.controls[0].value

        elements.append(Paragraph(f'Nome: {customer_name}', styles['Normal']))

        elements.append(Paragraph(f'Data do pedido: {formated_data}', styles['Normal']))

        address = con_input.content.controls[1].value
        elements.append(Paragraph(f'Endereço do cliente: {address}', styles['Normal']))
       
        elements.append(Paragraph(f'Descrição dos pedidos', styles['Heading1']))

        list_order=[]
        list_order.append(['Pedido', 'Quantidade', 'Preço'])

        for b in all_food.controls:
            list_order.append([
                b.content.controls[0].value,
                b.content.controls[1].value.replace('R$', '').replace(',', ''),
                b.content.controls[2].controls[1].value.replace('R$', '').replace(',', ''),
            ])

        table=Table(list_order)

        table.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,0),colors.grey),
            ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
            ('ALIGN',(0,0),(-1,0),'CENTER'),
            ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
            ('FONTSIZE',(0,0),(-1,0),14),
            ('BOTTOMPADDING',(0,0),(-1,0),12),

            ('BACKGROUND',(0,0),(-1,-1),colors.beige),
            ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('FONTNAME',(0,0),(-1,-1),'Helvetica'),
            ('FONTSIZE',(0,0),(-1,-1),14),
            ('BOTTOMPADDING',(0,0),(-1,-1),8),
        ]))

        elements.append(table)
        grand_total = sum([float(row[2]) for row in list_order[1:]])
        elements.append(Paragraph(f'Total da compra: R${grand_total:.2f}', styles['Heading1']))

        doc.build(elements)

    file_saver = FilePicker(
        on_result=saveminhanota
    )

    page.overlay.append(file_saver)

    def buildmeupedido(e):
        mdialog=AlertDialog(
            title=Text(
                'Nota dos pedidos',
                weight='blod',
                size=30,
                ),

            content=Column([
                Row([
                    #Nome do cliente
                    Text(f'Cliente: {con_input.content.controls[0].value}',
                        weight='bold',
                        color='black',
                        size=25,
                        text_align='CENTER'
                    ),
                ]),
                #Data do pedido
                Text(f'Data do pedido: {formated_data}',
                    weight='bold',
                    color='black',
                    size=25
                ),
                
                Text(f'Endereço: {con_input.content.controls[1].value}',
                    weight='bold',
                    color='black',
                    size=25,
                    text_align='start'
                ),
                
                Text(
                    'Seus pedidos',
                    weight='bold',
                    color='black',
                    size=25
                ),
                
                all_food
            ],
            scroll='auto'),
            actions=[
                ElevatedButton(
                    'Impromir rcibo',
                    bgcolor='blue',
                    color='red',
                    on_click=lambda e:file_saver.save_file()
                )
            ]
        )
        page.dialog=mdialog
        mdialog.open=True
        page.update()

    page.floating_action_button = FloatingActionButton(
        icon='add', 
        bgcolor='blue',
        on_click=buildmeupedido 
    )

    page.add(
        Column([
            con_input,
            Text('Lista de pedidos', size=20,weight='bold'),
            all_food
        ])
    )
    

ft.app(target=main) if casa else ft.app(target=main, view=ft.AppView.WEB_BROWSER)